# coding : utf-8

from odoo import models,fields

class SecStudent(models.Model):
    _name = "learn_sec.student"
    _descripion = "Student entity"
    
    name = fields.Char(string="Name", default="Fakhri")
    age = fields.Integer(string="Age", size=2)
