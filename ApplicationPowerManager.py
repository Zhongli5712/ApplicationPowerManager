
"""
This code was written by: Truong Minh Duong
"""
import pandas as pd
import ctypes
from time import sleep
from ctypes import *
import csv

def init():
    try:
        ipdDll = cdll.LoadLibrary("./EnergyLib64.dll")

        ipdDll.IntelEnergyLibInitialize()

        return ipdDll
    except FileNotFoundError as we:
        print("Missing EnergyLib64.dll file. Please download it again, you may refer to the release in Readme.md")
        quit()

def generate_report(ipdDll, csv_path): 

    ipdDll.StartLog(csv_path);


    for i in range(15):
        sleep(1)
        ipdDll.ReadSample()
    
    sleep(1)
    ipdDll.StopLog()

def main():
    print("Please wait a moment...")
    ipdDll = init()
    generate_report(ipdDll, './PowerGadgetLogBefore.csv')
    pre_avg_pp = 0.0

    try: 
        with open('PowerGadgetLogBefore.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                length = len(row)
                if (length == 6 and row[0] == 'Average' and row[1] == 'Processor'): pre_avg_pp = float(row[5])
    except IOError:
        print("IOError, the PowerGadgetLogBefore.csv file may not exist, please try again")
        quit()
    if pre_avg_pp == 0.0:
        print("PowerGadgetLogBefore.csv may not be properly loaded, or there is some error in the application, as the current power usage is 0. Please try again.")
    
    print("Now run the application you want to measure the power usage.")
    is_running = 'no'
    while (is_running != 'yes'):
        is_running = input("Have you run it? (yes/no)")
    print("Got it, please wait a moment while we calculate the result...")

    generate_report(ipdDll, './PowerGadgetLogAfter.csv')
    post_avg_pp = 0.0
    try:
        with open('PowerGadgetLogAfter.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                length = len(row)
                if (length == 6 and row[0] == 'Average' and row[1] == 'Processor'): post_avg_pp = float(row[5])
    except IOError:
        print("IOError, the PowerGadgetLogAfter.csv file may not exist, please try again")
        quit()

    if post_avg_pp == 0.0:
        print("PowerGadgetLogAfter.csv may not be properly loaded, or there is some error in the application, as the current power usage is 0. Please try again.")
    
    if post_avg_pp <= pre_avg_pp:
        print("The estimation of power usage is 0. Either the amount of power usage is too small or there is some error. You can try again")
    else:
        print(f"The estimation of power usage is: {post_avg_pp - pre_avg_pp} Watt")

if __name__ == "__main__":
    main()


