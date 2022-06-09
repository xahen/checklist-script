#checklist app, oliver borg 2022

#things i want to do:
"""
convert the checklist from a simple stored list to a class instead, as i want to create the checklist as an object
that would allow me to store data about the checklist in the pickle module, instead of just storing a plain checklist as a list
i could store data like: the date of the checklist, if it's finished or not, how many items are left unfinished etc.

also: research more about the pickle module, as i don't know much
"""

#from logging import NullHandler
#import sys
import pickle
from os.path import exists as file_exists
from os import listdir
from datetime import datetime


class ChecklistSlate:
    def __init__(self):
        self.checklist = []
        self.date = currentTime.strftime("%d-%m-%Y")
        self.day_number = currentTime.strftime("%d")
        self.month_number = currentTime.strftime("%m")
        self.year = currentTime.strftime("%Y")
        self.weekday = currentTime.strftime("%A")
        self.month = currentTime.strftime("%B")
        self.time_formatted = f"{self.weekday}, {self.month} {self.day_number}"
        self.items_total = 0
        self.items_checked = 0
        self.items_not_checked = 0
        self.times_viewed = 0
        self.is_finished = False
        self.save_name = f"{self.year}_{self.month_number}_{self.day_number}_checklist.dat"

    def itemAdded(self, number:int):
        self.items_total += number
        self.items_not_checked += number
    
    def itemChecked(self):
        self.items_checked += 1
        self.items_not_checked -= 1
    
    def finishList(self):
        self.is_finished = True
    
    def checkState(self):
        if self.items_checked >= self.items_total and self.items_total != 0:
            self.finishList()

    def viewChecklist(self):
        print(f"\nyour to-do checklist for {self.time_formatted} is:")
        if len(self.checklist) > 0:
            print()

            for i in self.checklist:
                if i.times_checked > 0:
                    emptySpaces = i.check_number - i.times_checked
                    checkMarkFormat = ""
                    if i.times_checked > 0:
                        checkMarkFormat = f" {checkMark}" * i.times_checked
                    if emptySpaces > 0:
                        checkMarkFormat = checkMarkFormat + (" __" * (emptySpaces))
                    print(f"{i.number} - {i.name}{checkMarkFormat}")
                else:
                    underScore = " __" * i.check_number
                    print(f"{i.number} - {i.name}{underScore}")
        
            self.times_viewed += 1
        else:
            print("\nEMPTY")

class ChecklistItem:
    def __init__(self, name, number, check_number):
        self.name = name
        self.is_checked = False
        self.number = number
        self.check_number = check_number
        self.times_checked = 0

    def checkItem(self):
        self.times_checked += 1
        if self.times_checked >= self.check_number:
            self.is_checked = True
        



def addItem():
    print("\nwhat do you want to add to your checklist? separate your objectives with '//' and add 'CM=' at the end to specify how many marks need to be checked (default is 1)\n")
    addChoice = str(input())
    split_list = addChoice.split('//')
    
    x = len(mainCL)
    y = x + 1
    
    for i in split_list:
        if "CM=" in i:
            z = i.index("CM=")
            a = z + 3
            markNumber = i[a:]
            i = i[:z]

            try:
                markNumber = int(markNumber)
            except ValueError:
                print("failed input. 'CM=' has to be at the end of the item and has to be followed by numbers only (example: CM=2)")
                return None

            if isinstance(markNumber, int):
                mainCL.append(ChecklistItem(i, y, markNumber))
                x += 1
                y += 1
        
        else:
            mainCL.append(ChecklistItem(i, y, 1))
            x += 1
            y += 1
    
    currentChecklist.itemAdded(len(split_list))

def removeItem():
    print("\nwhat do you want to remove from your checklist?")

    currentChecklist.viewChecklist()
    
    removeChoice = input()

    try:
        removeChoice = int(removeChoice)
    except ValueError:
        print("failed input, please enter a number")

    if isinstance(removeChoice, int):
        removeChoice -= 1

        del mainCL[removeChoice]

def checkItem():
    print("\nwhich item would you like to check off as finished?")
    
    currentChecklist.viewChecklist()

    print()

    checkChoice = input()
    print()

    try:
        checkChoice = int(checkChoice)
    except ValueError:
        print("failed input, please enter a number")

    if isinstance(checkChoice, int):
        checkChoice -= 1

        if not mainCL[checkChoice].is_checked:
            mainCL[checkChoice].checkItem()
            currentChecklist.itemChecked()
        else:
            print("that item has already been checked")


