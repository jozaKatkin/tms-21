import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory_name', required=True)
args = parser.parse_args()

file_path = os.path.realpath("python/home/joza/Documents/Dev/tms-21/cw14/task_14_05.py")
dir_name = os.path.dirname(args.directory_name)
s = "cw14/" + args.directory_name
os.mkdir(s)
