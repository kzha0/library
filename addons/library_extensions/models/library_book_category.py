# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(string="Category Name", required=True)

    _sql_constraints = [
        ("unique_name", "unique(name)", "Category name must be unique")
    ]

    @api.constrains("name")
    def _check_unique_name(self):
        for record in self:
            if self.search_count([("name", "=", record.name)]) > 1:
                raise ValidationError("The category name must be unique!")
