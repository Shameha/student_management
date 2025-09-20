#student_management
Odoo 18 module for managing students and courses with a many-to-many enrollment.

#Install and run
1.Create a custom_addons folder inside the Odoo 18 server folder and put student_management inside it.
2.Edit odoo.conf and set:
addons_path = E:/Odoo 18/server/custom_addons,E:/Odoo 18/server/odoo/addons
Also confirm your DB settings (db_host, db_port, db_user, db_password) and Python path are correct.
3.First install from terminal:
"E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf" -d odoo18 -i student_management --stop-after-init"
4.Start the server:
"E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf"

#Test
1.Open http://localhost:8069
2.Menu: Student Management → Courses → create a few courses
3.Menu: Student Management → Students → create students and enroll using Enrolled Courses
4.Use form buttons to navigate and print:
Student → Show Enrolled Courses
Course → View Students, Print Student List (PDF)
