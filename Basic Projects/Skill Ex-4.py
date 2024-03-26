'''
#Ex-4-1

import random
import string

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

def generate_random_alphabetical_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for _ in range(length))

def generate_random_between(start, end):
    random_num = random.randint(start, end)
    return random_num

def generate_random_multiple_of_seven():
    multiple_of_seven = random.randint(0, 10) * 7
    return multiple_of_seven

random_color = generate_random_color()
random_string = generate_random_alphabetical_string(8)
random_between = generate_random_between(50, 100)
random_multiple_of_seven = generate_random_multiple_of_seven()


print("Random Color Hex:", random_color)
print("Random Alphabetical String:", random_string)
print("Random Value between 50 and 100:", random_between)
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_seven)


#Ex-4-2

import random
from datetime import datetime, timedelta

def generate_random_excluding_six():
    random_num = random.randint(0, 5)
    return random_num

def generate_random_between_five_and_ten():
    random_num = random.randint(5, 9)
    return random_num

def generate_random_step_of_three():
    random_num = random.randrange(0, 10, 3)
    return random_num

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

random_num_excluding_six = generate_random_excluding_six()
random_num_between_five_and_ten = generate_random_between_five_and_ten()
random_num_step_of_three = generate_random_step_of_three()

start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
random_date = generate_random_date(start_date, end_date)

print("Random integer between 0 and 6 (excluding 6):", random_num_excluding_six)
print("Random integer between 5 and 10 (excluding 10):", random_num_between_five_and_ten)
print("Random integer between 0 and 10 with a step of 3:", random_num_step_of_three)
print("Random date between 2022-01-01 and 2023-12-31:", random_date.strftime("%Y-%m-%d"))


'''

# Ex-4-3






