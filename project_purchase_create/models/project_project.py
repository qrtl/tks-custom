# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Project(models.Model):
    _inherit = 'project.project'

    purchase_ids = fields.One2many(
        comodel_name='purchase.order',
        inverse_name='project_id',
        string='Purchase Orders',
        copy=False,
    )


    @api.multi
    def action_view_purchase(self):
        '''
        This function returns an action that display existing purchase orders
        of given project ids.
        When only one found, show the purchase order immediately.
        '''
        action = self.env.ref('purchase.purchase_form_action')
        result = action.read()[0]

        # override the context
        result['context'] = {'default_project_id': self.id}

        # choose the view_mode accordingly
        if len(self.purchase_ids) != 1:
            result['domain'] = \
                "[('id', 'in', " + str(self.purchase_ids.ids) + ")]"
        elif len(self.purchase_ids) == 1:
            res = self.env.ref('purchase.purchase_order_form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = self.purchase_ids.id
        return result
