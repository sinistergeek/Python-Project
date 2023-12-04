import os
import zipfile
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-I","--zippedfile",required=True,help="Zipped file")
file_name = zip_file

if os.path.exists(zip_file) == False:
    sys.exit("No such file presentin the directory")
    def extract(zip_file):
        file_name = zip_file.split(".zip")[0]


