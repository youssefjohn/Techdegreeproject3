# import datetime
# import pytz
import csv
# date = datetime.datetime.now()
# print(date)
#
# pacific = pytz.timezone('US/Pacific')
# date = pacific.localize(date)
# print(date)
# #date = pytz.utc.localize(date)
# print(date)


with open("work_log.csv", newline='') as fp:
    file = csv.DictReader(fp, delimiter = ',')
    file2 = list(file)
    for thing in file2:
        print(thing)

