#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import librosa
import os 
import sys
import numpy as np

from pydub import AudioSegment
from scipy.io import wavfile

def mp3_to_wav(mp3_voice, wav_voice):
    convert =  AudioSegment.from_mp3(mp3_voice)
    covert.export(destin, format='wav')

def voice_duration(voice):
    return librosa.get_duration(voice)

def voice_rate(voice):
    y, sr = librosa(voice, sr=None)
    return sr

def compare_duration(voice1, voice2):
    d1 = voice_duration(voice1)
    d2 = voice_duration(voice2)

    return d1 == d2 


def  reset_sampling_rate(voice, rate, path):
    y, sr = librosa(voice, sr=None)
    y_rt = librosa.resample(y, sr, rate)

    librosa.output.write_wav(path, y_rt, rate)


def detach_voice_chan(voice, left, right):
    left_voice = []
    right_voice = []

    try:
        rate, wav  = wavfile.read(voice)
        for item in wav :
            left_voice.append(item[0])
            right_voice.append(item[1])

        wavfile.write(left, rate, np.array(left_voice))
        wavfile.write(right, rate, np.array(right_voice))

    except IOError as e:
        print('datach voice channel error %s' % str(e))
    except:
        print('Unkonw error', sys.exec_info())




if __name__ == '__main__':
    pass
