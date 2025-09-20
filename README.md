# student_management
Odoo 18 module for managing students and courses with a many-to-many enrollment.

---

## Install and run

-Create a custom_addons folder inside the Odoo 18 server folder and put student_management inside it.
-Edit odoo.conf and set:
addons_path = E:/Odoo 18/server/custom_addons,E:/Odoo 18/server/odoo/addons
Also confirm your DB settings (db_host, db_port, db_user, db_password) and Python path are correct.
-First install from terminal:
"E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf" -d odoo18 -i student_management --stop-after-init"
-Start the server:
"E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf"






---

## Test
- Open **http://localhost:8069**
- Menu: **Student Management → Courses** → create a few
- Menu: **Student Management → Students** → create and enroll using **Enrolled Courses**
- Use the form buttons:
- Student → **Show Enrolled Courses**
- Course → **View Students**, **Print Student List** (PDF)

---

## Notes from setup
- In Odoo 18 use **`<list>`** and **`view_mode="list,form"`** (not `<tree>` / `tree,form`).
- Form header buttons should be **`type="object"`** and call Python methods.
- Define window actions **before** menuitems in the same XML file.
- Keep XML IDs consistent (e.g., `student_management.action_student_students`).
- The **root app menu** should have an action so the tile opens **Students** directly.

---

## Problems & quick fixes
- **PostgreSQL user/password**  
Create role & DB and match `odoo.conf`:
