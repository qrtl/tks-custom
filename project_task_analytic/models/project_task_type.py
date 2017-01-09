# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    done_stage = fields.Boolean(
        'Done Stage'
    )
