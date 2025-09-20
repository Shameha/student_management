# student_management
Odoo 18 module for managing students and courses with a many-to-many enrollment.

---


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
