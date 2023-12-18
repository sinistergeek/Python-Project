import os
import zipfile
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l","--zippedfile",required=True,help="Zipped file")
args = vars(parser.parse_args())
zip_file = args['zippedfile']
file_name = zip_file

if os.path.exists(zip_file) == False:
    sys.exit("No suuch file present in the directory")
def extact(zip_file):
    file_name = zip_file.split(".zip")[0]
    if zip_file.endswith(".zip"):

