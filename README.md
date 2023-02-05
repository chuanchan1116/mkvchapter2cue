#mkvchapter2cue

This program will convert a given MKV chapter format to cue format.

## Usage
```
usage: main.py [-h] -f FILE_NAME -t {WAVE,AIFF,MP3} [input]

positional arguments:
  input               The chapter xml to be converted. Default to read form stdin.

options:
  -h, --help          show this help message and exit
  -f FILE_NAME        The file which the cue sheet is for.
  -t {WAVE,AIFF,MP3}  file type
```

