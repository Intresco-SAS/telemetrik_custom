# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api, _


class AccountAnalyticTag(models.Model):
    _inherit = 'account.analytic.tag'

    hours = fields.Integer(string='Hours', default=120)
    analytic_distribution_ids = fields.One2many(copy=True) #Se edita el campo para poder duplicar la tabla con todos los valores

    def write(self, vals):
        res = super(AccountAnalyticTag, self).write(vals)
        for tag in self:
            if tag.active_analytic_distribution:
                total_worked_hours = sum(tag.analytic_distribution_ids.mapped('worked_hours'))
                total_percentage = sum(tag.analytic_distribution_ids.mapped('percentage'))
                total_percentage_1 = round(sum(tag.analytic_distribution_ids.mapped('percentage')))
                if total_worked_hours != tag.hours or total_percentage_1 != 100:
                    msg = "Total worked hours %s not matched with %s OR total percentage %s not match with 100" % (str(total_worked_hours), str(tag.hours), str(total_percentage))
                    raise ValidationError(_(msg))
        return res

    @api.model
    def create(self, vals):
        res = super(AccountAnalyticTag, self).create(vals)
        for tag in res:
            if tag.active_analytic_distribution:
                total_worked_hours = sum(tag.analytic_distribution_ids.mapped('worked_hours'))
                total_percentage = sum(tag.analytic_distribution_ids.mapped('percentage'))
                total_percentage_1 = round(sum(tag.analytic_distribution_ids.mapped('percentage')))
                if total_worked_hours != tag.hours or total_percentage_1 != 100:
                    msg = "Total worked hours %s not matched with %s OR total percentage %s not match with 100" % (str(total_worked_hours), str(tag.hours), str(total_percentage))
                    raise ValidationError(_(msg))
        return res


class AccountAnalyticDistribution(models.Model):
    _inherit = 'account.analytic.distribution'

    worked_hours = fields.Float(string='Worked Hours')

    @api.onchange('worked_hours')
    def _onchange_worked_hours(self):
        if self.worked_hours and self.tag_id and self.tag_id.hours:
            self.percentage = self.worked_hours / self.tag_id.hours * 100
        if self.worked_hours and not self.tag_id and self._context.get('hours'):
            self.percentage = self.worked_hours / self._context.get('hours') * 100

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_producer = fields.Char(string='Fabricante')