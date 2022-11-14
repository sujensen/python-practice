"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
Inputs: a list of data about a phone call: sending number, receiving number, time, and duration

Output: the total duration (summed over the whole list) for each phone number.
"""

def phone_dict(file_list):
    ret_dict = {}
    for record in file_list:
        phone_a = record[0]
        phone_b = record[1]
        duration = int(record[3])

        # compute for the sending number
        if phone_a not in ret_dict:
            ret_dict[phone_a] = 0
        ret_dict[phone_a] += duration
	# compute for the receiving number
        if phone_b not in ret_dict:
            ret_dict[phone_b] = 0
        ret_dict[phone_b] += duration
    return ret_dict

def test():
    from datetime import datetime
    phony_calls = [["a","b",datetime.now(),10],["a","c",datetime.now(),25],["b","d",datetime.now(),7]]
    phony_numbers = phone_dict(phony_calls)
    assert len(phony_numbers) == 4
    assert phony_numbers["a"] == 35
    assert phony_numbers["b"] == 17
    assert phony_numbers["c"] == 25
    assert phony_numbers["d"] == 7    

#test()

my_result = phone_dict(calls)
total_time = max(my_result.values())
biggest_phone_user = max(my_result, key=my_result.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(biggest_phone_user, total_time))
 

