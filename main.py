# 🚨 The idea is to create a program using maths and f-Strings
# that tells us how many days, weeks, months we have left if we live
# until 90 years old.

actual_age = input("What is your current age? \n")

death_age = input("How old do you want to live? \n")

years_remaining = int(death_age) - int(actual_age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"\nYou have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
