class User:

    def __init__(self, name, roles=[]):
        self.__name = name
        self.__roles = roles

    @property
    def name(self):
        return self.__name

    @property
    def roles(self):
        return self.__roles

    def is_role_assigned_to_user(self, role):
        if role.name in [role.name for role in self.__roles]:
            return True
        return False

    def add_role(self, role):
        if self.is_role_assigned_to_user(role):
            print("User already has the specified role!. Please assign a new role to user.")
            return False

        else:
            self.__roles.append(role)
            return True

    def remove_role(self, role):
        if role not in self.__roles:
            print("User does not have the specified role!")
            return False
        else:
            role.remove(role)
            return True

    def __repr__(self):
        return self.__name
