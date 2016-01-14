# File: powerball.py
# Henry Saniuk, Jr.
# This script reads in a ticket file and a string of winning numbers
# and determins how much money you won in powerball
#
# Command Line usage:
#   python powerball.py <winning numbers> <powerball>

import sys

try:
	winningNumbers = str(sys.argv[1]).split(",")
	powerball = int(sys.argv[2])
	
	# Open the tickets file and read/parse it
	with open('tickets.txt','r') as f:
	    	seq_data = f.readlines()
    		for i in range(len(seq_data)):
        		seq_data[i] = seq_data[i].rstrip()
	#loop through your numbers to see if any won
	for i in range(len(seq_data)):
		currentNumbers = seq_data[i].split(",")
		numbersMatched = 0
		for n in range(len(currentNumbers)-1):
			if currentNumbers[n] in winningNumbers:
				numbersMatched = numbersMatched + 1
		if currentNumbers[len(currentNumbers)-1] == powerball:
			powerballMatched = "MATCHED"
		else:
			powerballMatched = "NOT MATCHED"
		print currentNumbers
		print 'Numbers matched: ' + str(numbersMatched) + ' Powerball: ' + powerballMatched

except IndexError:
	print 'Usage: python powerball.py <winning numbers> <powerball>'
