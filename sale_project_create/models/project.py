# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Project(models.Model):
    _inherit = 'project.project'

    is_template = fields.Boolean(
        string="Template Project",
    )
    so_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sales Order',
    )
