# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleLayoutCategoryDesc(models.Model):
    _inherit = 'sale.layout_category.desc'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
    )


    @api.multi
    @api.onchange('layout_category_id')
    def onchange_layout_category(self):
        self.ensure_one()
        if self.layout_category_id:
            self.name = self.layout_category_id.name
        else:
            self.name = False
        return
