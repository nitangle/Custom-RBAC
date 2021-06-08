class Role():

    def __init__(self, name, resource_permissions_map={}):
        self.__name = name
        self.__resource_permissions_map = resource_permissions_map

    @property
    def name(self):
        return self.__name

    def get_resource_permissions(self):
        return self.__resource_permissions_map

    def add_resource_permissions(self, resource_permissions_map):
        for resource_name in resource_permissions_map:
            for action_type in resource_permissions_map[resource_name]:
                if action_type in self.__resource_permissions_map.get(resource_name):
                    print("Given permissions for resource {} already exist!".format(resource_name))
                else:
                    self.__resource_permissions_map.get(resource_name).push(action_type)

    def remove_resource_permissions(self, resource_permissions_map):
        for resource_name in resource_permissions_map:
            for action_type in resource_permissions_map[resource_name]:
                if action_type not in self.__resource_permissions_map.get(resource_name):
                    print("Given permissions for resource {} does not exist!".format(resource_name))
                else:
                    self.__resource_permissions_map.get(resource_name).remove(action_type)

    def __repr__(self):
        return f'{self.name} has permissions - {self.__resource_permissions_map}'
