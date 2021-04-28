#!/usr/bin/python3
import sys
from statistics import stdev

current_travel_number = None
current_start_timestamp = None

statistics = dict()

for line in sys.stdin:

	key, value = line.strip().split("\t")

	line_id , variant, _, _ = key.split(".")
	travel_number, timestamp, bus_stop, timeframe = value.split(".")

	timestamp = int(timestamp)

	if current_travel_number is None or current_travel_number != travel_number :
		current_travel_number = travel_number
		current_start_timestamp = timestamp
	else :
		time_difference = timestamp - current_start_timestamp
		key = "{}.{}.{}.{}".format(line_id, variant, timeframe, bus_stop)
		if key not in statistics.keys() :
			statistics[key] = []

		statistics[key].append(time_difference)


for key, value in statistics.items() :
	if len(value) == 1 :
		data = value.append(value[0])

	line_id, variant, timeframe, stop = key.split(".")
	print("<{},{},{},{}> min:{} max:{} average:{:.2f} std:{:.2f}".format(\
		line_id, variant, timeframe, stop, \
		min(value), \
		max(value), \
		sum(value) / len(value), \
		stdev(value)))
		