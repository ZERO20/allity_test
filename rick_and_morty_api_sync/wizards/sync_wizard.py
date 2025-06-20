# -*- coding: utf-8 -*-
import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class RickMortySyncWizard(models.TransientModel):
    _name = 'rick.morty.sync.wizard'
    _description = 'Rick and Morty Synchronization Wizard'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('error', 'Error')
    ], default='draft', string='State')

    error_message = fields.Text(string='Error Message')

    def action_sync(self):
        """Execute the synchronization process"""
        try:
            self.env['rick.morty.character'].action_sync_characters()
            self.write({'state': 'done'})
        except Exception as e:
            _logger.error("Error during sync: %s", str(e))
            self.write({
                'state': 'error',
                'error_message': str(e)
            })

        return self.action_refresh()

    def action_cancel(self):
        """Close the wizard"""
        return {'type': 'ir.actions.act_window_close'}

    def action_refresh(self):
        """Refresh the wizard view"""
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
