# -*- coding: utf-8 -*-
from odoo import models, fields


class VehicleBrand(models.Model):
    _name = 'vehicle.brand'
    _description = 'Vehicle Brand'
    _order = 'name'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The brand name must be unique')
    ]

    name = fields.Char(
        string='Name',
        required=True,
        help='Name of the vehicle brand'
    )

    active = fields.Boolean(
        string='Active',
        default=True,
        help='If not marked, allows hiding the brand without deleting it'
    )

    model_ids = fields.One2many(
        'vehicle.model',
        'brand_id',
        string='Models'
    )



