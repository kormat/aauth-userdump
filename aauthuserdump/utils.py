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
