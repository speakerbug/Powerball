# File: powerball.py
# Henry Saniuk, Jr.
# This script reads in a ticket file and a string of winning numbers
# and determins how much money you won in powerball
#
# Command Line usage:
#   python powerball.py <winning numbers> <powerball>

import sys

try:
	winningNumbers = str(sys.argv[1])
	powerball = int(sys.argv[2])
except IndexError:
	print 'Usage: python powerball.py <winning numbers> <powerball>'

print 'Success'
