#!/usr/bin/env python

import sys
from datetime import datetime

for entry in sys.stdin:
    # remove leading and trailing whitespace
    entry = entry.strip()

    # split data in entry
    data = entry.split(',')

    # assuming weekday and 9-5 are normal business hours
    try:
        date = datetime.strptime(data[0] + ' ' + data[1], '%m/%d/%Y %H:%M:%S')
    except ValueError:
        continue

    # move on if the day is a weekend
    if date.weekday() >= 5:
        continue

    shift_start = datetime.strptime(data[0] + ' 9:00:00', '%m/%d/%Y %H:%M:%S')
    shift_end = datetime.strptime(data[0] + ' 17:00:00', '%m/%d/%Y %H:%M:%S')

    # check if time is between a 9-5 work shift
    if shift_start <= date <= shift_end:
        # building id, hour, temperature, count
        print '%s:%s\t%s\t%s\t%s' % (data[6], date.hour, data[3], 1)
