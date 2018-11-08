import csv, os, sys, datetime, re
import pandas as pd


def clear():
    ''' THIS FUNCTION CLEARS THE SCREEN'''

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def edit_to_csv(a, b, c, d):
    ''' THIS IS MY FUNCTION THAT LOOPS THROUGH THE LIST THAT WAS CREATED
        I.E "DATE_LIST", IT RUNS THE EDIT() FUNCTION TO EDIT THE CSV FILE'''

    csv_in = -1
    with open("work_log1.csv", 'r') as fp:
        next(fp)
        reader = csv.reader(fp, delimiter=',')
        for row in reader:
            csv_in += 1
            if row == a:
                print(csv_in)

                if b == 'a':
                    alpha = d[c][0] = input("task: ")
                    print(csv_in)
                    edit("task", csv_in, alpha)
                elif b == 'b':
                    beta = d[c][1] = input("time: ")
                    edit("time", csv_in, beta)
                elif b == 'c':
                    charlie = d[c][2] = input("notes: ")
                    edit("notes", csv_in, charlie)
                elif b == 'd':
                    delta = d[c][3] = input("dates: ")
                    edit("date", csv_in, delta)


def previous(d, c):
    ''' THIS FUNCTION IS RAN IN MANY OTHER FUNCTIONS,
        IT LOOPS THROUGH THE "DATE_LIST" LIST,
        AND ALLOWS THE USER TO CHECK ON A PREVIOUS INPUT
    '''

    header = ['task: ', 'time: ', 'notes: ', 'date: ']
    print(header[0], d[c - 1][0])
    print(header[1], d[c - 1][1])
    print(header[2], d[c - 1][2])
    print(header[3], d[c - 1][3])
    print("")
    cont = input("This is your previous search\n"
                 "Please press Enter")


def find_by_date_range():
    '''THIS FUNCTION TAKES TWO DATE RANGES FROM A USER,
       IT THEN LOOPS THROUGH THE CSV AND IF A MATCH IS MADE,
       IT SHOWS ALL OF THE CSV ROWS THAT ARE WITHIN THE DATE RANGE
    '''

    clear()

    date_entry = input('Enter a date (i.e. 2017,7,1)')
    year, month, day = map(int, date_entry.split(','))
    date1 = datetime.date(year, month, day)

    date_entry = input('Enter a date (i.e. 2017,7,1)')
    year, month, day = map(int, date_entry.split(','))
    date2 = datetime.date(year, month, day)

    delta = date2 - date1
    o = []
    for i in range(delta.days + 1):
        o.append((date1 + datetime.timedelta(i)).strftime('%Y-%m-%d'))

    count = 0
    date_list = []
    with open("work_log1.csv", 'r') as fp:
        next(fp)
        reader = csv.reader(fp, delimiter=',')
        for row in reader:
            for thing in o:
                if thing == row[3]:
                    date_list.append(row)

        for thing in date_list:
            print("task:", thing[0])
            print("time:", thing[1])
            print("notes:", thing[2])
            print("dates:", thing[3])
            print("")

            edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
            if edit_or_previous == 'e':
                edit_coloumn = input("What would you like to edit?\n"
                                     "A) Task\n"
                                     "B) Time\n"
                                     "C) Notes\n"
                                     "D) Date").lower()

                edit_to_csv(thing, edit_coloumn, count, date_list)

            elif edit_or_previous == 'p':
                previous(date_list, count)

            count += 1


def find_by_date_exact():
    '''THIS FUNCTION TAKES AN EXACT DATE FROM A USER,
       IT THEN LOOPS THROUGH THE CSV AND IF A MATCH IS MADE,
       IT SHOWS ALL OF THE CSV ROWS THAT MATCH THAT EXACT DATE
    '''

    clear()
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

    count = 0
    date_list = []
    with open("work_log1.csv", 'r') as fp:
        next(fp)
        reader = csv.reader(fp, delimiter=',')
        for row in reader:
            if find == row[3]:
                date_list.append(row)

        for thing in date_list:
            print("task:", thing[0])
            print("time:", thing[1])
            print("notes:", thing[2])
            print("dates:", thing[3])
            print("")

            edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
            if edit_or_previous == 'e':
                edit_coloumn = input("What would you like to edit?\n"
                                     "A) Task\n"
                                     "B) Time\n"
                                     "C) Notes\n"
                                     "D) Date").lower()

                edit_to_csv(thing, edit_coloumn, count, date_list)

            elif edit_or_previous == 'p':
                previous(date_list, count)

            count += 1


def userstime():
    '''THIS FUNCTION IS RUN DURING THE ADD FUNCTION,
       ONCE THE USER FILLS OUT WHAT THEY WANT ADDED,
       TO THE CSV, THIS FUNCTION RUNS AND CAPTURES,
       THE TIME THEY ENTERED THAT INFORMATION.
    '''

    new_userst = datetime.date.today()
    return new_userst


