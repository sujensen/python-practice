"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Inputs: file of records (the first two columns in each file are phone numbers).

Output: set of phone numbers
"""

def phone_number_set(file_list):
    # return a set of phone numbers, from the union of the sending and receiving numbers
    unzipd_list = list(zip(*file_list))
    sending_number = set(unzipd_list[0])
    receiving_number = set(unzipd_list[1])
    ret_set = sending_number | receiving_number
    return ret_set

def test():
    
    t_1 = [["a","d"],["b","e"],["c","c"]]
    t_1_result = phone_number_set(t_1)
    assert len(t_1_result) == 5

    t_2 = [["a","c",0,1],["b","a",39,41],["b","a","foo","bar"]]
    t_2_result = phone_number_set(t_2)
    assert len(t_2_result) == 3

#test()
texts_result = phone_number_set(texts)
calls_result = phone_number_set(calls)
total_result = texts_result | calls_result
print("There are {} different telephone numbers in the records.".format(len(total_result))) 
    


