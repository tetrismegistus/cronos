#!/usr/bin/python3

import argparse
import os
from colorama import init, Fore
from task import RecurrentTask, Task
from serialization import load_file, save_file
from tasklist_interface import complete_task, delete_task, filter_list, sort_list 

COLOR_DICT = {'green': Fore.GREEN,
              'yellow': Fore.YELLOW,
              'red': Fore.RED,
              'blue': Fore.BLUE}


def print_tasks(task_list, list_type='incomplete', today=False):
    if list_type != 'full':
        filtered = filter_list(task_list, list_type)
        tasks = sort_list(filtered)
    else: 
        tasks = sort_list(task_list)
    
    
    print('#\tDue Date\tTask')
    print('-\t----------\t----')
    for i, t in enumerate(tasks):
        print(COLOR_DICT[t.get_status()] + '{}\t{}\t{}'.format(i, t.due, t.description))


def add_task(task_string, task_list):
    t = task_string.split(',')
    description = t[0]
    due_date = t[1]
    try:
        recurrence = t[2]
    except IndexError:
        recurrence = False

    if recurrence:
        task = RecurrentTask(description, due_date, recurrence)
    else:
        task = Task(description, due_date)

    task_list.append(task)


def main(args):

    if args.f:
        filename = os.path.expanduser(args.f)
    else:
        filename = os.path.expanduser('~/.tasks.p')

    try:
        task_list = load_file(filename)
    except FileNotFoundError:
        print('No task list exists')
        task_list = []
        save_file(filename, task_list)

    if args.a:
        add_task(args.a, task_list)
        save_file(filename, task_list)
    if args.c is not None:
        complete_task(task_list, args.c)
        save_file(filename, task_list)
    if args.d is not None:
        task_list = delete_task(task_list, int(args.d))
        save_file(filename, task_list)

    list_type = args.r
    print_tasks(task_list, list_type)


if __name__ == '__main__':
    init()
    parser = argparse.ArgumentParser(prog='cronos.py', usage='%(prog)s')

    parser.add_argument('-a', help="Add task [cronos -a 'description',due date,recurrence]")
    parser.add_argument('-c', help="Complete task [cronos -c task number]", type=int)
    parser.add_argument('-f', help="specify non-default filename [cronos -f file name]")
    parser.add_argument('-d', help="delete a task [cronos -d task number]")
    parser.add_argument('-t', help="print just today's tasks", action='store_true')
    parser.add_argument('-r', help="Choose report type", choices=('complete', 'incomplete', 'full', 'today'), default='incomplete')
    args = parser.parse_args()
    main(args)
