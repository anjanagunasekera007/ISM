import csv
from Item_Class import Item

Q1sales = []
Q2sales = []
Q3sales = []
Q4sales = []

def transactionlistcreator1():
    with open('./datasets/Q1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            print transaction
            print type(transaction)

def transactionlistcreator2():
    with open('./datasets/Q2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            print transaction
            print type(transaction)


def transactionlistcreator3():
    with open('./datasets/Q3.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            print transaction
            print type(transaction)



def transactionlistcreator4():
    with open('./datasets/Q4.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            print transaction
            print type(transaction)



transactionlistcreator()