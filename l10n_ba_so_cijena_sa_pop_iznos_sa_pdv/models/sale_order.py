# -*- coding: utf-8 -*-

from odoo import models, fields, _, api
import re

PATTERN = r'^\[.*?\]\s*'

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    name_without_ref = fields.Char(
        string="Name without REF",
        compute='_compute_name_without_ref',
        store=False)

    @api.depends('name')
    def _compute_name_without_ref(self):
        for line in self:
            line.name_without_ref = re.sub(PATTERN, '', line.name)
