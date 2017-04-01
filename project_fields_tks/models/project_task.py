# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

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
    date_startdate = fields.Date(
        string='Start Date',
        copy=False
    )
    stairs = fields.Integer(
        related='project_id.stairs',
        store=True,
        readonly=True,
        string='Stairs',
    )
    weight_stairs = fields.Float(
        related='project_id.weight_stairs',
        store=True,
        readonly=True,
        string='Weight',
    )
    handrail = fields.Float(
        related='project_id.handrail',
        store=True,
        readonly=True,
        string='Handrail',
    )
    weight_handrail = fields.Float(
        related='project_id.weight_handrail',
        store=True,
        readonly=True,
        string='Weight',
    )
    project_state = fields.Selection(
        related='project_id.state',
        store=True,
        readonly=True,
        string='Project State',
    )
