#   Copyright 2018 Stephen Shirley
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import logging

from django.template.loader import render_to_string
from django.contrib.auth.models import User

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, ServicesHook
from .tasks import UserDumpTasks

logger = logging.getLogger(__name__)

class UserDump(ServicesHook):
    def __init__(self):
        super().__init__()
        self.name = "userdump"

@hooks.register('services_hook')
def register_service():
    return UserDump()
