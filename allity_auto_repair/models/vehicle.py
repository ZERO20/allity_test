# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = 'Vehicle'
    _order = 'brand_id, model_id, year desc'

    name = fields.Char(
        string='Name',
        compute='_compute_name',
        store=True,
        help='Automatic name based on brand, model and license plate'
    )

    brand_id = fields.Many2one(
        'vehicle.brand',
        string='Brand',
        required=True,
        help='Vehicle brand'
    )

    model_id = fields.Many2one(
        'vehicle.model',
        string='Model',
        required=True,
        domain="[('brand_id', '=', brand_id)]",
        help='Vehicle model filtered by brand'
    )

    vehicle_type_id = fields.Many2one(
        'vehicle.type',
        string='Type',
        required=True,
        help='Vehicle type (Auto, Pick-UP, Suburban, Hybrid, etc.)'
    )

    year = fields.Char(
        string='Year',
        required=True,
        help='Vehicle year'
    )

    color = fields.Char(
        string='Color',
        required=True,
        help='Vehicle color'
    )

    license_plate = fields.Char(
        string='License Plate',
        required=True,
        help='Vehicle license plate'
    )

    notes = fields.Text(
        string='Notes',
        help='Additional vehicle observations'
    )

    active = fields.Boolean(
        string='Active',
        default=True,
        help='If not marked, allows hiding the vehicle without deleting it'
    )

    @api.depends('brand_id', 'model_id', 'license_plate', 'year')
    def _compute_name(self):
        for record in self:
            if record.brand_id and record.model_id and record.license_plate:
                record.name = f"{record.brand_id.name} {record.model_id.name} ({record.year}) - {record.license_plate}"
            else:
                record.name = _('New Vehicle')

    @api.onchange('brand_id')
    def _onchange_brand_id(self):
        if self.brand_id:
            self.model_id = False
            return {
                'domain': {
                    'model_id': [('brand_id', '=', self.brand_id.id)]
                }
            }
        else:
            return {
                'domain': {
                    'model_id': []
                }
            }

    def name_get(self):
        result = []
        for record in self:
            name = record.name or _('New Vehicle')
            result.append((record.id, name))
        return result


