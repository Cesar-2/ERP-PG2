""" It handle the addition of profiles to an user """

from django.shortcuts import get_object_or_404
from ..models.enterprise.module import Module


class EnterpriseModules:
    def __init__(self, enterprise, modules=None):
        """ Initializes class with an enterprise and an optional list of pk modules.

        Parameters:
            enterprise (Enterprise):enterprise model instance.
            modules (List):Primary keys list about modules instances.

        """

        self.enterprise = enterprise
        self.modules = modules if modules else None

    def add_module(self, module):
        """ Add the module to an enterprise.

        Returns:
            enterprise (Enterprise):enterprise instance with module within its ManyToMany
                        relation.

        """
        # pylint: disable=no-member
        enterprise_module = Module.objects.get_or_create(names=module)
        self.enterprise.module.add(enterprise_module[0])
        return self.enterprise
