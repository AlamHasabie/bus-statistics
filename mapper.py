#!/usr/bin/python
import sys
from datetime import datetime

occurence_set = set()

def join_values(*args) :
	return ".".join([str(arg) for arg in args])

def get_timeframe(time):
	if 4 * 60 <= time.minute + time.hour * 60 <= 12 * 60 :
		return "morning"

	if 12 * 60 + 1 <= time.minute + time.hour * 60 <= 20 * 60 :
		return "afternoon"

	return "night"

for line in sys.stdin:
	# remove leading and trailing whitespace
	data = line.strip().split(",")
	try :
		timestamp = int(data[0])/1000000

		# skip data without line_id
		line_id = int(data[1])

		# We distinct journey with different direction, hence 
		# variant = direction + variant
		variant = data[2] + "-" + data[3]
		travel_number = int(data[5])	
		ts_date = datetime.fromtimestamp(timestamp)
		timeframe = get_timeframe(ts_date)
	
		# With this, we skip data with null bus stop
		bus_stop = int(data[13])

		occurence_set_val = join_values(line_id, variant, travel_number)

		# Format : line_id.variant.travel_number.timestamp
		# Key : compound line_id.variant(primary).travel_number.timestamp(secondary, sorting)
		# info : travel_number.timestamp.bus_stop.timeframe
		at_stop = data[14]
		if data[14] != "0" and (occurence_set_val not in occurence_set):
			occurence_set.add(occurence_set_val)
			key = join_values(line_id, variant, travel_number, timestamp)
			value = join_values(travel_number, timestamp, bus_stop, timeframe, at_stop)
			print("{}\t{}".format(key, value))

	except Exception :
		continue



