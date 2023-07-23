# -*- coding: utf-8 -*-
# Part of Intresco. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import Warning
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class RequisitionLine(models.Model):
    _inherit = "requisition.line"
    
    @api.onchange('product_id')
    def onchange_requisition_action(self):
        if self.product_id.type != 'service':
            self.requisition_action = 'internal_picking'
        else:
            self.requisition_action = 'purchase_order'  
    
    
    #requisition_action = fields.Selection(default='internal_picking')
