# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    category_id = fields.Many2one(
        comodel_name='project.task.category',
        string='Category',
        required=True
    )
    category_sequence = fields.Integer(
        string='Category Sequence',
        related='category_id.sequence',
        store=True,
        readonly=True,
    )
