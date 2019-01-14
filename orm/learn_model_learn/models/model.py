# -*- coding: utf-8 -*-

from odoo import models,fields

class ModelDoctor(models.Model):
    _name = "learn.doctor"
    _descripion = "Doctor entity"
    _sql_constraints = [
            ("uniq_fullname","UNIQUE (name)","Fullname must be unique"),
            ("denied_fullname","CHECK (name != 'AAA BBB')","Fakhri Brahem is not a teacher !")
                      ]
    
    name = fields.Char(string="Fullname", required=True, size=64, help="Doctor's fullname", default="Doctor Fullname")
    height = fields.Integer(string="height(cm)", default=None)
    description = fields.Text(string="Description", help="job description")
    signature = fields.Html(string="Signature")
    date_of_birth = fields.Date(string="Date of birthday")
    age = fields.Char(string="Age", readonly=True)
    datetime_of_registration = fields.Datetime(string="Date/Time d'enregistrement", default = lambda self : fields.datetime.now(), readonly=True)
    avatar = fields.Binary(string="Avatar")
    gender = fields.Selection([
        ("male","Male"),("female","Female")
        ], string="Gender")
    patient_ids = fields.One2many(comodel_name="learn.patient", inverse_name="doctor_id", string="Patients")
    hospital_id = fields.Many2many(comodel_name="learn.hospital", relation="doctor_hospitals_rel", column1="doctor_id", column2="hospital_id", string="Hospitals")
    
    
class ModelPatient(models.Model):
    _name = "learn.patient"
    _description = "Patient entity"
    
    name = fields.Char(string="Fullname", required=True, size=64, help="Patient's Fullname", default="Patient Fullname")
    date_of_birth = fields.Date(string="Date of birthday")
    gender = fields.Selection(
        [("male","Male"),("female","Female")], string="Gender")
    doctor_id = fields.Many2one(comodel_name="learn.doctor", string="Doctor")
    

class ModelHospital(models.Model):
    """ A doctor can work in multiple hospitals and a hospital can have multiple doctors"""
    _name = "learn.hospital"
    _description = "Hospital entity"
    
    name = fields.Char(string="Hospital name", required=True)
    date_of_creation = fields.Date(sting="Creation date")
    