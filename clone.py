#!/usr/bin/env python



import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='voice clone tool')

    parser.add_argument('--source-file-path', type=str, 
					help='Path of voice', required=True)

    args = parser.parse_args()
