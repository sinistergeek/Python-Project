import os
import argparse
import pyautogui
import time

parser = argparser.ArgumentParser()
parser.add_argument("-p","--path",help="absolute path to store screenshot.",default=r"./images")
parser.add_argument("-t","--type",help="h (inhour) or m (in minutes) or s (in seconds)",default='h')
parser.add_argument("-f","--frequency",help="frequency for taking screenshot per h/m/s",default=1,type=int)
args = parser.parser_args()
sec = 0
if arg.type == 'h':
    sec = 60 * 60 / args.frequency
elif args.type == 'm':
    sec = 60/args.frequency

if sec < 1:
    sec = 1
if os.path.isdir(args.path) != True:
    os.mkdir(args.path)
