from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Producto(models.Model):
    _name = "mi.producto"
    _description = "Mi producto"

    name = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio")
    stock = fields.Integer(string="Stock")
    valor_total = fields.Float(
        string="Valor total",
        compute="_calcular_valor_total",
        store=True,
    )

    categoria_id = fields.Many2one(
        "mi.categoria",
        string="Categoria",
    )

    @api.constrains("precio", "stock")
    def comprobar_valores(self):
        for producto in self:
            if producto.precio < 0:
                raise ValidationError("El precio no puede ser menor que 0")
            if producto.stock < 0:
                raise ValidationError("El stock no puede ser menor que cero")

    @api.depends("precio", "stock")
    def _calcular_valor_total(self):
        for record in self:
            record.valor_total = record.precio * record.stock
