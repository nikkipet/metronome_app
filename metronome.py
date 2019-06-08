# Metronome App
# Nikki Pet, June 2019

import time
import sys

bpm = int(input("Beats per minute: "))
bpb = int(input("Subdivisions per measure: "))

def main(bpm, bpb):
	sleep = 60.0 / bpm
	counter = 0
	while True:
		#usr_input = input()
		if counter % bpb:
			print('tick')
		else:
			print('TICK')
		time.sleep(sleep)
		counter += 1


main(bpm, bpb)