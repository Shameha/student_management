student_management
Odoo 18 module for managing students and courses with a many-to-many enrollment.

Install and run

Create a custom_addons folder inside the Odoo 18 server folder and put student_management inside it.

Edit odoo.conf and set:
addons_path = E:/Odoo 18/server/custom_addons,E:/Odoo 18/server/odoo/addons
Confirm your Python path and DB settings (db_host, db_port, db_user, db_password) are correct.

First install from terminal:
"E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf" -d odoo18 -i student_management --stop-after-init

Start server:
"E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf"

Test

Open http://localhost:8069

Menu: Student Management → Courses → create a few

Menu: Student Management → Students → create and enroll using the Enrolled Courses field

Use the buttons on forms to view related records and print the course-wise student list

Notes from setup

In Odoo 18 use <list> and view_mode="list,form"

Form header buttons should be type="object" and call Python methods

Define window actions before menuitems in the same XML file

Keep XML IDs consistent (e.g., student_management.action_student_students)

Root app menu should have an action so the tile opens Students directly

Common problems I faced (and quick fixes)

PostgreSQL user/password: create a DB user with CREATEDB, set db_user/db_password in odoo.conf, ensure the service is running and the port is correct.

Interpreter (PyCharm): use the Odoo bundle interpreter (e.g., E:/Odoo 18/python/python.exe) to avoid import/runtime mismatches.

Hosting/port: if 8069 is busy, change the XML-RPC port; for LAN access, allow the app through Windows firewall.

Redirects back to Apps: add an action to the root menu (Student Management → action_student_students).

Invalid view type 'tree': replace legacy <tree> with <list> and use view_mode="list,form".

External ID not found: make sure the action exists, is spelled correctly, and is defined before the menu that references it; include the XML in manifest.py.
