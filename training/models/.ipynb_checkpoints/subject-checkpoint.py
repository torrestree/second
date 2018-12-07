from odoo import api, fields, models

class Subject(models.Model):
    _name='training.subject'
    _description='科目'
    
    name=fields.Char(string='名称')
    persion_id=fields.Many2one('res.partner',string='负责人')
    lesson_ids=fields.One2many('training.lesson','subject_id','课程')
    description=fields.Text(string='备注')