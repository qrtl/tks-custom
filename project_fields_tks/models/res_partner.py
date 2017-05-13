# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    cad_partner = fields.Boolean(
        string="CAD Partner",
    )
