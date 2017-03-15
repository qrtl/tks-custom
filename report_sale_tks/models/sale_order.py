# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from itertools import groupby
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    category_desc_ids = fields.One2many(
        comodel_name='sale.layout_category.desc',
        inverse_name='sale_order_id',
        string='Section Description',
    )


    # override the standard method
    @api.multi
    def order_lines_layouted(self):
        """
        Returns this order lines classified by sale_layout_category and separated in
        pages according to the category pagebreaks. Used to render the report.
        """
        self.ensure_one()
        report_pages = [[]]
        for category, lines in groupby(self.order_line, lambda l: l.layout_category_id):

            # get description and subtotal from SO category descs [OSCG]
            description = ''
            hide_price = False
            subtotal = False
            pagebreak = False
            if category:
                category_desc = self.category_desc_ids.search(
                    [('sale_order_id', '=', self.id),
                     ('layout_category_id', '=', category.id)]
                )
                if category_desc:
                    description = category_desc[0].name
                    hide_price = category_desc[0].hide_price
                    subtotal = category_desc[0].subtotal
                    pagebreak = category_desc[0].pagebreak

            # If last added category induced a pagebreak, this one will be on a new page
            if report_pages[-1] and report_pages[-1][-1]['pagebreak']:
                report_pages.append([])
            # Append category to current report page
            report_pages[-1].append({
                'name': category and category.name or 'Uncategorized',
                'description': description, # added [OSCG]
                'hide_price': hide_price,
                # 'subtotal': category and category.subtotal, # deleted [OSCG]
                'subtotal': subtotal,  # added [OSCG]
                # 'pagebreak': category and category.pagebreak, # del [OSCG]
                'pagebreak': pagebreak,
                'lines': list(lines)
            })

        return report_pages
