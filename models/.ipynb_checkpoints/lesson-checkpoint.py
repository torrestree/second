from odoo import api, fields, models

class Lesson(models.Model):
    _name='training.lesson'
    _description='课程'
    
    name=fields.Char(string='名称')
    subject_id=fields.Many2one('training.subject')
    teacher_id=fields.Many2one('res.partner',string='教师',domain=[('is_teacher','=',True)])
    student_ids=fields.Many2many('res.partner',string='学生',domain=[('is_student','=',True)])
    startdate=fields.Date(string='开始日期')
    enddate=fields.Date(string='结束日期')
    qty_seat=fields.Integer(string='座位数')
    description=fields.Text(string="备注")