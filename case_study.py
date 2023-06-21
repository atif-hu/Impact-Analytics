'''
Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773
'''

def calculate_attendance_probability(days):
    if days < 4:
        return str(2 ** (days - 1)) + '/' + str(2 ** days)
    
    one_day_absent = 2 
    two_day_absent = 1 
    three_day_absent = 1 
    present_cases= 4  
    total_count = 8  
    day=4
    while(day<=days):
        temp_valid_cases = three_day_absent
        three_day_absent = two_day_absent
        two_day_absent = one_day_absent
        one_day_absent = present_cases
        present_cases=total_count
        total_count = (total_count - temp_valid_cases) * 2 + temp_valid_cases
        day+=1

    return str(one_day_absent+two_day_absent+three_day_absent) + '/' + str(total_count)

print(calculate_attendance_probability(5))  # Output: 14/29
print(calculate_attendance_probability(10))  # Output: 372/773