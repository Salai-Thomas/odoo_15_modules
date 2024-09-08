from odoo import fields, models,api

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


    @api.model
    def create(self, vals):
        partner_id = self.env.user.partner_id.id
        if 'work_team_ids' in vals:
            # Add the current user's partner if it's not already in the list
            vals['work_team_ids'].append((4, partner_id))
        else:
            # If 'work_team_ids' is not present, create it and add the current user's partner
            vals['work_team_ids'] = [(4, partner_id)]

        return super(TodoItem, self).create(vals)
