# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one(
        string="Author", comodel_name="res.partner", required=True
    )
    category_id = fields.Many2many(
        string="Categories", comodel_name="library.book.category"
    )
