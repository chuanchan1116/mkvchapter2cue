#!/usr/bin/env python3

import argparse
import fileinput
import sys
import xml.etree.ElementTree as ET
from math import ceil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input',
        type=str,
        nargs='?',
        help='The chapter xml to be converted. Default to read form stdin.')
    parser.add_argument('-f', dest='file_name', required=True,
                        help='The file which the cue sheet is for.')
    parser.add_argument('-t', dest='file_type', required=True,
                        choices=['WAVE', 'AIFF', 'MP3'], help='file type')
    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r') as f:
            input = f.read()
    else:
        input = sys.stdin.read()

    root = ET.fromstring(input).find('EditionEntry')
    track = 1
    print(f'FILE "{args.file_name}" {args.file_type}')
    for chapter in root.findall('ChapterAtom'):
        start_time = chapter.find('ChapterTimeStart').text.split(':')
        name = chapter.find('ChapterDisplay').find('ChapterString').text
        cue_min = int(start_time[0]) * 60 + int(start_time[1])
        cue_sec = start_time[2].split('.')[0]
        cue_frame = ceil(float(f'0.{start_time[2].split(".")[1]}') * 75)

        print(f'  TRACK {track:02} AUDIO')
        print(f'    TITLE {name}')
        print(f'    INDEX 01 {cue_min}:{cue_sec}:{cue_frame:02}')
        track += 1


if __name__ == '__main__':
    main()
