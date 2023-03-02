#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import soundfile as sf


def synthesis(ph_path, f0_path, output_path):
    ph_x, rate = sf.read(ph_path)
    ph_f0, ph_sp, ph_ap = detach_voice(ph_x, rate)

    f0_x, f0_rate = sf.read(f0_path)
    f0_f0 = detach_voice_f0(f0_x, f0_rate)

    v = voice_synthesize(f0_f0, ph_sp, ph_ap, rate)
    sf.write(output_path, v, rate)



if __name__ == '__main__':
    pass
