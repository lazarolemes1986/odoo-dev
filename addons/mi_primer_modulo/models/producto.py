from odoo import models, fields

class Producto (models.Model):
    _name = "mi.producto"
    _description = "Mi producto"

    name = fields.Char(string="Nombre")
    categoria = fields.Char(string="Categoría")
    precio = fields.Float(string="Precio")
    stock= fields.Integer(string="Stock")


