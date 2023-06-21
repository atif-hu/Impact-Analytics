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
