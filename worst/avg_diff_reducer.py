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
    building_system, diff, count = line.split('\t', 3)
    temp = building_system.split(':')
    building = temp[0]
    system = temp[1]

    # typecast count and diff to int, ignore/discard if not a number
    try:
        count = float(count)
        diff = float(diff)
    except ValueError:
        continue

    # add differances than get the average and print it out
    if curr_building == building and curr_system == system:
        sum += diff
        curr_count += count
    else:
        if curr_building and curr_system:
            avg = sum / curr_count
            print '%s\t(BuildingID: %s\tSystem: %s)' % (avg, curr_building, curr_system)
        
        # reset variables
        curr_count = count
        curr_building = building
        curr_system = system
        sum = diff

# print last entry
if curr_building == building and curr_system == system:
    avg = sum / curr_count
    print '%s\t(BuildingID: %s\tSystem: %s)' % (avg, curr_building, curr_system)