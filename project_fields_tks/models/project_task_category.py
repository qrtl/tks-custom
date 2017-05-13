# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import api, fields, models


class ProjectTaskCategory(models.Model):
    _name = 'project.task.category'
    _description = 'Task Category'

    name = fields.Char(
        string='Category Name',
        required=True,
        translate=True
    )
    code = fields.Char(
        string='Code',
        required=True,
    )
    sequence = fields.Integer(default=1)
