#!/usr/bin/env python

import os
import argparse
import filetype 

import voice as vc

def file_type(filepath):
    return filetype.guess(filepath)

if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser(description='voice clone tool')

    parser.add_argument('--phoneme', type=str, 
                                    help='The path of voice as phoneme', required=True)

    parser.add_argument('--base-band',type=str, 
                                    help='The path of voice as base band', required=True)

    parser.add_argument('--output', type=str,
                                    help='The path of result voice tools handled ', required=False)

    args = parser.parse_args()

    if not os.path.isfile(args.phoneme):
        raise Exception("The phoneme file not exists")

    if not os.path.isfile(args.base_band):
        raise Exception("The base band file not exists")
    """
    v, rate = vc.voice_load("resources/luo.mp3")
    print(rate)




