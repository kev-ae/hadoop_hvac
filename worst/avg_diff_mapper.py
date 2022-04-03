#!/usr/bin/env python

import sys

# get input from stdin
for entry in sys.stdin:
    # remove leading and trailing whitespace
    entry = entry.strip()

    # split data in entry
    data = entry.split(',')

    # calculate the difference between the target temperature and the actual temperature
    try:
        target_temp = int(data[2])
        actual_temp = int(data[3])
    except ValueError:
        # if entry is first entry that contain only the column labels
        continue

    diff = abs(target_temp - actual_temp)

    # send to reducer the buiding id, system, temperature difference, and count for avg
    print '%s:%s\t%s\t%s' % (data[6], data[4], diff, 1)