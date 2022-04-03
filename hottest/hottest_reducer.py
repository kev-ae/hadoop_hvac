#!/usr/bin/env python

from operator import itemgetter
import sys

curr_hour = None
curr_building = None
building = None
hour = None
sum = 0
cur_count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    building_hour, temp, count = line.split('\t', 3)
    temp = building_hour.split(':')
    building = temp[0]
    hour = temp[1]