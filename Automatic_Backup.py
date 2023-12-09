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


