# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Convert(models.Model):
    _inherit = 'project.task'

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
        vals['task_id'] = self.id
        vals['kanban_state'] = self.kanban_state
        vals['name'] = self.name
        vals['stage_id'] = self.stage_id.id
        vals['date_deadline'] = self.date_deadline

        new_issue = self.env['project.issue'].create(vals)
        if new_issue:
            for msg in self.message_ids:
                msg.write({'res_id' : new_issue.id, 'model' : 'project.issue'})
            if self.timesheet_ids:
                for tsh in self.timesheet_ids:
                    tsh.write({'issue_id' : new_issue.id, 'model' : 'project.issue'})
            self.write({'active': False})
            self.write({'issue_id': new_issue.id})
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            self.message_post(
                body="This task has been converted into issue: " '%s/#id=%s&amp;view_type=form&amp;model=project.issue' % (
                base_url, new_issue.id))

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.issue',
            'view_mode': 'form',
            'res_id': new_issue.id,
            'target': 'current',
            'flags': {'form': {'action_buttons': True, 'options': {'mode': 'edit'}}}
        }
