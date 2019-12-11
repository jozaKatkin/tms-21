import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory_name', required=True)
parser.add_argument('-fn', '--file_name', required=True)
args = parser.parse_args()


os.mkdir(args.directory_name)
file_path = args.directory_name + "/" + args.file_name
print(args.file_name)
if ".py" in args.file_name:
    with open(file_path, "w") as py_file:
        s = "def main():\n    pass\n\n\nif __name__ == '__main__':\n    main()\n"
        py_file.writelines(s)
else:
    f = open(file_path, "w")
    f.close()
