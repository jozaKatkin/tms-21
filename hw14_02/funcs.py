import argparse
from time import sleep
from datetime import (
    timedelta,
    datetime
)
from classes import Time


def prepare_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first_name', required=True)
    parser.add_argument('-ln', '--last_name', required=True)
    parser.add_argument('-t', '--work_time')
    parser.add_argument('-b', '--break_length')
    parser.add_argument('-cycles', '--num_of_cycles')
    parser.add_argument('-name', '--task_name', required=True)
    args = parser.parse_args()
    return args.first_name, args.last_name, args.task_name, args.work_time, int(args.num_of_cycles), args.break_length


def count_time(time):
    end_time = Time(time).convert_to_timedelta()
    start_time = timedelta(hours=0, minutes=0, seconds=0)
    while start_time <= end_time:
        if start_time == end_time:
            break
        else:
            yield start_time
            start_time += timedelta(hours=0, minutes=0, seconds=1)
        if start_time == timedelta(hours=0, minutes=0, seconds=0):
            continue
        sleep(1)


def count_cycles():
    first_name, last_name, task_name, work_time, cycles, break_length = prepare_args()
    cycle_counter = 0
    s = Time(work_time).beautiful_output()
    s2 = Time(break_length).beautiful_output()
    print("Let's start working!")
    while cycle_counter <= cycles:
        if cycle_counter == cycles:
            print("\nNice job!")
            break
        print("\nLet's concentrate for {}".format(s))
        gener_work = count_time(work_time)
        for i in gener_work:
            print(i)
        print("\nLet's take a nap for {}".format(s2))
        gener_break = count_time(break_length)
        for i in gener_break:
            print(i)
        cycle_counter += 1
        print("Cycle number {} finished".format(cycle_counter))


def create_log():
    first_name, last_name, task_name, _, _, _, = prepare_args()
    with open("log_file.txt", "a+") as f:
        s = "{} {}  {:_^13s}  {}\n".format(first_name, last_name, task_name, datetime.today().strftime("%D, %R"))
        f.writelines(s)

