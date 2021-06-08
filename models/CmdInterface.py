from main import ACTION_TYPE


class CmdInterface:
    def __init__(self, rbac_system, super_admin):
        self.__rbac_system = rbac_system
        self.__logged_in_as = super_admin
        self.__root = super_admin

    def __is_super_admin(self):
        return self.__rbac_system.is_user_super_admin(self.__logged_in_as)

    def get_interactive_menu(self):
        while True:
            print("######--------Menu--------######")
            print("######--------Logged in as root-------######")
            print("Press 1 for select user")
            print("Press 2 to check access type of a resource")
            if self.__is_super_admin():
                print("Press 3 to create a role")
            if self.__is_super_admin():
                print('Press 4 to assign role to user')
            if self.__is_super_admin():
                print('Press 5 to make user super admin')
            print("press 0 to exit")
            choice = int(input())
            print(f'-----------------choice is {choice}')
            if choice is 0:
                break
            elif choice is 1:
                self.__select_logged_in_user()
            elif choice is 2:
                self.__check_user_has_resource_access()
            elif self.__is_super_admin() and choice is 3:
                self.__create_role()
            elif self.__is_super_admin() and choice is 4:
                self.__assign_role()

            elif self.__is_super_admin() and choice is 5:
                self.__make_super_admin()
            else:
                print('Please enter valid choice!!')
                print('---------------------------')
                continue

    def __select_user(self):
        print('Select user from the given list. Enter the index of the user from list')
        users = self.__rbac_system.get_users()
        for user, index in zip(users, range(len(users))):
            print(f'{index}: {user}')
        while True:
            try:
                choice = int(input())
                if not isinstance(choice, int) or choice >= len(users):
                    raise ValueError('Invalid Choice! Please try again')
                return users[choice]
            except Exception as err:
                print(f'{err}')

    def __select_logged_in_user(self):
        self.__logged_in_as = self.__select_user()

    def __check_user_has_resource_access(self):
        print('Please select resource from the list. Type its index')
        resources = self.__rbac_system.get_resources()
        for resource, index in zip(resources, range(len(resources))):
            print('{}: {}'.format(index, resource))
        while True:
            try:
                choice = int(input())
                if not isinstance(choice, int) or choice >= len(resources):
                    raise ValueError('Invalid Choice! Please try again')
                resource = resources[choice]
                break
            except Exception:
                pass

        print('Type 0 for READ access,1 for WRITE access and 2 to check DELETE access')
        while True:
            try:
                choice = int(input())
                actions = [ACTION_TYPE.READ, ACTION_TYPE.WRITE, ACTION_TYPE.DELETE]
                if not isinstance(choice, int) or choice not in [0, 1, 2]:
                    raise ValueError('Invalid Choice! Please try again')
                access_type = actions[choice]
                break
            except Exception as err:
                print(err)
        print(f'resource={resource},access_type={access_type} and user={self.__logged_in_as}')
        if self.__rbac_system.check_user_has_resource_access(self.__logged_in_as, resource, access_type):
            print(f'You have {access_type} access to {resource}.')
        else:
            print(f'You do not have {access_type} access to resource')

    def __create_role(self):
        print('Please output name of role.')
        name = input()
        print('Please type 0 to grant read access to displayed resource, 1 for write access, 2 for delete access and '
              'any other choice or skip for no permission for that resource')
        print('Type values separated by comma if more than 1 access has to be granted.')
        permissions = dict()
        for resource in self.__rbac_system.get_resources():
            print(f'{resource}')
            try:
                choice = list(set(map(int, input().split(','))))
                permissions[resource.name] = choice
            except Exception:
                continue
        role = self.__rbac_system.create_role(name, permissions)
        self.__rbac_system.add_role(role)
        print(f'{role} created successfully!')

    def __select_role(self):
        print('Select role from the given list. Enter the index of the role from list')
        roles = self.__rbac_system.get_roles()
        for user, index in zip(roles, range(len(roles))):
            print(f'{index}: {user}')
        while True:
            try:
                choice = int(input())
                return roles[choice]
            except Exception:
                raise ValueError('Invalid Choice! Please try again')

    def __assign_role(self):
        role = self.__select_role()
        if self.__rbac_system.assign_role_to_user(self.__logged_in_as, role):
            print('Role assigned successfully')

    def __get_roles(self):
        for role in self.__rbac_system.get_roles():
            print(role)

    def __get_users(self):
        users = self.__rbac_system.get_users()
        for index, user in zip(range(len(users)), users):
            print(f'{index}: {user}')

    def __make_super_admin(self):
        print('Select user from the list. Type the index of the user.')
        users = self.__rbac_system.get_users()
        self.__get_users()
        try:
            choice = int(input())
            if not isinstance(choice, int) and choice not in len(users):
                raise ValueError('Invalid choice given')
            user = users[choice]
            result = self.__rbac_system.make_super_admin(user)
            if result is False:
                raise Exception('Could not make user super admin')
            print(f'User {user} successfully made super admin')
        except Exception as err:
            print(err)
