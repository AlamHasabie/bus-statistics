#!/usr/bin/python
import sys

current_count = 0
current_key = None

for line in sys.stdin:

	data = line.strip().split("\t")
	print(data)
