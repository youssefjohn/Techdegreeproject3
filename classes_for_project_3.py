import csv
import re
import datetime
import pytz



class Time:
    print("Please enter the exact time match\n"
          "If time does not match, no results will be returned.")


    def __init__(self):
        self.time_brackets = 1000

    def find_by_time(self):
        self.choice = input("Please input the time you want to find in minutes. E.g.'60': ")


        with open("work_log.csv", newline='') as fp:
            reader = csv.DictReader(fp, delimiter=',')
            for row in reader:
                if self.choice in row['time spent']:
                    for key, value in row.items():
                        print(key,':' , value)

class Date:
    print("Please enter the date in the format YY/MM/DD")

    