# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class VehicleDiagnostic(models.Model):
    _name = 'vehicle.diagnostic'
    _description = 'Vehicle Diagnostic'
    _order = 'date desc'
    _rec_name = 'display_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    display_name = fields.Char(
        string='Name',
        compute='_compute_display_name',
        store=True,
        help='Automatic name of the diagnostic',
        tracking=True
    )

    client_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        help='Customer owner of the vehicle',
        tracking=True
    )

    vehicle_id = fields.Many2one(
        'vehicle.vehicle',
        string='Vehicle',
        required=True,
        help='Vehicle to diagnose',
        tracking=True
    )

    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.today,
        help='Date of the diagnostic',
        tracking=True
    )

    responsible_id = fields.Many2one(
        'hr.employee',
        string='Responsible of the Diagnostic',
        required=True,
        help='Employee responsible for the diagnostic (mechanic)',
        tracking=True
    )

    diagnostic_detail = fields.Text(
        string='Detail',
        required=True,
        help='Detailed information of the diagnostic performed by the mechanic',
        tracking=True
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State',
        default='draft',
        required=True,
        help='State of the diagnostic',
        tracking=True,
        copy=False
    )

    active = fields.Boolean(
        string='Active',
        default=True,
        help='If not marked, allows hiding the diagnostic without deleting it'
    )


    @api.depends('client_id', 'vehicle_id', 'date')
    def _compute_display_name(self):
        for record in self:
            if record.client_id and record.vehicle_id and record.date:
                record.display_name = _("Diagnostic - %s - %s - %s") % (record.client_id.name, record.vehicle_id.license_plate, record.date)
            else:
                record.display_name = _('New Diagnostic')

    def name_get(self):
        result = []
        for record in self:
            name = record.display_name or _('New Diagnostic')
            result.append((record.id, name))
        return result

    def action_start_diagnosis(self):
        """Start the diagnostic"""
        self.state = 'in_progress'

    def action_finish_diagnosis(self):
        """Finish the diagnostic"""
        self.state = 'done'

    def action_cancel_diagnosis(self):
        """Cancel the diagnostic"""
        self.state = 'cancelled'

    def action_reset_to_draft(self):
        """Reset to draft"""
        self.state = 'draft'
