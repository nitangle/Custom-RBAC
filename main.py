from models import ACTION_TYPE, User, Resource, Role, CmdInterface, Rbac

if __name__ == '__main__':
    print("welcome to rbac system demo")
    print('Creating some default resources, roles and users')

    print('------ Creating resources -------')
    file_resource = Resource('file_resource')
    device_resource = Resource('device_resource')
    resources = [file_resource, device_resource]

    print('------ Creating roles -------')
    files_admin = Role('files_admin',
                       {file_resource.name: [ACTION_TYPE.READ, ACTION_TYPE.WRITE, ACTION_TYPE.DELETE]})
    guest = Role('guest',
                 {device_resource.name: [ACTION_TYPE.READ], file_resource.name: [ACTION_TYPE.READ]})
    devices_admin = Role('devices_admin',
                         {device_resource.name: [ACTION_TYPE.READ, ACTION_TYPE.WRITE, ACTION_TYPE.DELETE]})
    roles = [files_admin, devices_admin, guest]

    print('------ Creating users -------')
    users = []
    john = User('john', [files_admin])
    users.append(john)
    sara = User('sara', [devices_admin])
    users.append(sara)
    guest_user = User('guest', [guest])
    users.append(guest_user)

    print('------ Creating RBAC system -------')
    # Rbac system Initialised
    rbac = Rbac(roles, users, resources)

    print('------ Creating super admin -------')
    root = User('root')
    rbac.make_super_admin(root)
    cmd_interface = CmdInterface(rbac, root)
    cmd_interface.get_interactive_menu()
