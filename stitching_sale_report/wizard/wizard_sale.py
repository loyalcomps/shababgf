from odoo import models, fields, api, _

class SalesStitchingReport(models.TransientModel):
    _name = 'sale.stitching.report'

    operating_unit = fields.Many2one('operating.unit', string='Operating Unit', required=True,
                                     default=lambda self: self.env.user.default_operating_unit_id)
    # company_id = fields.Many2one('res.company', required=True, string='Company', default=lambda self: self.env.company)
    start_date = fields.Date(string="Start Date", required=True,default=fields.Date.context_today)
    end_date = fields.Date(string="End Date", required=True,default=fields.Date.context_today)

    selection_user = fields.Selection([
        ('cutting_user', 'Cutting User'),
        ('stitching_user', 'Stitching User'), ], string='Select User')
    cutting_user = fields.Many2one('res.users', string="Cutting User")
    cutting_status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'),],string='Cutting Status')
    # cutting_completed = fields.Boolean('Cutting Completed', default=False)
    stitching_user = fields.Many2one('res.users', string="Stitching User")
    stitching_status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'), ], string='Stitching Status')
    # stitching_completed = fields.Boolean("Stitching Completed", default=False)

    @api.onchange('selection_user')
    def _onchange_selection_user(self):
        for i in self:
            if i.selection_user =='cutting_user':
                i.stitching_user=False
                i.stitching_status = False
            if i.selection_user == 'stitching_user':
                i.cutting_user = False
                i.cutting_status = False



    def print_report(self):
        project_id = self.env.context.get('active_id')
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'selection_user':self.selection_user,
                'cutting_user': self.cutting_user.id,
                'cutting_status': self.cutting_status,
                'stitching_user': self.stitching_user.id,
                'stitching_status': self.stitching_status,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'operating_unit':self.operating_unit.id
            },
        }
        return self.env.ref('stitching_sale_report.action_report_by_stitching').report_action(self, data=data)

