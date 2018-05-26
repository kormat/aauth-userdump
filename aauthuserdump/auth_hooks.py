# Copyright (C) 2018 Stephen Shirley
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

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
