Custom RBAC Usage:
Command to run the application:

python main.py

An option driven menu will guide you through.

Assumptions:

- A super_admin role exists and any user who has that role is considered super_admin. Super admin has the privileges to
  create role, assign role and make a user superadmin.
- For the purpose of demo, any user driving the application can at any time log in as a new user.
- A user and a role are uniquely identified by their names. No 2 roles or users with same name cannot exist.

Improvements:

- More options can be provided in command lin interface menu.
- Better text formatting.



