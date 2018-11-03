import csv,os,sys,datetime,pytz,re
import pandas as pd


def find_by_date_range():
    '''THIS FUNCTION TAKES TWO DATE RANGES FROM A USER,
       IT THEN LOOPS THROUGH THE CSV AND IF A MATCH IS MADE,
       IT SHOWS ALL OF THE CSV ROWS THAT ARE WITHIN THE DATE RANGE
    '''

    date_entry = input('Enter a date (i.e. 2017,7,1)')
    year, month, day = map(int, date_entry.split(','))
    date1 = datetime.date(year, month, day)

    date_entry = input('Enter a date (i.e. 2017,7,1)')
    year, month, day = map(int, date_entry.split(','))
    date2 = datetime.date(year, month, day)

    delta = date2 - date1
    o = []
    count = -1
    for i in range(delta.days + 1):
        o.append((date1 + datetime.timedelta(i)).strftime('%Y-%m-%d'))

    with open("work_log1.csv", 'r') as fp:
        reader = csv.DictReader(fp, delimiter = ',')
        for row in reader:
            count += 1
            for thing in o:
                if thing == row["date"]:
                    for key, value in row.items():
                        print(key,':', value)

                    print("")
                    edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
                    print("")

                    if edit_or_previous == 'e':
                        edit_coloumn = input("What would you like to edit?\n"
                                             "A) Task\n"
                                             "B) Time\n"
                                             "C) Notes\n"
                                             "D) Date").lower()
                        if edit_coloumn == 'a':
                            edit("task", count)
                        elif edit_coloumn == 'b':
                            edit("time", count)
                        elif edit_coloumn == 'c':
                            edit("notes", count)
                        elif edit_coloumn == 'd':
                            edit("date", count)

                    elif edit_or_previous == "p":
                        with open("work_log1.csv", 'r') as p:
                            reader = csv.reader(p, delimiter=",")
                            for _, line in enumerate(reader):
                                if _ == count:
                                    print("Here is your previous entry:\n"
                                          "")
                                    print("task: ", line[0])
                                    print("time: ", line[1])
                                    print("notes: ", line[2])
                                    print("date: ", line[3])
                                    print("")
                                    keep_going = input("Press Enter to continue").lower()
                                    print("")


def find_by_date_exact():
    '''THIS FUNCTION TAKES AN EXACT DATE FROM A USER,
       IT THEN LOOPS THROUGH THE CSV AND IF A MATCH IS MADE,
       IT SHOWS ALL OF THE CSV ROWS THAT MATCH THAT EXACT DATE
    '''

    while True:
        find = input("Please enter a valid date in the form YYYY-MM-DD.\n"
                     "> ")
        if len(find) < 1:
            continue
        else:
            break

    print("Matches will appear below\n"
          "If no matches were made\n"
          "You will return back to the previous menu.\n"
          "")
    count = -1
    with open("work_log1.csv", 'r') as fp:
        reader = csv.DictReader(fp, delimiter = ',')
        for row in reader:
            count += 1
            if find in row["date"]:
                for key, value in row.items():
                    print(key,':', value)

                print("")
                edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
                print("")

                if edit_or_previous == 'e':
                    edit_coloumn = input("What would you like to edit?\n"
                                         "A) Task\n"
                                         "B) Time\n"
                                         "C) Notes\n"
                                         "D) Date").lower()
                    if edit_coloumn == 'a':
                        edit("task", count)
                    elif edit_coloumn == 'b':
                        edit("time", count)
                    elif edit_coloumn == 'c':
                        edit("notes", count)
                    elif edit_coloumn == 'd':
                        edit("date", count)

                elif edit_or_previous == "p":
                    with open("work_log1.csv", 'r') as p:
                        reader = csv.reader(p,delimiter=",")
                        for _, line in enumerate(reader):
                            if _ == count:
                                print("Here is your previous entry:\n"
                                      "")
                                print("task: ",line[0])
                                print("time: ", line[1])
                                print("notes: ", line[2])
                                print("date: ", line[3])
                                print("")
                                keep_going= input("Press Enter to continue").lower()
                                print("")

def userstime():
    '''THIS FUNCTION IS RUN DURING THE ADD FUNCTION,
       ONCE THE USER FILLS OUT WHAT THEY WANT ADDED,
       TO THE CSV, THIS FUNCTION RUNS AND CAPTURES,
       THE TIME THEY ENTERED THAT INFORMATION.
    '''

    userst = datetime.datetime.now()
    new_userst = pytz.utc.localize(userst)
    return new_userst


