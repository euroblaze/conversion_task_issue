# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Convert(models.Model):
    _inherit = 'project.issue'

    def get_data(self):
        vals = {}
        vals['color'] = self.color
        vals['date_last_stage_update'] = self.date_last_stage_update
        vals['partner_id'] = self.partner_id.id
        vals['create_uid'] = self.create_uid.id
        vals['user_id'] = self.user_id.id
        vals['company_id'] = self.company_id.id
        vals['project_id'] = self.project_id.id
        vals['description'] = self.description
        vals['issue_id'] = self.id
        vals['kanban_state'] = self.kanban_state
        vals['name'] = self.name
        vals['stage_id'] = self.stage_id.id
        vals['date_deadline'] = self.date_deadline

        new_task = self.env['project.task'].create(vals)
        if new_task:
            for msg in self.message_ids:
                msg.write({'res_id' : new_task.id, 'model' : 'project.task'})
            if self.timesheet_ids:
                for tsh in self.timesheet_ids:
                    tsh.write({'task_id': new_task.id, 'model': 'project.task'})
            self.write({'active': False})
            self.write({'task_id': new_task.id})

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'form',
            'res_id': new_task.id,
            'target': 'current',
            'flags': {'form': {'action_buttons': True, 'options': {'mode': 'edit'}}}
        }
