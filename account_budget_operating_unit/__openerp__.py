# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jordi Ballester (Eficent)
#    Copyright 2015 Eficent
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Budget with Operating Units',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'description': '''

Budget with Operating Units
===========================
This module introduces the following features:
- Adds the OU as a required field in the budget plan / budget line
- Security rules are defined to ensure that users can only display the
budget in which they are allowed access to.

''',
    'author': "Eficent",
    'website': 'http://www.eficent.com',
    'depends': ['account_budget', 'operating_unit'],
    'data': [
        'views/account_budget_view.xml',
        'security/account_budget_security.xml'
    ],
    'installable': True,
}
