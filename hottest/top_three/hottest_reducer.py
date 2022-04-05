#!/usr/bin/env python

from operator import itemgetter
import sys

cur_hour = None
cur_building = None
building = None
hour = None
sum = 0
cur_count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    building_hour, temp, count = line.split('\t', 3)
    t = building_hour.split(':')
    building = t[0]
    hour = t[1]

    # typecase temp and count
    try:
        temp = float(temp)
        count = float(count)
    except ValueError:
        continue

    if cur_building == building and cur_hour == hour:
        sum += temp
        cur_count += count
    else:
        if cur_building and cur_hour:
            avg = sum / cur_count
            print '%s\t(BuildingID: %s\tHour: %s)' % (avg, cur_building, cur_hour)

            # reset variables
            cur_count = count
            cur_building = building
            cur_hour = hour
            sum = temp

# print last entry
if cur_building == building and cur_hour == hour:
    avg = sum / cur_count
    print '%s\t(BuildingID: %s\tHour: %s)' % (avg, cur_building, cur_hour)
