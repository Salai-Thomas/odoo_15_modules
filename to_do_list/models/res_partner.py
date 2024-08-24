from odoo import fields, models

class InheritedResPartner(models.Model):
    _inherit = 'res.partner'

    is_work_team = fields.Boolean('Is Work Team?')
