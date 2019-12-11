import argparse
from time import sleep
from datetime import (
    datetime,
    timedelta,
)


def prepare_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first_name', required=True)
    parser.add_argument('-ln', '--last_name', required=True)
    parser.add_argument('-ho', '--hours', required=True)
    parser.add_argument('-mi', '--minutes', required=True)
    parser.add_argument('-se', '--seconds', required=True)
    args = parser.parse_args()
    return args.first_name, args.last_name, map(int, [args.hours, args.minutes, args.seconds])


def create_log(first_name, last_name):
    with open("log_file.txt", "w") as f:
        s = "{} {}: {}\n".format(first_name, last_name, datetime.today().strftime("%D, %R"))
        f.writelines(s)


def my_generator(h, m, s):
    start_time = timedelta(hours=0, minutes=0, seconds=0)
    alarm_time = timedelta(hours=h, minutes=m, seconds=s)
    while start_time <= alarm_time:
        if start_time == alarm_time:
            yield "ALARM!!!"
            break
        else:
            yield start_time
            start_time += timedelta(hours=0, minutes=0, seconds=1)
        if start_time == timedelta(hours=0, minutes=0, seconds=0):
            continue
        sleep(1)







