#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import pyworld as pw
import soundfile as sf

def detach_voice_f0(x, rate):
    _f0, _t = pw.harvest(x, rate)
    return pw.stonemask(x, _f0, _t, rate)

def detach_voice(x, rate):
    _f0, t = pw.harvest(x, rate)

    f0 = pw.stonemask(x, _f0, t, rate)
    sp =  pw.cheaptrick(x, f0, t, rate)
    ap = pw.d4c(x, f0, t, rate)

    return f0, sp, ap

def voice_synthesize(f0, sp, ap, rate):
     return pw.synthesize(f0, sp, ap, rate, pw.default_frame_period)

def synthesize(ph_path, f0_path, output_path):
    ph_x, rate = sf.read(ph_path)
    ph_f0, ph_sp, ph_ap = detach_voice(ph_x, rate)

    f0_x, f0_rate = sf.read(f0_path)
    f0_f0 = detach_voice_f0(f0_x, f0_rate)

    v = voice_synthesize(f0_f0, ph_sp, ph_ap, rate)
    sf.write(output_path, v, rate)



if __name__ == '__main__':
    synthesis("output.mp3", "shan.mp3", "1.wav")
