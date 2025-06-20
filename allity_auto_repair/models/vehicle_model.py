# -*- coding: utf-8 -*-
from odoo import models, fields, api


class VehicleModel(models.Model):
    _name = 'vehicle.model'
    _description = 'Vehicle Model'
    _order = 'brand_id, name'

    name = fields.Char(
        string='Model Name',
        required=True,
        help='Name of the vehicle model'
    )

    brand_id = fields.Many2one(
        'vehicle.brand',
        string='Brand',
        required=True,
        ondelete='cascade',
        help='Brand to which this model belongs'
    )

    active = fields.Boolean(
        string='Active',
        default=True,
        help='If not marked, allows hiding the model without deleting it'
    )

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.brand_id.name} {record.name}"
            result.append((record.id, name))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:
            # search by model name or brand name
            domain = ['|', ('name', operator, name), ('brand_id.name', operator, name)]
            records = self.search(domain + args, limit=limit, access_rights_uid=name_get_uid)
            return records.name_get()
        return super(VehicleModel, self)._name_search(name, args, operator, limit, name_get_uid)
