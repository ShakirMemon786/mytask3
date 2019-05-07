# -*- coding: utf-8 -*-
from flectra import api, fields, models


class ProductDetails(models.Model):
    _name = "product.details"

    name = fields.Char(string="Product Name", )
    description = fields.Text(string="Description")
    published_date = fields.Date(string="Published date")
    price = fields.Float(String="Price")
    product_image = fields.Binary(string="Product image")
    product_feature_ids = fields.Many2many("product.feature", "product_product_feature_rel", 'prod_feature_id',
                                           'prod_details_id', string="Features")
    customer_details_ids = fields.Many2many("customer.details", "product_cust_rel", 'customer_details_id',
                                            'product_details_id', string='Customers')
