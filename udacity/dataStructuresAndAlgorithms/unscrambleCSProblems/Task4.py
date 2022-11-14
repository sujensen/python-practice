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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Input: records of calls and texts

Output: set of numbers that make outgoing calls, but never receive calls or send or receive texts
"""

def find_possible_telemarketers(calls, texts):
    # The most straightforward algorithm that I can think of is to compare sets of phone numbers.
    unzip_calls = list(zip(*calls))
    unzip_texts = list(zip(*texts))
    outgoing_call_numbers = set(unzip_calls[0])
    receiving_call_numbers = set(unzip_calls[1])
    outgoing_text_numbers = set(unzip_texts[0])
    receiving_text_numbers = set(unzip_texts[1])
    possible_telemarketers = outgoing_call_numbers.difference(receiving_call_numbers, outgoing_text_numbers, receiving_text_numbers)
    return sorted(list(possible_telemarketers))

def test():
    # Four phone calls
    test_calls = ["78130 00821,98453 94494,01-09-2016 06:01:12,186".split(","), 
    "78298 91466,(022)28952819,01-09-2016 06:01:59,2093".split(","), 
    "97424 22395,(022)47410783,01-09-2016 06:03:51,1975".split(","), 
    "93427 40118,(080)33118033,01-09-2016 06:11:23,1156".split(",")]
    # Three text messages (same phone numbers as the last three phone call records)
    test_texts = test_calls[1:len(test_calls)]
    
    # Only the first outgoing phone number could be a telemarketer
    results = find_possible_telemarketers(test_calls, test_texts)
    assert len(results) == 1
    assert results[0] == "78130 00821"
    print("test is over")


#test()

result_list = find_possible_telemarketers(calls, texts)
print("These numbers could be telemarketers: ")
for num in result_list:
    print(num)

