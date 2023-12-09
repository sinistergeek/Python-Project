import argparse
import gzip
import os
import shutil
import sys
import threading


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target',nargs=1,required=True,help='Target Backup folder')

