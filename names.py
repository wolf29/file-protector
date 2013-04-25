#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  names.py
#  
#  Copyright 2013 Wolf Halton  <wolf@sourcefreedom.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import random
import string
import utility


char_set = string.letters + string.digits

def generate_name(length, generator=random):
    '''
    generates a random alphanumeric string with length 1 to length, along a
    bell curve
    '''
    length = utility.random_int_bell_curve(1, length, generator=generator)
    return string.join(utility.sample_wr(char_set, length, generator=generator), '')
    

