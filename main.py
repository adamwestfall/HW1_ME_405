"""! 
@main.py
This file contains the code to run plot a csv file according 
to assignment 1 of ME-405

@authors    Adam Westfall
@date       23-Jan-2023
"""
from matplotlib import pyplot 

def read_csv(filename):
    """
    Read integers from a Comma-Separated Value file.
    TODO: Complete this function.
    :param filename: An existing CSV's filename
    :return: A list of rows from the CSV, where each row is a dictionary
             mapping column names to cell values
    """
    data = {}
    with open(filename, 'r') as csv_file:
        first_line = csv_file.readline()
        first_line = first_line.strip()
        titles = first_line.split(',')
        
        for i in titles:
            data[i] = []
        for line in csv_file:
            row = line.strip()
            values = row.split(',')
            print(values)
            if len(values) == len(titles):
                for i in range(len(values)):
                    data[titles[i]].append(values(i))
    
    return data


if __name__ == '__main__':
    data = read_csv('data.csv')
    print(data.keys())
