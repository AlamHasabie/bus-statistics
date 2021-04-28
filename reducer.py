#!/usr/bin/python
import sys

current_travel_number = None
current_start_timestamp = None
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
		print("{}.{}.{}.{}\t{}").format(line_id, variant, timeframe, bus_stop, time_difference)