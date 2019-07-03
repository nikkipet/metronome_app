# Metronome App
# Nikki Pet, June 2019

import time
import sys
from pydub import AudioSegment
from pydub.playback import play
from glob import glob

import timeit



#convert audio files
db = AudioSegment.from_wav("ddownbeat.wav")
ob = AudioSegment.from_wav("oofbeat.wav")
##ob_len = len(ob) / 1000.
##db_len = len(db) /1000.
##print(ob_len)
##print(db_len)

def metronome(bpm, bpb):
	sleep = 60.0 / bpm
	##First 'sleep' seconds of file##
	ob_short = ob[:sleep*1000]
	db_short = db[:sleep*1000]
	len_ob = len(ob)/1000
	len_db = len(db)/1000

	#Metronome code
	counter = 0
	while True:
		#Offbeat
		if counter % bpb:
			print('tick')
			play(ob)
			#time.sleep(sleep_ob)
			##if sleep > len_ob:
				##print("HEEEEEEEEEELO")
				##time.sleep(sleep-len_ob)
		#Downbeat
		else:
			print('TICK')
			play(db)
			##if sleep > len_db:
				##print("HEEEEEEEEEEEELO")
				##time.sleep(sleep-len_db)
			##time.sleep(sleep_db)
		##time.sleep(sleep)
		counter += 1

def main():
	#User input
	bpm = int(input("Beats per minute: "))
	bpb = int(input("Subdivisions per measure: "))

	metronome(bpm, bpb)
	
	
	
	

main()