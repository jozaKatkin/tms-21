import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory_name', required=True)
parser.add_argument('-fn', '--file_name', required=True)
args = parser.parse_args()


os.mkdir(args.directory_name)
file_path = args.directory_name + "/" + args.file_name
f = open(file_path, "w")
f.close()

