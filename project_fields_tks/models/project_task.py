# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api, _
from odoo.exceptions import Warning


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
    date_project_due = fields.Date(
        related='project_id.date',
        string='Project Due Date',
    )
    """ make partner_id a related field """
    partner_id = fields.Many2one(
        related='project_id.partner_id',
    )
    plant = fields.Boolean(
        related='category_id.plant',
        readonly=True,
    )


    @api.multi
    def write(self, vals):
        if 'project_id' in vals:
            new_proj = self.env['project.project'].browse(vals['project_id'])
            for task in self:
                # there should be no warning when a new project is created
                # by copying a template project
                if not task.project_id.is_template and \
                                new_proj != task.project_id:
                    raise Warning(
                        _('Task cannot be moved to another project.'))
        res = super(ProjectTask, self).write(vals)
        return res
