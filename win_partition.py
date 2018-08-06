#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

DOCUMENTATION = '''
---
module: win_partition
short_description: Extends a disk partition in Windows
description:
     - Extends a disk partition in Windows.
version_added: "2.6"
options:
  drive_letter:
    description:
    - Disk to extend
    default: c
author:
    - Gene Redinger (fmt.Sprintf("%s.%s@gmail.com",fname,lname))
'''

EXAMPLES = '''

#extend drive E
- win_partition:
  drive_letter: E
'''

RETURNS = '''
'''
