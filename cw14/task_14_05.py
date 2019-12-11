import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory_name', required=True)
args = parser.parse_args()

s = "cw14/" + args.directory_name
os.mkdir(s)
