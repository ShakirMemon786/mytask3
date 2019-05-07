# -*- coding: utf-8 -*-
from flectra import api, fields, models


class CustomerDetails(models.Model):
    _name = "customer.details"



    name = fields.Char(string="Name of Customer")
#    degree = fields.Selection([('be', 'BE'),('bca', 'BCA')], string="Degree",)
    user_email = fields.Char(type="char", string="Customer Email", copy=False)
#    job_id = fields.Many2one('job.details', "Applied Job")
#    salary_proposed = fields.Float(string="Proposed Salary")
#   salary_expected = fields.Float(string="Expected Salary")
#    availability = fields.Date(string="Availability")
#    phone = fields.Char("Phone", size=12, copy=False)
    mobile = fields.Char("Mobile", size=12)
    _sql_constraints = [
        ('name_uniq', 'unique (mobile)', 'The mobile number of the job seeker must be unique!'), ('name_uniq', 'unique (user_email)', 'The email of the job Seeker for Recruitment must be unique!')
    ]
#    type_id = fields.Many2one('hr.recruitment.degree', "Degree")
#    company_id = fields.Many2one('company.details', "Companys")
    product_details_ids = fields.Many2many("product.details","product_cust_rel","customer_details_id", "product_details_id", string="Product Details")
    complaints_id = fields.One2many("complaints.data", 'customer_details_line', string="complaints")

    state = fields.Selection([('ordered', 'Ordered'),('depart', 'Depart'),('cancle', 'Cancle')], readonly=True)
#    bank_id = fields.Many2one("bank.name", required=True, string="Bank")
#    account_line = fields.One2many("account.details", 'bank_id', string = "Accounts", readonly="True")


    @api.multi
    def button_ordered(self):
            self.state = "ordered"

    @api.multi
    def button_depart(self):
        self.state = "depart"

    @api.multi
    def button_cancle(self):
        self.state = "cancle"
