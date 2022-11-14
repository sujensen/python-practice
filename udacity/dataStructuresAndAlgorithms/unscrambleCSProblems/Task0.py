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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
What are the inputs?  The user input is an integer representing the record number of a file
(or index of a list)

What are the outputs?  The output is the data from that record of the file.  We could format
the output as a list, and use the same algorithm for both the calls and texts data. 
"""

# Define some constant strings
bad_filename = "Not a valid file name.  Please choose either 'texts' or 'files'."
bad_input = "Not a valid record number. Please choose an integer between 0 and {}."

# Algorithm for use in both parts of this task
def read_record(k, file):

    # check user input: file should be calls or texts
    if file != "calls" and file != "texts":
        return bad_filename

    # k should be an integer, within the range of the size of the file
    if file == "texts":
        total_records = len(texts)
    else:
        total_records = len(calls)
    if k < 0 or k >= total_records:
        return bad_input.format(total_records - 1)

    # User input looks okay; get the data
    if file == "texts":
        record = texts[k]
    else:
        record = calls[k]
    return record

# Some tests
def test():
    
    # Test the user input filename
    result00 = read_record(0, "imessages")
    assert result00 == bad_filename
    # Test the value of k
    result0 = read_record(-1, "texts")
    assert result0 == bad_input.format(len(texts) - 1)
    # Test a good result 
    result1 = read_record(4, "texts")
    result1_string = ",".join(result1)
    assert result1_string == "81515 42171,98440 02823,01-09-2016 06:13:30"
    # Test a good result for calls
    result2 = read_record(len(calls) - 1, "calls")
    result2_string = ",".join(result2)
    assert result2_string == "98447 62998,(080)46304537,30-09-2016 23:57:15,2151"

# Run the tests
#test()
 
# Get the final output strings
first_text = read_record(0, "texts")
print("First record of texts, {} texts {} at time {}".format(first_text[0], first_text[1], first_text[2]))
last_call = read_record(len(calls) - 1, "calls")
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call[0], last_call[1], last_call[2], last_call[3]))