def edit(x,y):
    '''THIS FUNCTION IS RUN DURING OTHER FUNCTIONS,
       IT TAKES AN INPUT OF DATA,
       THEN IT CHANGES THE CSV BASED ON ITS INDEX
       Y = INDEX, X = CHANGE
    '''

    new_change = input("input new data: ")
    fp = pd.read_csv("work_log1.csv")
    fp.set_value(y, x, new_change)
    fp.to_csv("work_log1.csv", index=False)
    print("Your change has been made\n"
          "")


def add():
    '''THIS FUNCTION TAKES INPUT FROM A USER,
       IT THEN ADDS A NEW ROW OF INPUTS TO THE CSV FILE
    '''

    taskname = input("What is your task name? ")
    timetaken = input("How long did it take in minutes? ")
    addnotes = input("Any additional notes? ")
    print("Your date has been automatically added, Thank you.")

    with open("work_log1.csv", 'a') as fp:
        fieldnames = ["task", "time", "notes", "date"]
        writer = csv.DictWriter(fp,fieldnames=fieldnames)
        writer.writerow({fieldnames[0]: taskname, fieldnames[1]: timetaken,
                          fieldnames[2]: addnotes, fieldnames[3]:userstime()})

    return taskname, timetaken, addnotes


def lookup():
    '''THIS FUNCTION ALLOWS THE USER TO LOOKUP DATA,
       BY TAKING SOME INPUT, E.G, IF THEY WANT TO,
       FIND "DATE", THEN THEY TYPE "A" AND ENTER
    '''

    while True:
        find = input("What would you like to find?\n"
                    "a) Find by Date\n"
                    "b) Find by Time spent(minutes)\n"
                    "c) Find by Exact\n"
                    "d) Find by Pattern\n"
                    "e) Go back to previous menu\n"
                    "> ").lower()

        if find == "a":
            date()
        elif find == "b":
            time()
        elif find == 'c':
            exact()
        elif find == 'd':
            pattern()
        elif find == 'e':
            break
        else:
            print("Sorry, I can only except the letters\n"
                  "'a', 'b', 'c', 'd'\n"
                  "Please try again"
                  )
            continue


def date():
    exact_or_range = input("A) Would you like to find entries by an exact date?\n"
                           "or\n"
                           "B) Find entries by a range of two dates?"
                           ).lower()
    if exact_or_range == "a":
        find_by_date_exact()
    elif exact_or_range == 'b':
        find_by_date_range()




def time():
    ''' THIS FUNCTION TAKES IN A TIME INPUT FROM THE USER
        IT THEN LOOPS THROUGH THE CSV FILE AND CHECKS THE TIME
        COLOUMN FOR A MATCH, IF A MATCH IT MADE
        IT PRINTS IT OUT TO THE USER
    '''

    while True:
        find = input("Please enter a time in minutes(rounded)\n"
                    "> ")

        if len(find) < 1:
            continue
        else:
            break

    print("Matches will appear below\n"
          "If no matches were made\n"
          "You will return back to the previous menu.\n"
          "")

    count = -1

    with open("work_log1.csv", 'r') as fp:
        reader = csv.DictReader(fp, delimiter=',')
        for row in reader:
            count+=1
            if find == row["time"]:
                for key, value in row.items():
                    print(key,':',value)

                print("")
                edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
                print("")

                if edit_or_previous == 'e':
                    edit_coloumn = input("What would you like to edit?\n"
                                         "A) Task\n"
                                         "B) Time\n"
                                         "C) Notes\n"
                                         "D) Date").lower()
                    if edit_coloumn == 'a':
                        edit("task", count)
                    elif edit_coloumn == 'b':
                        edit("time", count)
                    elif edit_coloumn == 'c':
                        edit("notes", count)
                    elif edit_coloumn == 'd':
                        edit("date", count)

                elif edit_or_previous == "p":
                    with open("work_log1.csv", 'r') as p:
                        reader = csv.reader(p,delimiter=",")
                        for _, line in enumerate(reader):
                            if _ == count:
                                print("Here is your previous entry:\n"
                                      "")
                                print("task: ",line[0])
                                print("time: ", line[1])
                                print("notes: ", line[2])
                                print("date: ", line[3])
                                print("")
                                keep_going = input("Press Enter to continue").lower()
                                print("")


