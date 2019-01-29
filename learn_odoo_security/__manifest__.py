# -*- coding: utf-8 -*-

{
    'name':"security training",
    'description':"""
    This is a module for learning security in Odoo:
    - Groups
    - ACL
    - rules
    etc . . .
    """,
    'summary':"security in Odoo ..",
    'author' : "p4k!s",
    'sequence': 6,
    'depends' : ['base'],
    'data' : [
        "security/learnOdooSecurity_security.xml",
        "security/ir.model.access.csv",
        "views/student_view.xml",
        ],
    'installable':True,
}