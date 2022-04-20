#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
General Code for sound recording

This code will record and save the sound recording in a .wav file for a specified duration.
Requires: 1 USB microphone

'''
import pyaudio
import wave
import time

filename = 'output-white-noise.wav'

# Constants for audio devices
FORMAT  = pyaudio.paInt16   # audio format specific for microphone
CHANNELS = 2                # number of audio streams to use
RATE = 48000                # 48kHz since mic is specific at 48kHz
FRAMES_PER_BUFFER = 1024    # number of frames the speaker is taking in
DURATION = 1*60             # in seconds EDIT HERE

# Create an itnerface to PortAudio
pa = pyaudio.PyAudio()

# Save the recorded data in a .wav format
def _prepare_file(fname, mode='wb'):
    sf = wave.open(fname, mode)
    sf.setnchannels(CHANNELS)
    sf.setsampwidth(pa.get_sample_size(FORMAT))
    sf.setframerate(RATE)
    return sf

wf = _prepare_file(filename, 'wb')

def callback(in_data, frame_count, time_info, status):
        wf.writeframes(in_data)
        return in_data, pyaudio.paContinue
    
stream = pa.open(format=FORMAT,
                 channels = CHANNELS,
                 rate = RATE,
                 input=True,
                 frames_per_buffer = FRAMES_PER_BUFFER,
                 input_device_index = 2, # EDIT HERE
                 stream_callback = callback)

print('recording...')

start = time.time()
elapsed = 0.0

# Store data in chunks for "duration" seconds
while elapsed < CHANNELS*DURATION: # since channels used are 2, IF 1 CHANNEL, DURATION IS 1*DURATION
        # start stream
        stream.start_stream() 
        elapsed = time.time() - start
        
# Stop and close the stream
stream.stop_stream()
stream.close()
wf.close()

print('Done!')

# sf.writeframes(b''.join(frames))
# sf.close()
