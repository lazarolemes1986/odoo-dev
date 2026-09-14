from odoo import models, fields

class Categoria(models.Model):
    _name ="mi.categoria"
    _description = "Categoria"

    name =fields.Char(string="Nombre", required=True)
    descripcion =fields.Text(string="Descripcion")
    active = fields.Boolean(string="Activa", default = True)

    producto_ids=fields.One2many(
        "mi.producto",
        "categoria_id",
        string="Productos"
    )