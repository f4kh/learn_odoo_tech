# -*- coding: utf-8 -*-

{
    'name':"Learn about models",
    'description':"""
    This is a module for learning purpose:
    - Fields
    - Decorators
    - ORM methods
    etc . . .
    """,
    'summary':"ORM/Model fields ..",
    'author' : "p4k!s",
    'sequence': 2,
    'depends' : ['base'],
    'data' : [
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/hospital_view.xml',
        'views/spectrum_menu.xml',
        'data/hospital_data.xml',
        'data/doctor_data.xml',
        'data/patient_data.xml',
        ],
    'installable':True,
}