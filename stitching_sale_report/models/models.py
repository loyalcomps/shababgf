# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
import datetime
from datetime import datetime


class ReportSalesstitching(models.AbstractModel):
    _name = 'report.stitching_sale_report.sale_stitching_report_view'


    def get_sale(self, data):

        lines = []

        start_date = data['form']['start_date']
        end_date = data['form']['end_date']
        cutting_user = data['form']['cutting_user']
        cutting_status = data['form']['cutting_status']
        stitching_user = data['form']['stitching_user']
        stitching_status = data['form']['stitching_status']
        operating_unit = data['form']['operating_unit']
        selection_user = data['form']['selection_user']

        sl = 0

        if not cutting_user and not stitching_user:

            query = '''
            
            select s.name as order,
			to_char(date_trunc('day',s.date_order),'YYYY-MM-DD') as date,
			s.cutting_user as cutting_user,
			s.cutting_completed as cutting_completed,
			s.stitching_user as stitching_user,
			s.stitching_completed as stitching_completed,
			rp.name as customer,
			s.amount_total as total
		from sale_order s 
			left join res_partner rp on s.partner_id = rp.id
		 WHERE  s.state in ('done','sale')
				and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
				AND s.operating_unit_id = %s


                                                              '''

            self.env.cr.execute(query, (
                start_date,end_date, operating_unit
            ))
            for row in self.env.cr.dictfetchall():
                sl += 1

                order = row['order'] if row['order'] else " "
                if row['date']:
                    date_object = datetime.strptime(str(row['date']), '%Y-%m-%d').date()
                    date = date_object.strftime('%d-%m-%Y')
                else:
                    date = ""


                if row['cutting_user']:
                    cutting_user = self.env['res.users'].browse(row['cutting_user']).name
                else:
                    cutting_user = ""

                if row['cutting_completed']:
                    if row['cutting_completed']==True:
                        cutting_completed = 'completed'
                    else:
                        cutting_completed = 'pending'

                else:
                    cutting_completed = ""


                if row['stitching_user']:
                    stitching_user = self.env['res.users'].browse(row['stitching_user']).name
                else:
                    stitching_user = ""

                if row['stitching_completed']:
                    if row['stitching_completed'] == True:
                        stitching_completed = 'completed'
                    else:
                        stitching_completed = 'pending'

                else:
                    stitching_completed = ""

                # date = row['date'] if row['date'] else " "
                # cutting_user = row['cutting_user'] if row['cutting_user'] else ""
                # cutting_completed = row['cutting_completed'] if row['cutting_completed'] else " "
                # stitching_user = row['stitching_user'] if row['stitching_user'] else ""
                # stitching_completed = row['stitching_completed'] if row['stitching_completed'] else ""
                customer = row['customer'] if row['customer'] else ""
                total = row['total'] if row['total'] else 0

                res = {
                    'sl_no': sl,
                    'order': order,
                    'date': date if date else "",
                    'cutting_user': cutting_user if cutting_user else "",
                    'cutting_completed': cutting_completed if cutting_completed else "",
                    'stitching_user': stitching_user if stitching_user else "",
                    'stitching_completed': stitching_completed if stitching_completed else "",
                    'customer': customer if customer else "",
                    'total': total if total else 0.0,

                }

                lines.append(res)
            if lines:
                return lines
            else:
                return []
        elif selection_user == 'cutting_user':
            if cutting_user and not cutting_status:

                query = '''

                            select s.name as order,
                			to_char(date_trunc('day',s.date_order),'YYYY-MM-DD') as date,
                			s.cutting_user as cutting_user,
                			s.cutting_completed as cutting_completed,
                			s.stitching_user as stitching_user,
                			s.stitching_completed as stitching_completed,
                			rp.name as customer,
                			s.amount_total as total
                		from sale_order s 
                			left join res_partner rp on s.partner_id = rp.id
                		 WHERE  s.state in ('done','sale')
                				and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
                				AND s.operating_unit_id = %s and s.cutting_user=%s


                                                                              '''

                self.env.cr.execute(query, (
                    start_date, end_date, operating_unit,cutting_user
                ))
                for row in self.env.cr.dictfetchall():
                    sl += 1

                    order = row['order'] if row['order'] else " "
                    if row['date']:
                        date_object = datetime.strptime(str(row['date']), '%Y-%m-%d').date()
                        date = date_object.strftime('%d-%m-%Y')
                    else:
                        date = ""

                    if row['cutting_user']:
                        cutting_user = self.env['res.users'].browse(row['cutting_user']).name
                    else:
                        cutting_user = ""

                    if row['cutting_completed']:
                        if row['cutting_completed'] == True:
                            cutting_completed = 'completed'
                        else:
                            cutting_completed = 'pending'

                    else:
                        cutting_completed = ""

                    if row['stitching_user']:
                        stitching_user = self.env['res.users'].browse(row['stitching_user']).name
                    else:
                        stitching_user = ""

                    if row['stitching_completed']:
                        if row['stitching_completed'] == True:
                            stitching_completed = 'completed'
                        else:
                            stitching_completed = 'pending'

                    else:
                        stitching_completed = ""

                    customer = row['customer'] if row['customer'] else ""
                    total = row['total'] if row['total'] else 0

                    res = {
                        'sl_no': sl,
                        'order': order,
                        'date': date if date else "",
                        'cutting_user': cutting_user if cutting_user else "",
                        'cutting_completed': cutting_completed if cutting_completed else "",
                        'stitching_user': stitching_user if stitching_user else "",
                        'stitching_completed': stitching_completed if stitching_completed else "",
                        'customer': customer if customer else "",
                        'total': total if total else 0.0,

                    }

                    lines.append(res)
                if lines:
                    return lines
                else:
                    return []
            elif cutting_user and cutting_status=='pending':

                query = '''

                            select s.name as order,
                			to_char(date_trunc('day',s.date_order),'YYYY-MM-DD') as date,
                			s.cutting_user as cutting_user,
                			s.cutting_completed as cutting_completed,
                			s.stitching_user as stitching_user,
                			s.stitching_completed as stitching_completed,
                			rp.name as customer,
                			s.amount_total as total
                		from sale_order s 
                			left join res_partner rp on s.partner_id = rp.id
                		 WHERE  s.state in ('done','sale')
                				and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
                				AND s.operating_unit_id = %s and s.cutting_user=%s and s.cutting_completed = false


                                                                              '''

                self.env.cr.execute(query, (
                    start_date, end_date, operating_unit,cutting_user
                ))
                for row in self.env.cr.dictfetchall():
                    sl += 1

                    order = row['order'] if row['order'] else " "
                    if row['date']:
                        date_object = datetime.strptime(str(row['date']), '%Y-%m-%d').date()
                        date = date_object.strftime('%d-%m-%Y')
                    else:
                        date = ""

                    if row['cutting_user']:
                        cutting_user = self.env['res.users'].browse(row['cutting_user']).name
                    else:
                        cutting_user = ""

                    if row['cutting_completed']:
                        if row['cutting_completed'] == True:
                            cutting_completed = 'completed'
                        else:
                            cutting_completed = 'pending'

                    else:
                        cutting_completed = ""

                    if row['stitching_user']:
                        stitching_user = self.env['res.users'].browse(row['stitching_user']).name
                    else:
                        stitching_user = ""

                    if row['stitching_completed']:
                        if row['stitching_completed'] == True:
                            stitching_completed = 'completed'
                        else:
                            stitching_completed = 'pending'

                    else:
                        stitching_completed = ""

                    customer = row['customer'] if row['customer'] else ""
                    total = row['total'] if row['total'] else 0

                    res = {
                        'sl_no': sl,
                        'order': order,
                        'date': date if date else "",
                        'cutting_user': cutting_user if cutting_user else "",
                        'cutting_completed': cutting_completed if cutting_completed else "",
                        'stitching_user': stitching_user if stitching_user else "",
                        'stitching_completed': stitching_completed if stitching_completed else "",
                        'customer': customer if customer else "",
                        'total': total if total else 0.0,

                    }

                    lines.append(res)
                if lines:
                    return lines
                else:
                    return []
            elif cutting_user and cutting_status=='completed':

                query = '''

                            select s.name as order,
                			to_char(date_trunc('day',s.date_order),'YYYY-MM-DD') as date,
                			s.cutting_user as cutting_user,
                			s.cutting_completed as cutting_completed,
                			s.stitching_user as stitching_user,
                			s.stitching_completed as stitching_completed,
                			rp.name as customer,
                			s.amount_total as total
                		from sale_order s 
                			left join res_partner rp on s.partner_id = rp.id
                		 WHERE  s.state in ('done','sale')
                				and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
                				AND s.operating_unit_id = %s and s.cutting_user=%s and s.cutting_completed = true


                                                                              '''

                self.env.cr.execute(query, (
                    start_date, end_date, operating_unit,cutting_user
                ))
                for row in self.env.cr.dictfetchall():
                    sl += 1

                    order = row['order'] if row['order'] else " "
                    if row['date']:
                        date_object = datetime.strptime(str(row['date']), '%Y-%m-%d').date()
                        date = date_object.strftime('%d-%m-%Y')
                    else:
                        date = ""

                    if row['cutting_user']:
                        cutting_user = self.env['res.users'].browse(row['cutting_user']).name
                    else:
                        cutting_user = ""

                    if row['cutting_completed']:
                        if row['cutting_completed'] == True:
                            cutting_completed = 'completed'
                        else:
                            cutting_completed = 'pending'

                    else:
                        cutting_completed = ""

                    if row['stitching_user']:
                        stitching_user = self.env['res.users'].browse(row['stitching_user']).name
                    else:
                        stitching_user = ""

                    if row['stitching_completed']:
                        if row['stitching_completed'] == True:
                            stitching_completed = 'completed'
                        else:
                            stitching_completed = 'pending'

                    else:
                        stitching_completed = ""

                    customer = row['customer'] if row['customer'] else ""
                    total = row['total'] if row['total'] else 0

                    res = {
                        'sl_no': sl,
                        'order': order,
                        'date': date if date else "",
                        'cutting_user': cutting_user if cutting_user else "",
                        'cutting_completed': cutting_completed if cutting_completed else "",
                        'stitching_user': stitching_user if stitching_user else "",
                        'stitching_completed': stitching_completed if stitching_completed else "",
                        'customer': customer if customer else "",
                        'total': total if total else 0.0,

                    }

                    lines.append(res)
                if lines:
                    return lines
                else:
                    return []
        elif selection_user == 'stitching_user':
            if stitching_user and not stitching_status:

                query = '''

                            select s.name as order,
                			to_char(date_trunc('day',s.date_order),'YYYY-MM-DD') as date,
                			s.cutting_user as cutting_user,
                			s.cutting_completed as cutting_completed,
                			s.stitching_user as stitching_user,
                			s.stitching_completed as stitching_completed,
                			rp.name as customer,
                			s.amount_total as total
                		from sale_order s 
                			left join res_partner rp on s.partner_id = rp.id
                		 WHERE  s.state in ('done','sale')
                				and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
                				AND s.operating_unit_id = %s and s.stitching_user=%s


                                                                              '''

                self.env.cr.execute(query, (
                    start_date, end_date, operating_unit,stitching_user
                ))
                for row in self.env.cr.dictfetchall():
                    sl += 1

                    order = row['order'] if row['order'] else " "
                    if row['date']:
                        date_object = datetime.strptime(str(row['date']), '%Y-%m-%d').date()
                        date = date_object.strftime('%d-%m-%Y')
                    else:
                        date = ""

                    if row['cutting_user']:
                        cutting_user = self.env['res.users'].browse(row['cutting_user']).name
                    else:
                        cutting_user = ""

                    if row['cutting_completed']:
                        if row['cutting_completed'] == True:
                            cutting_completed = 'completed'
                        else:
                            cutting_completed = 'pending'

                    else:
                        cutting_completed = ""

                    if row['stitching_user']:
                        stitching_user = self.env['res.users'].browse(row['stitching_user']).name
                    else:
                        stitching_user = ""

                    if row['stitching_completed']:
                        if row['stitching_completed'] == True:
                            stitching_completed = 'completed'
                        else:
                            stitching_completed = 'pending'

                    else:
                        stitching_completed = ""

                    customer = row['customer'] if row['customer'] else ""
                    total = row['total'] if row['total'] else 0

                    res = {
                        'sl_no': sl,
                        'order': order,
                        'date': date if date else "",
                        'cutting_user': cutting_user if cutting_user else "",
                        'cutting_completed': cutting_completed if cutting_completed else "",
                        'stitching_user': stitching_user if stitching_user else "",
                        'stitching_completed': stitching_completed if stitching_completed else "",
                        'customer': customer if customer else "",
                        'total': total if total else 0.0,

                    }

                    lines.append(res)
                if lines:
                    return lines
                else:
                    return []
            elif stitching_user and stitching_status=='pending':

                query = '''

                            select s.name as order,
                			to_char(date_trunc('day',s.date_order),'YYYY-MM-DD') as date,
                			s.cutting_user as cutting_user,
                			s.cutting_completed as cutting_completed,
                			s.stitching_user as stitching_user,
                			s.stitching_completed as stitching_completed,
                			rp.name as customer,
                			s.amount_total as total
                		from sale_order s 
                			left join res_partner rp on s.partner_id = rp.id
                		 WHERE  s.state in ('done','sale')
                				and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
                				AND s.operating_unit_id = %s and s.stitching_user=%s and s.stitching_completed = false


                                                                              '''

                self.env.cr.execute(query, (
                    start_date, end_date, operating_unit,stitching_user
                ))
                for row in self.env.cr.dictfetchall():
                    sl += 1

                    order = row['order'] if row['order'] else " "
                    if row['date']:
                        date_object = datetime.strptime(str(row['date']), '%Y-%m-%d').date()
                        date = date_object.strftime('%d-%m-%Y')
                    else:
                        date = ""

                    if row['cutting_user']:
                        cutting_user = self.env['res.users'].browse(row['cutting_user']).name
                    else:
                        cutting_user = ""

                    if row['cutting_completed']:
                        if row['cutting_completed'] == True:
                            cutting_completed = 'completed'
                        else:
                            cutting_completed = 'pending'

                    else:
                        cutting_completed = ""

                    if row['stitching_user']:
                        stitching_user = self.env['res.users'].browse(row['stitching_user']).name
                    else:
                        stitching_user = ""

                    if row['stitching_completed']:
                        if row['stitching_completed'] == True:
                            stitching_completed = 'completed'
                        else:
                            stitching_completed = 'pending'

                    else:
                        stitching_completed = ""

                    customer = row['customer'] if row['customer'] else ""
                    total = row['total'] if row['total'] else 0

                    res = {
                        'sl_no': sl,
                        'order': order,
                        'date': date if date else "",
                        'cutting_user': cutting_user if cutting_user else "",
                        'cutting_completed': cutting_completed if cutting_completed else "",
                        'stitching_user': stitching_user if stitching_user else "",
                        'stitching_completed': stitching_completed if stitching_completed else "",
                        'customer': customer if customer else "",
                        'total': total if total else 0.0,

                    }

                    lines.append(res)
                if lines:
                    return lines
                else:
                    return []
            elif stitching_user and stitching_status=='completed':

                query = '''

                            select s.name as order,
                			to_char(date_trunc('day',s.date_order),'YYYY-MM-DD') as date,
                			s.cutting_user as cutting_user,
                			s.cutting_completed as cutting_completed,
                			s.stitching_user as stitching_user,
                			s.stitching_completed as stitching_completed,
                			rp.name as customer,
                			s.amount_total as total
                		from sale_order s 
                			left join res_partner rp on s.partner_id = rp.id
                		 WHERE  s.state in ('done','sale')
                				and  to_char(date_trunc('day',s.date_order),'YYYY-MM-DD')::date between %s and %s
                				AND s.operating_unit_id = %s and s.stitching_user=%s and s.stitching_completed = true


                                                                              '''

                self.env.cr.execute(query, (
                    start_date, end_date, operating_unit,stitching_user
                ))
                for row in self.env.cr.dictfetchall():
                    sl += 1

                    order = row['order'] if row['order'] else " "
                    if row['date']:
                        date_object = datetime.strptime(str(row['date']), '%Y-%m-%d').date()
                        date = date_object.strftime('%d-%m-%Y')
                    else:
                        date = ""

                    if row['cutting_user']:
                        cutting_user = self.env['res.users'].browse(row['cutting_user']).name
                    else:
                        cutting_user = ""

                    if row['cutting_completed']:
                        if row['cutting_completed'] == True:
                            cutting_completed = 'completed'
                        else:
                            cutting_completed = 'pending'

                    else:
                        cutting_completed = ""

                    if row['stitching_user']:
                        stitching_user = self.env['res.users'].browse(row['stitching_user']).name
                    else:
                        stitching_user = ""

                    if row['stitching_completed']:
                        if row['stitching_completed'] == True:
                            stitching_completed = 'completed'
                        else:
                            stitching_completed = 'pending'

                    else:
                        stitching_completed = ""

                    customer = row['customer'] if row['customer'] else ""
                    total = row['total'] if row['total'] else 0

                    res = {
                        'sl_no': sl,
                        'order': order,
                        'date': date if date else "",
                        'cutting_user': cutting_user if cutting_user else "",
                        'cutting_completed': cutting_completed if cutting_completed else "",
                        'stitching_user': stitching_user if stitching_user else "",
                        'stitching_completed': stitching_completed if stitching_completed else "",
                        'customer': customer if customer else "",
                        'total': total if total else 0.0,

                    }

                    lines.append(res)
                if lines:
                    return lines
                else:
                    return []




    def _get_report_values(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))

        start_date = data['form']['start_date']
        end_date = data['form']['end_date']
        cutting_user = data['form']['cutting_user']
        cutting_status = data['form']['cutting_status']
        stitching_user = data['form']['stitching_user']
        stitching_status = data['form']['stitching_status']
        operating_unit = data['form']['operating_unit']
        selection_user = data['form']['selection_user']

        operating_unit_name = self.env['operating.unit'].browse(operating_unit).name


        get_sale = self.get_sale(data)

        date_object_startdate = datetime.strptime(start_date, '%Y-%m-%d').date()
        date_object_enddate = datetime.strptime(end_date, '%Y-%m-%d').date()

        if cutting_user:
            cutting_user = self.env['res.users'].browse(cutting_user).name
        else:
            cutting_user = ""

        if stitching_user:
            stitching_user = self.env['res.users'].browse(stitching_user).name
        else:
            stitching_user = ""

        docargs = {
            'doc_ids': docids,
            'doc_model': model,
            'data': data['form'],
            'date_start': date_object_startdate.strftime('%d-%m-%Y'),
            'date_end': date_object_enddate.strftime('%d-%m-%Y'),
            'docs': docs,
            'get_sale': get_sale,
            'cutting_user':cutting_user,
            'stitching_user':stitching_user,
            'operating_unit':operating_unit_name,
            'selection_user':selection_user

        }
        return docargs

