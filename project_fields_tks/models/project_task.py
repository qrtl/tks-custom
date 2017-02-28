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
        compute='_get_stairs_handrail',
        store=True,
        readonly=True,
        string='Stairs',
    )
    weight_stairs = fields.Float(
        compute='_get_stairs_handrail',
        store=True,
        readonly=True,
        string='Weight',
    )
    handrail = fields.Float(
        compute='_get_stairs_handrail',
        store=True,
        readonly=True,
        string='Handrail',
    )
    weight_handrail = fields.Float(
        compute='_get_stairs_handrail',
        store=True,
        readonly=True,
        string='Weight',
    )


    @api.multi
    @api.depends('project_id.stairs', 'project_id.weight_stairs',
                 'project_id.handrail', 'project_id.weight_handrail',
                 'category_code')
    def _get_stairs_handrail(self):
        for task in self:
            if task.category_code == 'quotation':
                stairs = task.project_id.stairs
                weight_stairs = task.project_id.weight_stairs
                handrail = task.project_id.handrail
                weight_handrail = task.project_id.weight_handrail
            else:
                stairs = 0
                weight_stairs = 0.0
                handrail = 0.0
                weight_handrail = 0.0
            task.stairs = stairs
            task.weight_stairs = weight_stairs
            task.handrail = handrail
            task.weight_handrail = weight_handrail
        return
