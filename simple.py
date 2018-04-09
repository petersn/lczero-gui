#!/usr/bin/python

import sys, time

with open("test2") as f:
	for line in f:
		sys.stdout.write(line)
		sys.stdout.flush()
		time.sleep(0.02)

exit()

i = 0
while True:
	i += 1
	sys.stdout.write("Val")
	sys.stdout.flush()
	time.sleep(0.5)
	sys.stdout.write("ue: %i\n" % i)
	sys.stdout.flush()
	time.sleep(1)

