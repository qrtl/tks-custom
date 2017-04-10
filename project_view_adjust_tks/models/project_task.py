# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'


    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        kanban_sort = self.env.context.get('kanban_sort')
        if kanban_sort:
            order = "category_sequence, date_deadline"
        return super(ProjectTask, self).search(
            args, offset=offset, limit=limit, order=order, count=count
        )
