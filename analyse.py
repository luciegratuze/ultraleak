#!/usr/bin/python
# -*- coding: utf-8 -*-

import wave
import struct
import numpy as np
from scipy.io import wavfile
import sys, os, getopt

# Applies fft to the array representing a audio signal it receives as argument, and returns the dominant frequency

def analyse(data, data_size, frate):  # Adapted from the first answer on https://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python

	data = struct.unpack('{n}h'.format(n=data_size), data)
	data = np.array(data)

	w = np.fft.fft(data)
	freqs = np.fft.fftfreq(len(w))

	# Find the peak in the coefficients
	idx = np.argmax(np.abs(w))
	freq = freqs[idx]
	freq_in_hertz = abs(freq * frate)
	print(freq_in_hertz)
	return(freq_in_hertz)

#main function: opens the .wav file, and extracts the sent.
	
def main(argv):

	hlp = "analyse.py -f <File_Path> -t <Tolerance> -1 <HZ> -0 <HZ> -d <Duration>"
	try:
		opts, args = getopt.getopt(argv,"h1:0:f:d:t:",["help","one","zero","file","duration","tolerance"])
	except getopt.GetoptError as err:
		print("~ %s" % str(err))
		print(hlp)
		sys.exit()

	one,zero,dur,tolerance,myAudio = -1,-1,-1,-1,""
    
	for opt, arg in opts:
		if opt == '-h':
			print(hlp)
			sys.exit()

		elif opt in ("-f","--file"):
			myAudio = arg
			if not os.path.exists(myAudio):
				print("File in path ", myAudio, " does not exists")
				sys.exit()
        
		elif opt in ("-1","--one"):
			one = int(arg)

		elif opt in ("-0","--zero"):
			zero = int(arg)
        
		elif opt in ("-d","--duration"):
			dur = int(arg)/1000
		
		elif opt in ("-t", "--tolerance"):
			tolerance = int(arg)
    
	if one == -1 or zero == -1 or tolerance == -1 or dur == -1 or myAudio == "":
		print(hlp)
		sys.exit()

	#Determines T=duration of an element, cuts the signal in pieces of T, and calls analyse(), and interprets the returned result to write it to output		
		
	samplingFreq, mySound = wavfile.read(myAudio)
	l = len(mySound)
	T = int(int(samplingFreq)*dur) #number of points that correspond to one bit
	n = int(l/T) #number of bits that are contained in the sample
	
	f = open("output", "wb")
	f_v = open("output.txt", "w")
	
	count = 0
	bit_str = ""
	for i in range(n+1):
		if (count == 8):
			m = int(bit_str, 2)
			byte = bytes([m])
			print(byte)
			f.write(byte)
			bit_str = ""
			count = 0
		if (i == n):
			break
		subdata = mySound[i*T:(i+1)*T]
		max_freq = analyse(subdata, T, samplingFreq)
		if (abs(max_freq - one) <= tolerance):
			bit_str = "1" + bit_str
			count+=1
			#f_v.write("1")
			#if (count == 8):
			#	f_v.write("  ")
			#print(1)
		elif (abs(max_freq - zero) <= tolerance):
			bit_str = "0" + bit_str
			count+=1
			#f_v.write("0")
			#if (count == 8):
			#	f_v.write("  ")
			#print(0)
		#else:
			#f_v.write("?")
			#if (count == 8):
			#	f_v.write("  ")
			#print("invalid freq")
	
	f.close()
	
	

if __name__ == '__main__':
    main(sys.argv[1:])
