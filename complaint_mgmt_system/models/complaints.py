# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Complaints(models.Model):
    _name = "complaints.data"

    name = fields.Char(string="Complaints", size=60)
    customer_details_line = fields.Many2one("customer.details", string="customers")
    #is_Available = fields.Boolean(string="Available")
    #product_line = fields.Many2one("product.details", string="Product")

#    vehical_ids = fields.Many2many("vehical.data", "vehical_feature_rel",
#                                   "feature_id", "vehical_id",  string="Vechiles")
