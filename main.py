"""! 
@main.py
This file contains the code to run plot a csv file according 
to assignment 1 of ME-405

@authors    Adam Westfall
@date       23-Jan-2023
"""
from matplotlib import pyplot 

def check_numeric(lst):
    """
    check if all values in a list of strings are numeric
    TODO: Complete this function.

    :param lst: An existing CSV's filename
    :return: true or false if the values are numeric
    """
    for item in lst:
        try:
            float(item)
        except ValueError:
            return False
    return True

def read_csv(filename):
    """
    Read integers from a Comma-Separated Value file. Rejecting data that is not in the correct format.
    TODO: Complete this function.
    :param filename: An existing CSV's filename
    :return:    A dictionary with the headers of the csv as the keys and the values as
                the elements in a list.
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
            if len(values) == len(titles) and check_numeric(values):
                for i in range(len(values)):
                    data[titles[i]].append(float(values[i]))
    
    return data


if __name__ == '__main__':
    data = read_csv('data.csv')
    keys = list(data.keys())
    # pyplot is used to show the data with correct axis titles
    pyplot.plot(data[keys[0]],data[keys[1]])
    pyplot.xlabel(keys[0])
    pyplot.ylabel(keys[1])
    pyplot.show()
    