# Copyright 2016 Akretion (http://www.akretion.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# @author Alexis de Lattre <alexis.delattre@akretion.com>

{
    'name': 'Base UNECE',
    'version': '11.0.1.0.1',
    'category': 'Tools',
    'license': 'AGPL-3',
    'summary': 'Base module for UNECE code lists',
    'author': 'Akretion,Odoo Community Association (OCA)',
    "website": "https://github.com/OCA/community-data-files",
    'depends': ['base'],
    'data': [
        'views/unece_code_list.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
}
