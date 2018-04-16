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
        logger.debug("aauthuserdump.update_all_users running")
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
            logger.debug("user %s char: %s(%s) groups: %s", u, char_name(c), cid, groups)
            d[cid] = groups
        path = output_path()
        with open(path, "w") as f:
            json.dump(d, f, sort_keys=True, indent=4, separators=(',', ': '))
        logger.info("aauthuserdump.update_all_users wrote %s", path)
