# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one(comodel_name="res.partner", required=True)
    category_id = fields.Many2many(comodel_name="library.book.category")


class BookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    
    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise ValidationError("The category name must be unique!")
