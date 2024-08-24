from odoo import fields, models

class TodoItem(models.Model):
    _name = 'todo.item'

    name = fields.Char(string='Name')
    is_done = fields.Boolean(string='Is Done?')
    work_team_ids = fields.Many2many('res.partner',string='Work Team')