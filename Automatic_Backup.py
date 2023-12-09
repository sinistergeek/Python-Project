import argparse
import gzip
import os
import shutil
import sys
import threading


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target',nargs=1,required=True,help='Target Backup folder')
    parser.add_argument('-s','--source',nargs='+',required=True,help='Source File to be added')
    parser.add_argument('-c','--compress',nargs=1,type=int,help='Gzip threshold in bytes,Deafult 1024KB',default=[102400])
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    return parser.parser_args()

def size_if_newer(source,target):
    src_stat = os.stat(source)
    try:
        target_ts = os.stat(target).st_mtime
    except FileNotFoundError:
        try:
            target_ts = os.stat(target + '.gz').st_mtime
        except FileNotFoundError:
            target_ts = 0
    return src_stat.st_size if(src_stat.st_mtime - target_ts > 1) else False


