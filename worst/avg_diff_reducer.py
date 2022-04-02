#!/usr/bin/env python

from operator import itemgetter
import sys

curr_building = None
curr_system = None
system = None
building = None
sum = 0
curr_count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    building, system, diff, count = line.split('\t', 4)

    # typecast count and diff to int, ignore/discard if not a number
    try:
        count = int(count)
        diff = int(diff)
    except ValueError:
        continue

    # add differances than get the average and print it out
    if curr_building == building and curr_system == system:
        sum += diff
        curr_count += count
    else:
        if curr_building and curr_system:
            avg = sum / curr_count
            print 'BuildingID: %s\tSystem: %s\tAverage: %s' % (curr_building, curr_system, avg)
        
        # reset variables
        curr_count = count
        curr_building = building
        curr_system = system
        sum = 0

# print last entry
if curr_building == building and curr_system == system:
    avg = sum / curr_count
    print 'BuildingID: %s\tSystem: %s\tAverage: %s' % (curr_building, curr_system, avg)