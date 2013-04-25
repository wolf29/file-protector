#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utility.py
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
import time
import itertools
import string
from math import floor, ceil

import json

def random_int_bell_curve(min, max, lean=.5, narrow=10, generator=random):
    '''
    Generate a random int on a beta distribution, with a mean of lean, scaled
    to min and max. The parameters are tuned such that alpha=lean*narrow,
    beta=(1-lean)*narrow. Therefore, the larger narrow is, the narrower the
    graph will be.
    '''

    if min == max:
        return min

    if min > max:
        raise ValueError("Invalid min-max range for random int generation")

    if not 0 <= lean <= 1:
        raise ValueError("lean must be between 0 and 1")

    alpha = lean * narrow
    beta = (1 - lean) * narrow

    return int(generator.betavariate(alpha, beta) * (max - min) + min)

def print_histogram(items, scale, clamp_left=None, clamp_right=None):
    '''
    Takes a list of integers, and prints a histogram of that list, where each
    int is a separate bucket.
    '''
    counts = {}
    def count(x):
        if x in counts:
            counts[x] += scale
        else:
            counts[x] = scale

    map(count, items)

    if clamp_left is None:
        clamp_left = min(counts.iterkeys())

    if clamp_right is None:
        clamp_right = max(counts.iterkeys())

    for bucket in xrange(clamp_left, clamp_right + 1):
        print bucket, '\t:',
        if bucket in counts:
            for _ in xrange(int(floor(counts[bucket]))):
                print '*',
        print '\n',

def test_bell_curve(samples, scale, min, max, lean):
    '''
    Simple demonstration function to show that random_int_bell_curve does
    generate on a bell curve
    '''
    print_histogram((random_int_bell_curve(min, max, lean) for _ in xrange(samples)), scale, min, max)

def random_OID(generator):
    hex_set = "0123456789abcdef"
    return bson.ObjectId(string.join(sample_wr(hex_set, 24, generator), ''))

def multicall(func, params):
    '''
    Runs func with the various arguments provided in params. Each param value
    should be an iterable, and the function will be called with every
    combination of arguments. For instance,
    multicall(f, {'x':[1, 2], 'y':[3, 4]}) will call f(x=1, y=3), f(x=1, y=4),
    f(x=2, y=3), f(x=2, y=4). Implemented as a generator.
    '''

    for values in itertools.product(*params.itervalues()):
        args = dict(itertools.izip(params.iterkeys(), values))
        yield func(**args), args

def timer(func):
    '''
    Function decorator to time a function
    '''

    def newFunc(*args, **kwargs):
        print "Timing..."
        begin = time.time()
        result = func(*args, **kwargs)
        print "Took %f seconds" % (time.time() - begin)
        return result

    return newFunc

def chunk(iterable, chunk_size):
    '''
    Chunks iterable. Repeatedly yields iterators that yield chunk_size items
    of iterable before stopping. It should be the case that
    chain.from_iterable(chunk(iterable, whatever)) is the same as iterable.
    Note that chunk assumes that each yielded chunk is completely consumed
    before it is iterated again
    '''

    while True:
        next_item = next(iterable) #This will stop iteration by throwing a StopIteration
        yield itertools.islice(itertools.chain((next_item,), iterable), chunk_size)
                
#Lifted directly from the itertools recipies page
def quantify(iterable, pred=bool):
    '''Count how many times the predicate is true'''
    return sum(itertools.imap(pred, iterable))

def sample_wr(population, k, generator=random):
    return [generator.choice(population) for _ in xrange(k)]
