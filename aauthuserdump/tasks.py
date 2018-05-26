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

import json
import logging

from django.contrib.auth.models import User
from celery import shared_task

from .utils import main_char, char_name, char_id, user_groups, output_path

logger = logging.getLogger(__name__)

class UserDumpTasks:
    def __init__(self):
        pass

    @staticmethod
    @shared_task(name='aauthuserdump.update_all_users')
    def update_all_users():
        logger.debug("Exporting all users")
        d = {}
        for u in User.objects.all():
            c = main_char(u)
            if c is None:
                logger.debug("User %s has no main char, skipping", u)
                continue
            cid = char_id(c)
            if not cid:
                logger.error("User %s's main char (%s) has no char id, skipping", u, c)
                continue
            groups = user_groups(u)
            logger.debug("Export: user %s char: %s(%s) groups: %s", u, char_name(c), cid, groups)
            d[cid] = groups
        path = output_path()
        with open(path, "w") as f:
            json.dump(d, f, sort_keys=True, indent=4, separators=(',', ': '))
        logger.info("Export written to %s", path)
