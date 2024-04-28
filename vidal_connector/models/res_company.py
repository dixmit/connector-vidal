# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    vidal_client_id = fields.Char(string="Client ID")  # Our identifier
    vidal_client_secret = fields.Char(string="Client Secret")
