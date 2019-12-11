import csv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('echo')
    args = parser.parse_args()
    print(args)
    print('First name:', args.first_name)
    print('Last name:', args.last_name)
    print('echo:', args.echo)

    with open("filename2.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([args.first_name, args.last_name, args.echo])


if __name__ == "__main__":
    main()
