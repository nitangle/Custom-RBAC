from models.Role import Role


class Rbac:
    SUPER_ADMIN_ROLE = Role("super_admin")

    def __init__(self, roles, users, resources):
        self.__roles = roles
        self.__users = users
        self.__resources = resources

    def get_roles(self):
        return self.__roles

    def get_users(self):
        return self.__users

    def get_resources(self):
        return self.__resources

    def add_role(self, role):
        if role.name in self.__roles:
            print('Role with the given name already exists!. Please choose another name')
        else:
            self.__roles.append(role)

    def add_user(self, user):
        if user.name in self.__users:
            print('USer with given name already exists! Please choose another name')
        else:
            self.__users.append(user)

    def create_role(self, role_name, permissions={}):
        return Role(role_name, permissions)

    def assign_role_to_user(self, user, role):
        return user.assign_role_to_user(role)

    def check_user_has_resource_access(self, user, resource, action_type):
        if self.is_user_super_admin(user):
            return True
        user_roles = user.roles
        resource_name = resource.name
        for role in user_roles:
            if action_type in role.get(resource_name):
                return True
        return False

    def remove_role_from_user(self, user, role):
        return user.remove_role(role)

    def make_super_admin(self, user):
        return user.add_role(self.SUPER_ADMIN_ROLE)

    def is_user_super_admin(self, user):
        return user.is_role_assigned_to_user(self.SUPER_ADMIN_ROLE)
