#!/usr/bin/env python

from operator import itemgetter
import sys

cur_building = None
cur_count = 0
building = None
sum = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    building, temp, count = line.split('\t', 3)

    try:
        temp = float(temp)
        count = float(count)
    except ValueError:
        continue

    if cur_building == building:
        sum += temp
        cur_count += count
    else:
        if cur_building:
            avg = sum / cur_count
            print '%s\t (BuildingID: %s)' % (avg, cur_building)

        # reset variables
        cur_count = count
        sum = temp
        cur_building = building

# print last entry
if cur_building == building:
    avg = sum / cur_count
    print '%s\t (BuildingID: %s)' % (avg, cur_building)