# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_type = fields.Selection(
        related='project_id.type',
        store=True,
        string='Project Type',
        readonly=True,
    )
    category_id = fields.Many2one(
        comodel_name='project.task.category',
        string='Category',
        required=True
    )
    category_code = fields.Char(
        related='category_id.code',
        string='Code',
        store=True,
    )
    category_sequence = fields.Integer(
        string='Category Sequence',
        related='category_id.sequence',
        store=True,
        index=True,
        readonly=True,
    )
    stairs = fields.Integer(
        related='project_id.stairs',
        store=True,
        readonly=True,
        string='Stairs (sets)',
    )
    handrail = fields.Float(
        related='project_id.handrail',
        store=True,
        readonly=True,
        string='Handrail (m)',
    )
    weight = fields.Float(
        related='project_id.weight',
        store=True,
        readonly=True,
        string='Weight (kg)',
    )
    project_state = fields.Selection(
        related='project_id.state',
        store=True,
        readonly=True,
        string='Project State',
    )
