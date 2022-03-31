# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountAnalyticTag(models.Model):
    _inherit = 'account.analytic.tag'

    hours = fields.Integer(string='Hours', default=120)


class AccountAnalyticDistribution(models.Model):
    _inherit = 'account.analytic.distribution'

    worked_hours = fields.Float(string='Worked Hours')

    @api.onchange('worked_hours')
    def _onchange_worked_hours(self):
        if self.worked_hours and self.tag_id and self.tag_id.hours:
            self.percentage = self.worked_hours / self.tag_id.hours * 100
        if self.worked_hours and not self.tag_id and self._context.get('hours'):
            self.percentage = self.worked_hours / self._context.get('hours') * 100
