# -*- coding: utf-8 -*-
from odoo import models, fields


class VehicleType(models.Model):
    _name = 'vehicle.type'
    _description = 'Vehicle Type'
    _order = 'name'

    name = fields.Char(
        string='Name',
        required=True,
        help='Type of vehicle (Auto, Pick-UP, Suburban, Hybrid, etc.)'
    )

    description = fields.Text(
        string='Description',
        help='Detailed description of the vehicle type'
    )

    active = fields.Boolean(
        string='Active',
        default=True,
        help='If not marked, allows hiding the type without deleting it'
    )
