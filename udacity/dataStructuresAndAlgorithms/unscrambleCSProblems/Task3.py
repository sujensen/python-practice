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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Part A:

Input: a call record.

Output: the area code or the mobile code of the receiving number, if the sending number was a fixed line in Bangalore.
"""

# Given a phone number, is this mobile, fixed, telemarketer, or unknown
def type_of_number(number):
    if number[0] == "(":
        number_type = "fixed"
    elif " " in number:
        number_type = "mobile"
    elif number.startswith("140"):
        number_type = "telemarketer"
    else:
        number_type = "unknown"    
    return number_type
    
# Given a phone number, return the type ("mobile", "fixed", or "telemarketer") and the code (either mobile code or area code or telemarketer code)
def number_data(number):
    number_type = type_of_number(number)
    ret_data = dict()
    ret_data["type"] = number_type
    if number_type == "fixed":
        ret_data["code"] = number[1:number.find(")")]
    elif number_type == "mobile":
        ret_data["code"] = number[0:4]
    elif number_type == "telemarketer":
        ret_data["code"] = "140"
    return ret_data    

# Given a record, return the called code, if the sending number was a fixed line from Bangalore
def code_called_from_bangalore(record):
    ret_code = "None"
    sending_number = record[0]
    receiving_number = record[1]
    # if sending number is fixed line from Bangalore
    sending_number_data = number_data(sending_number)
    if sending_number_data["type"] == "fixed" and sending_number_data["code"] == "080":
        # then return code of receiving number
        receiving_number_data = number_data(receiving_number)
        ret_code = receiving_number_data["code"]
    return ret_code

# Analyze all the call records, return the lexicographic set that is desired
def part_a_analysis(file):
    # set of receiving number codes, if sending number was fixed line in Bangalore
    my_set = set()
    for record in file:
        code_called = code_called_from_bangalore(record)
        if (code_called != "None"):
            my_set.add(code_called)
    my_sorted_list = sorted(list(my_set))
    return my_sorted_list

def test_part_a():
    assert type_of_number("(080)33251027") == "fixed"
    assert type_of_number("90192 87313") == "mobile"
    assert type_of_number("1400481538") == "telemarketer"
    
    data_1 = number_data("(080)33251027")
    assert data_1["type"] == "fixed"
    assert data_1["code"] == "080"
    data_2 = number_data("90192 87313")
    assert data_2["type"] == "mobile"
    assert data_2["code"] == "9019"
    data_3 = number_data("1400481538")
    assert data_3["type"] == "telemarketer"
    assert data_3["code"] == "140"

    assert code_called_from_bangalore("(080)35538852,98446 78140,29-09-2016 17:42:07,604".split(",")) == "9844"
    assert code_called_from_bangalore("1402316533,90357 17994,30-09-2016 18:28:42,62".split(",")) == "None"

    test_file = list()
    test_file.append("(080)35538852,98446 78140,29-09-2016 17:42:07,604".split(","))
    test_file.append("(022)34715405,97448 02140,30-09-2016 18:51:47,66".split(","))
    test_file.append("(080)68739140,97406 74488,29-09-2016 10:23:27,1917".split(","))
    test_file.append("98446 78140,(080)35538852,30-09-2016 19:05:27,655".split(","))
    test_file.append("(080)68739123,97401 12345,29-09-2016 10:23:27,1917".split(","))
    assert part_a_analysis(test_file) == ['9740', '9844']
    print("end of test for part A")



#test_part_a()

part_a_result = part_a_analysis(calls)
print("The numbers called by people in Bangalore have codes:")
for num in part_a_result:
    print(num)


# Analyze all the call records, return the percentage of "from fixed Bangalore" that is "to fixed Bangalore"
def part_b_analysis(file):

    # numerator is the count of fixed calls from Bangalore to fixed number in Bangalore
    my_numerator = 0
    # denominator is the count of all fixed calls from Bangalore
    my_denominator = 0

    for record in file:
        sending_number = record[0]
        sending_number_data = number_data(sending_number)
        if sending_number_data["type"] == "fixed" and sending_number_data["code"] == "080":
            my_denominator += 1
            receiving_number = record[1]
            receiving_number_data = number_data(receiving_number)      
            if receiving_number_data["type"] == "fixed" and receiving_number_data["code"] == "080":
                my_numerator += 1
    return dict(zip(['numerator', 'denominator'], [my_numerator, my_denominator]))

def test_part_b():
    test_file = list()
    test_file.append("(080)35538852,98446 78140,29-09-2016 17:42:07,604".split(","))
    test_file.append("(022)34715405,97448 02140,30-09-2016 18:51:47,66".split(","))
    test_file.append("(080)68739140,97406 74488,29-09-2016 10:23:27,1917".split(","))
    test_file.append("(080)68739140,(080)68712345,29-09-2016 10:23:27,1917".split(","))
    test_file.append("98446 78140,(080)35538852,30-09-2016 19:05:27,655".split(","))
    test_file.append("(080)68739123,97401 12345,29-09-2016 10:23:27,1917".split(","))
    test_results = part_b_analysis(test_file)
    assert test_results["numerator"] == 1
    assert test_results["denominator"] == 4
    print("end of test for part B")

#test_part_b()

part_b_result = part_b_analysis(calls)
perc_string = "%.2f" % ((part_b_result["numerator"] / part_b_result["denominator"]) * 100)
print(perc_string, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.") 


