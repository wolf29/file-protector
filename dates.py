#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dates.py
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


import datetime
import random

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def random_datetime(generator=random):
    date_dict = {}

    year = generator.randint(2000, 2010)
    month = generator.randint(1, 12)
    day = generator.randint(1, days_per_month[month - 1])
    hour = generator.randint(0, 23)
    minute = generator.randint(0, 59)
    second = generator.randint(0, 59)

    return datetime.datetime(year, month, day, hour, minute, second)

def make_created_modified(chance_of_same=.5, generator=random):
    '''
    Returns 2 date/time dicts. There is a chance_of_same% chance they will be the same;
    otherwise, the first date will always be before the second
    '''
    if generator.random() >= chance_of_same:
        date1 = random_datetime(generator)
        date2 = random_datetime(generator)

        if date1 > date2:
            date1, date2 = date2, date1
    else:
        date1 = date2 = random_datetime(generator)

    return date1, date2
