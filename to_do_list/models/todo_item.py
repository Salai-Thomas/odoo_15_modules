from odoo import fields, models

class TodoItem(models.Model):
    _name = 'todo.item'

    name = fields.Char(string='Name')
    is_done = fields.Boolean()
    label_done = fields.Char(string='Status',compute="_compute_dynamic_label",readonly=1)
    work_team_ids = fields.Many2many('res.partner',string='Work Team')

    def _compute_dynamic_label(self):
        for record in self:
            if record.is_done:
                record.label_done = 'Done'
            else:
                record.label_done = 'Not Done'