# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Harbour Q3 2017 Phase 3 Customization',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Added window actions/tree views for sales.
        """,
    'depends': ['base_import','sale'],
    'data': [
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window_menu.xml',
    ],
    'installable': True,
}
