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

from django.conf import settings

def main_char(user):
    return getattr(user.profile, 'main_character', None)

def char_name(char):
    return getattr(char, "character_name", "")

def char_id(char):
    return getattr(char, "character_id", "")

def user_groups(user):
    groups = [user.profile.state.name]
    for g in user.groups.all():
        groups.append(g.name)
    return groups

def output_path():
    return getattr(settings, "USERDUMP_PATH", '/tmp/userdump.json')