def edit(x, y, new):
    '''THIS FUNCTION IS RUN DURING OTHER FUNCTIONS,
       IT TAKES AN INPUT OF DATA,
       THEN IT CHANGES THE CSV BASED ON ITS INDEX
       Y = INDEX, X = CHANGE
    '''

    fp = pd.read_csv("work_log1.csv", error_bad_lines=False)
    fp.set_value(y, x, new)
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
    cont = input("Your date has been automatically added, Thank you.\n"
                 "Press ENTER to continue back to the main menu.")
    clear()

    with open("work_log1.csv", 'a', newline='') as fp:
        fieldnames = ["task", "time", "notes", "date"]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writerow({fieldnames[0]: taskname, fieldnames[1]: timetaken,
                         fieldnames[2]: addnotes, fieldnames[3]: userstime()})

    return taskname, timetaken, addnotes


def lookup():
    '''THIS FUNCTION ALLOWS THE USER TO LOOKUP DATA,
       BY TAKING SOME INPUT, E.G, IF THEY WANT TO,
       FIND "DATE", THEN THEY TYPE "A" AND ENTER
    '''

    clear()
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
    '''THIS FUNCTION RUNS MAKES THE USER CHOOSE IF THEY
       WANT TO SEARCH A DATE USING THE EXACT DATE,
       OR BY USING A DATE RANGE
    '''
    clear()
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
    clear()
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

    count = 0
    date_list = []
    with open("work_log1.csv", 'r') as fp:
        next(fp)
        reader = csv.reader(fp, delimiter=',')
        for row in reader:
            if find == row[1]:
                date_list.append(row)

        for thing in date_list:
            print("task:", thing[0])
            print("time:", thing[1])
            print("notes:", thing[2])
            print("dates:", thing[3])
            print("")

            edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
            if edit_or_previous == 'e':
                edit_coloumn = input("What would you like to edit?\n"
                                     "A) Task\n"
                                     "B) Time\n"
                                     "C) Notes\n"
                                     "D) Date").lower()

                edit_to_csv(thing, edit_coloumn, count, date_list)

            elif edit_or_previous == 'p':
                previous(date_list, count)

            count += 1


def exact():
    ''' THIS FUNCTION TAKES IN INPUT FROM THE USER IT THEN LOOPS THROUGH
        THE CSV FILE AND CHECKS THE TASK AND NOTES COLOUMN FOR A MATCH,
        IF A MATCH IT MADE IT PRINTS IT OUT TO THE USER
    '''

    clear()
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

    count = 0
    date_list = []
    with open("work_log1.csv", 'r') as fp:
        next(fp)
        reader = csv.reader(fp, delimiter=',')
        for row in reader:
            if find == row[0] or find == row[2]:
                date_list.append(row)

        for thing in date_list:
            print("task:", thing[0])
            print("time:", thing[1])
            print("notes:", thing[2])
            print("dates:", thing[3])
            print("")

            edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
            if edit_or_previous == 'e':
                edit_coloumn = input("What would you like to edit?\n"
                                     "A) Task\n"
                                     "B) Time\n"
                                     "C) Notes\n"
                                     "D) Date").lower()

                edit_to_csv(thing, edit_coloumn, count, date_list)

            elif edit_or_previous == 'p':
                previous(date_list, count)

            count += 1


def pattern():
    ''' THIS FUNCTION TAKES IN A REGEX PATTERN FROM THE USER
        IT THEN LOOPS THROUGH THE CSV FILE AND CHECKS THE TASK
        AND NOTES COLOUMN FOR A MATCH, IF A MATCH IT MADE
        IT PRINTS IT OUT TO THE USER'''

    clear()
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

    count = 0
    date_list = []
    with open("work_log1.csv", 'r') as fp:
        next(fp)
        reader = csv.reader(fp, delimiter=',')
        for row in reader:
            if re.findall(r"{}".format(find), row[0]) or re.findall(r"{}".format(find), row[2]):
                date_list.append(row)

    for thing in date_list:
        print("task:", thing[0])
        print("time:", thing[1])
        print("notes:", thing[2])
        print("dates:", thing[3])
        print("")

        edit_or_previous = input("[P]revious, [E]dit, Enter for next: ").lower()
        if edit_or_previous == 'e':
            edit_coloumn = input("What would you like to edit?\n"
                                 "A) Task\n"
                                 "B) Time\n"
                                 "C) Notes\n"
                                 "D) Date").lower()

            edit_to_csv(thing, edit_coloumn, count, date_list)

        elif edit_or_previous == 'p':
            previous(date_list, count)

        count += 1


'''THIS IS THE MAIN BODY, IT PROMPTS THE USER FOR INPUT,
   WHATEVER THE INPUT IS, DECIDES WHICH FUNCTIONS ABOVE,
   WILL RUN.'''

filename = "work_log1.csv"
file_exists = os.path.isfile((filename))

with open("work_log1.csv", 'a', newline='') as fp:
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