# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookCategory(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one(comodel_name="res.partner", required=True)
    category_id = fields.Many2many(comodel_name="library.book.category")


class BookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(string="Name", required=True, unique=True)

