from django.template.loader import render_to_string

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, ServicesHook
#from .urls import urlpatterns

class UserDump(ServicesHook):
    def __init__(self):
        super().__init__()
        self.name = "UserDump"

#@hooks.register('services_hook')
#def register_service():
#    return UserDump()

@hooks.register('menu_item_hook')
def register_menu():
        return MenuItemHook('Example Item', 'glyphicon glyphicon-heart',
                            'example_url_name', 150)
