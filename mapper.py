#!/usr/bin/python3
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
		timestamp = int(data[0])//1000000

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

		occurence_set_val = join_values(line_id, variant, travel_number, bus_stop)

		# Data is already sorted by timestamp
		# Original paper uses control point, so we want to simulate bus stops as control points
		# To do this, we just take the first occurence of data with key :
		# line_id, variant, travel_number, bus_stop

		# bus_stop means where the bus starts from
		# so , transition from bus stop 1 -> bus stop 2 means that the bus arrives at bus stop 2
		# so we take the first occurence of said data to be

		# Additionally, we may have some bus stops without at stops = 1
		# This is fine, since we can assume that :
		# 1. We can predict the data from the first timestamp, or
		# 2. The bus did not stop at said bus stop

		# Format : line_id.variant.travel_number.timestamp
		# Key : compound line_id.variant(primary).travel_number.timestamp(secondary, sorting)
		# info : travel_number.timestamp.bus_stop.timeframe
		if occurence_set_val not in occurence_set :
			occurence_set.add(occurence_set_val)
			key = join_values(line_id, variant, travel_number, timestamp)
			value = join_values(travel_number, timestamp, bus_stop, timeframe)
			print("{}\t{}".format(key, value))

	except Exception :
		continue



