# -*- coding: utf-8 -*-

from flectra import fields, models


class ProductFeature(models.Model):
    _name = "product.feature"

    name = fields.Char(string="Feature", size=20)
    is_Available = fields.Boolean(string="Available")
    #    product_line = fields.Many2one("product.details", string="Product")
    product_detail_ids = fields.Many2many("product.details", "product_product_feature_rel",
                                          "prod_feature_id", "prod_details_id", string="Product")