def saveChecklist():
    if file_exists(f"saves\{currentChecklist.year}\{currentChecklist.month_number} {currentChecklist.month}\{currentChecklist.save_name}"):
        saveChoice = str(input("\nthis file already exists, are you sure you want to overwrite it? y/n\n\n")).lower()
        if saveChoice == "y":
            pickle.dump(currentChecklist, open(f"saves\{currentChecklist.year}\{currentChecklist.month_number} {currentChecklist.month}\{currentChecklist.save_name}", "wb"))
            print("\nchecklist saved\n")
        elif saveChoice == "n":
            print("\nchecklist not saved\n")
        else:
            print("\nfalse input\n")
    else:
        pickle.dump(currentChecklist, open(f"saves\{currentChecklist.year}\{currentChecklist.month_number} {currentChecklist.month}\{currentChecklist.save_name}", "wb"))
        print()


def loadChecklist(file, startup):
    print()
    if startup:
        return pickle.load(open(file, "rb"))
    else:
        x = 1

        for i in listdir("saves"):
            print(f"{x} - {i}")
            x += 1

        yearChoice = input("\nwhich year?\n\n")

        try:
            yearChoice = int(yearChoice)
        except ValueError:
            print("failed input, please enter a number")
            return None

        if isinstance(yearChoice, int):
            if yearChoice > len(listdir("saves")):
                print("\nthat was not an option")
                return None

            y = 1
            print()

            for i in listdir("saves"):
                if y == yearChoice:

                    saveYear = i
                    z = 1

                    for i in listdir(f"saves\{saveYear}"):
                        print(f"{z} - {i}")
                        z += 1

                    monthChoice = input("\nwhich month?\n\n")

                    try:
                        monthChoice = int(monthChoice)
                    except ValueError:
                        print("failed input, please enter a number")
                        return None

                    if isinstance(monthChoice, int):
                        if monthChoice > len(listdir(f"saves\{saveYear}")):
                            print("\nthat was not an option")
                            return None

                        a = 1
                        print()

                        for i in listdir(f"saves\{saveYear}"):
                            if a == monthChoice:

                                saveMonth = i
                                b = 1

                                for i in listdir(f"saves\{saveYear}\{saveMonth}"):
                                    fileName = i.replace("_checklist.dat", "")
                                    print(f"{b} - {fileName}")
                                    b += 1
                                
                                dayChoice = input("\nwhich checklist would you like to load?\n\n")

                                try:
                                    dayChoice = int(dayChoice)
                                except ValueError:
                                    print("failed input, please enter a number")
                                    return None
                                
                                if isinstance(dayChoice, int):
                                    if dayChoice > len(listdir(f"saves\{saveYear}\{saveMonth}")):
                                        print("\nthat was not an option")
                                        return None

                                    c = 1

                                    for i in listdir(f"saves\{saveYear}\{saveMonth}"):
                                        if c == dayChoice:
                                            return pickle.load(open(f"saves\{saveYear}\{saveMonth}\{i}", "rb"))
                                        else:
                                            c += 1       

                                else:
                                    a += 1                
                else:
                    y += 1

        

checkMark = "✓"
currentTime = datetime.now()
#saveDate = datetime.now().strftime("%Y_%m_%d")
#saveName = datetime.now().strftime(f"{saveDate}_checklist.dat")
currentChecklist = ChecklistSlate()
#fileLoaded = False


mainCL = currentChecklist.checklist

print("checklist app\n")


while True:

    print("what do you want to do to your checklist?\noptions: 'add' item(s), 'remove' item(s), 'check' off an item, 'view' the list, 'load' a checklist\n")
    checklistChoice = str(input()).lower()

    if checklistChoice == 'add':
        addItem()

    elif checklistChoice == 'remove' or checklistChoice == 'rmv':
        removeItem()

    elif checklistChoice == "check":
        checkItem()

    elif checklistChoice == "view":
        currentChecklist.viewChecklist()

    elif checklistChoice == "load":
        currentChecklist = loadChecklist("", False)

    elif checklistChoice == "exit" or checklistChoice == "quit" or checklistChoice == "q":
        print()
        if len(mainCL) > 0:
            quitChoice = str(input("exiting... would you like to save your current checklist? y/n\n\n")).lower()

            if quitChoice == "y":
                saveChecklist()
                break

            elif quitChoice == "n":
                print("\nchecklist not saved\n")
                break
            else:
                print("\nfalse input")
        
        else:
            print("exiting...\n")
            break

    else:
        print("\nfalse input")
    
    print()


#saveChecklist()