def exact():
    ''' THIS FUNCTION TAKES IN INPUT FROM THE USER IT THEN LOOPS THROUGH
        THE CSV FILE AND CHECKS THE TASK AND NOTES COLOUMN FOR A MATCH,
        IF A MATCH IT MADE IT PRINTS IT OUT TO THE USER
    '''

    while True:
        find = input("Please enter the exact word you want to find\n"
                     "> ")
        if len(find) < 1:
            continue
        else:
            break

    print("Matches will appear below\n"
          "If no matches were made\n"
          "You will return back to the previous menu.\n"
          "")

    count = -1

    with open("work_log1.csv", 'r') as fp:
        reader = csv.DictReader(fp, delimiter = ',')
        for row in reader:
            count += 1
            if find == row["task"] or find == row["notes"]:
                for key, value in row.items():
                    print(key,":",value)

                print("")
                edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
                print("")

                if edit_or_previous == 'e':
                    edit_coloumn = input("What would you like to edit?\n"
                                         "A) Task\n"
                                         "B) Time\n"
                                         "C) Notes\n"
                                         "D) Date").lower()
                    if edit_coloumn == 'a':
                        edit("task", count)
                    elif edit_coloumn == 'b':
                        edit("time", count)
                    elif edit_coloumn == 'c':
                        edit("notes", count)
                    elif edit_coloumn == 'd':
                        edit("date", count)

                elif edit_or_previous == "p":
                    with open("work_log1.csv", 'r') as p:
                        reader = csv.reader(p, delimiter=",")
                        for _, line in enumerate(reader):
                            if _ == count:
                                print("Here is your previous entry:\n"
                                      "")
                                print("task: ", line[0])
                                print("time: ", line[1])
                                print("notes: ", line[2])
                                print("date: ", line[3])
                                print("")
                                keep_going = input("Press Enter to continue").lower()
                                print("")


def pattern():
    ''' THIS FUNCTION TAKES IN A REGEX PATTERN FROM THE USER
        IT THEN LOOPS THROUGH THE CSV FILE AND CHECKS THE TASK
        AND NOTES COLOUMN FOR A MATCH, IF A MATCH IT MADE
        IT PRINTS IT OUT TO THE USER'''

    while True:
        find = input("please enter your Regex pattern\n"
                     "> ")
        if len(find) < 1:
            continue
        else:
            break

    print("Matches will appear below\n"
          "If no matches were made\n"
          "You will return back to the previous menu.\n"
          "")
    count = -1
    with open("work_log1.csv", 'r') as fp:
        reader = csv.DictReader(fp, delimiter=',')
        for row in reader:
            count +=1
            if re.findall(r"{}".format(find), row["task"]) or re.findall(r"{}".format(find), row["notes"]):
                for key, value in row.items():
                    print(key,':',value)

                print("")
                edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
                print("")

                if edit_or_previous == 'e':
                    edit_coloumn = input("What would you like to edit?\n"
                                         "A) Task\n"
                                         "B) Time\n"
                                         "C) Notes\n"
                                         "D) Date").lower()
                    if edit_coloumn == 'a':
                        edit("task", count)
                    elif edit_coloumn == 'b':
                        edit("time", count)
                    elif edit_coloumn == 'c':
                        edit("notes", count)
                    elif edit_coloumn == 'd':
                        edit("date", count)

                elif edit_or_previous == "p":
                    with open("work_log1.csv", 'r') as p:
                        reader = csv.reader(p, delimiter=",")
                        for _, line in enumerate(reader):
                            if _ == count:
                                print("Here is your previous entry:\n"
                                      "")
                                print("task: ", line[0])
                                print("time: ", line[1])
                                print("notes: ", line[2])
                                print("date: ", line[3])
                                print("")
                                keep_going = input("Press Enter to continue").lower()
                                print("")



'''THIS IS THE MAIN BODY, IT PROMPTS THE USER FOR INPUT,
   WHATEVER THE INPUT IS, DECIDES WHICH FUNCTIONS ABOVE,
   WILL RUN.'''

filename = "work_log1.csv"
file_exists = os.path.isfile((filename))

with open("work_log1.csv", 'a') as fp:
    fieldnames = ["task", "time", "notes", "date"]
    writer = csv.DictWriter(fp, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()

while True:
    choice = input("Hi Welcome. What would you like to do\n"
                    "a) Add a new log\n"
                    "b) Look up a previous log\n"
                    "c) Quit the Database\n"
                    "> ").lower()

    if not len(choice) == 1:
        print("Sorry please answer 'a' or 'b' only.")
    else:
        if choice == 'a':
            add()
        elif choice == 'b':
            lookup()
        elif choice == 'c':
            sys.exit("Goodbye")

