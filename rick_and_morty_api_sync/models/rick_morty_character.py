# -*- coding: utf-8 -*-
import base64
import logging

import requests

from odoo import models, fields, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class RickMortyCharacter(models.Model):
    _name = 'rick.morty.character'
    _description = 'Rick and Morty Characters'
    _order = 'name'

    name = fields.Char(
        string='Name',
        required=True,
        help='Name of the character'
    )

    api_id = fields.Integer(
        string='ID',
        help='ID of the character in the Rick and Morty API',
        readonly=True
    )

    image = fields.Binary(
        string='Image',
        help='Image of the character'
    )

    def _character_exists_by_api_id(self, api_id):
        """Check if a character exists by API ID using search_count for better performance"""
        return self.search_count([('api_id', '=', api_id)]) > 0

    def _get_existing_character_by_api_id(self, api_id):
        """Get existing character by API ID"""
        return self.search([('api_id', '=', api_id)], limit=1)

    def action_sync_characters(self):
        """Action to synchronize characters from the Rick and Morty API"""
        try:
            # URL of the API (gets first 20 characters by default)
            api_url = 'https://rickandmortyapi.com/api/character'

            _logger.info(_("Getting data from: %s") % api_url)
            response = requests.get(api_url, timeout=30)
            response.raise_for_status()
            data = response.json()

            processed_count = 0
            created_count = 0
            updated_count = 0

            for character_data in data.get('results', []):
                processed_count += 1
                api_id = character_data.get('id')
                character_vals = self._prepare_character_data(character_data)

                if self._character_exists_by_api_id(api_id):
                    existing_character = self._get_existing_character_by_api_id(api_id)
                    existing_character.write(character_vals)
                    updated_count += 1
                    _logger.info(_("Updated character: %s") % character_vals['name'])
                else:
                    self.create(character_vals)
                    created_count += 1
                    _logger.info(_("Created character: %s") % character_vals['name'])

            message = _(
                "Synchronization completed!\n"
                "- Characters processed: %d\n"
                "- Characters created: %d\n"
                "- Characters updated: %d"
            ) % (processed_count, created_count, updated_count)

            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Synchronization successful'),
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }

        except requests.exceptions.RequestException as e:
            _logger.error(_("Error connecting to the API: %s") % str(e))
            raise UserError(_(
                "Error connecting to the Rick and Morty API:\n%s"
            ) % str(e))
        except Exception as e:
            _logger.error(_("Error during synchronization: %s") % str(e))
            raise UserError(_(
                "Error during synchronization:\n%s"
            ) % str(e))

    def _prepare_character_data(self, character_data):
        """Prepare data of the character to create/update"""
        image_data = None
        image_url = character_data.get('image')
        if image_url:
            try:
                img_response = requests.get(image_url, timeout=10)
                if img_response.status_code == 200:
                    image_data = base64.b64encode(img_response.content)
            except Exception as e:
                _logger.warning(_("Error downloading image for %s: %s") % (character_data.get('name'), str(e)))

        return {
            'name': character_data.get('name', ''),
            'api_id': character_data.get('id'),
            'image': image_data,
        }
