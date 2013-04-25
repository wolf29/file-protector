#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file-protector.py
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
import json

import names
import utility
import dates

def directory_name(generator=random):
    '''
    Generates a random directory name, which is an alphanumeric string of
    length 1 to 32, selected from a bell curve
    '''
    return names.generate_name(32, generator)

def main():
    fish=[]
    cat=input("enter the number of files you have to hide: ")
    i = cat
    print i
    for i in range(0, (cat+1)):
        carp = directory_name(generator=random)
        fish.append(carp) 
        print carp
        print i
    print fish
    return 0

if __name__ == '__main__':
	main()

