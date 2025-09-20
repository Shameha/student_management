from odoo import fields, models

class Student(models.Model):
    _name = "student.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    roll_no = fields.Char(string="Roll No")
    department = fields.Char(string="Department")

    course_ids = fields.Many2many(
        comodel_name="student.course",
        relation="student_course_rel",
        column1="student_id",
        column2="course_id",
        string="Enrolled Courses",
    )

    def action_show_enrolled_courses(self):
        self.ensure_one()
        return {
            "name": "Enrolled Courses",
            "type": "ir.actions.act_window",
            "res_model": "student.course",
            "view_mode": "list,form",  # Odoo 18
            "domain": [("id", "in", self.course_ids.ids)],
            "target": "current",
        }


class Course(models.Model):
    _name = "student.course"
    _description = "Course"

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Code", required=True)
    credit = fields.Float(string="Credit", default=0.0)

    student_ids = fields.Many2many(
        comodel_name="student.student",
        relation="student_course_rel",
        column1="course_id",
        column2="student_id",
        string="Students",
    )

    def action_view_students(self):
        self.ensure_one()
        return {
            "name": "Enrolled Students",
            "type": "ir.actions.act_window",
            "res_model": "student.student",
            "view_mode": "list,form",  # Odoo 18
            "domain": [("id", "in", self.student_ids.ids)],
            "target": "current",
        }

    # Print report safely (resolve XML ID at click time)
    def action_print_student_list(self):
        self.ensure_one()
        return self.env.ref("student_management.course_student_report_action").report_action(self)
