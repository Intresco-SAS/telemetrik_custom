# -*- coding: utf-8 -*-
{
    'name': "Telemetrik",
    'summary': """Analytics Account Enhancement""",
    'description': """Analytics Account Enhancement""",
    'author': "Intresco SAS",
    'website': "https://www.intresco.co",
    'category': 'HR',
    'version': '14.0.0.1',
    'depends': ['analytic',
                'bi_hr_overtime_request_comm',
                'hr_timesheet',
                'bi_material_purchase_requisitions',],
    'data': [
        'views/views.xml',
        'views/purchase_order_custom.xml',
        'views/purchase_quotation_co.xml',
        'views/invoice_report_custom.xml',
        'views/material_purchase_requisition.xml',
    ],
}
