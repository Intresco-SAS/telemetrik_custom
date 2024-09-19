from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_producer = fields.Char(string='Fabricante')