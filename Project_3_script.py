import csv
import re
import datetime
import sys
import pytz
import os
from classes_for_project_3 import Time


def greaterthanone(x):
    if len(x) < 1:
        x = "Field left empty."
        return x


def users_timezone():
    date = datetime.datetime.now()
    new_date = pytz.utc.localize(date)
    return new_date


def add():


    task = input("Please enter your TASK: ")
    greaterthanone(task)
    time = input("Now enter how long it took Days/hours/minutes: ")
    greaterthanone(time)
    notes = input("Any additional notes you would like to add? ")
    greaterthanone(notes)
    users_timezone()
    print("Your date has been automatically recorded :)\n"
          "You'll now be sent back to the main menu.")


    with open("work_log.csv", "a") as fp:
        fieldnames = ["task name", "time spent", "additional notes", "date recorded"]
        writer = csv.DictWriter(fp, fieldnames)
        writer.writerow({"task name": task,
                         "time spent": time,
                         "additional notes": notes,
                         "date recorded": users_timezone()
                         })

    return time, task, notes


def lookup():
    choice = input("How would you like to lookup the data?\n"
                   "Find by date\n"
                   "Find by time spent\n"
                   "Find by exact search\n"
                   "find by pattern\n"
                   "Please Enter The Exact Method: ").lower()

    if choice == "time":
        use_class = Time()
        use_class.find_by_time()

    elif choice == "date":
        use_class = Date()
        use_class.find

time = None
task = None
notes = None

format = '%Y-%m-%d %H:%M:%S %Z%z'
filename = "work_log.csv"
file_exists = os.path.isfile((filename))


with open("work_log.csv", "a") as fp:
    fieldnames = ["task name",
                  "time spent",
                  "additional notes",
                  "date recorded"]
    writer = csv.DictWriter(fp, fieldnames)
    if not file_exists:
        writer.writeheader()




# Main body to ask to begin
while True:

    path = input("Hi welcome to Work Log!\n"
                 "Please tell us what you would like to do.\n"
                 "a) Add a new entry\n"
                 "b) Lookup an existing entry \n"
                 "c) Quit Work Log")

    if path == 'c':
        print("bye")
        break
    elif path != "a" and path != "b":
        print("Please enter 'a', 'b' or 'c'")
        continue
    elif path == "a":
        add()
    elif path == "b":
        lookup()

