from sys import argv,exit
import csv

def main():
    csv_path = argv[1]
    with open(csv_path) as csv_file:
        reader=csv.reader(csv.file)
        for row in reader:
            print(row)