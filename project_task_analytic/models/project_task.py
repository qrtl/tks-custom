# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'


    @api.multi
    def action_task_done(self):
        stage_obj = self.env['project.task.type']
        stage_done = stage_obj.search([('sequence', '=', 2)])
        self.write({'stage_id': stage_done.id})
        analytic_line_obj = self.env['account.analytic.line']
        for task in self:
            if task.project_id.analytic_account_id:
                analytic_line_id = analytic_line_obj.create(
                    {'name': task.name,
                     'date': fields.Date.context_today(self),
                     'account_id': task.project_id.analytic_account_id.id,
                     'unit_amount': False,
                     'amount': task.budget_amt,
                     'partner_id': task.project_id.partner_id.id,
                     'product_id': False,
                     'product_uom_id': False,
                     'general_account_id': False,
                     'ref': task.project_id.name,
                     }
                )
                task.analytic_line = analytic_line_id

    # @api.multi
    # def action_cancel(self):
    #     moves = self.env['account.move']
    #     for inv in self:
    #         if inv.move_id:
    #             moves += inv.move_id
    #         if inv.payment_move_line_ids:
    #             raise UserError(_('You cannot cancel an invoice which is partially paid. You need to unreconcile related payment entries first.'))
    #
    #     # First, set the invoices as cancelled and detach the move ids
    #     self.write({'state': 'cancel', 'move_id': False})
    #     if moves:
    #         # second, invalidate the move(s)
    #         moves.button_cancel()
    #         # delete the move this invoice was pointing to
    #         # Note that the corresponding move_lines and move_reconciles
    #         # will be automatically deleted too
    #         moves.unlink()
    #     return True
    #
    # @api.multi
    # def action_task_cancel(self):
    #     if self.filtered(lambda inv: inv.state not in ['proforma2', 'draft', 'open']):
    #         raise UserError(_("Invoice must be in draft,Pro-forma or open state in order to be cancelled."))
    #     return self.action_cancel()
