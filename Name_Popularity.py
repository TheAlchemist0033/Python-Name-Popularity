'''
*@file Name Popularity.py
*@brief Compares popularity of two names and prints the total sum of their frequencies
* and also figures out maximum popularity of a name and prints out associated year and frequency
*
*@author Tina Kordahi
*@date February 10, 2021
*@date revised October 23, 2023
*@bug None
*
'''

import csv


print("Welcome to the baby name analyzer!")
repeat = "yes"

while repeat == "yes":
  answer = input("What would you like to run (name comparison/maximum popularity)?: ").lower()

#NAME COMPARISON
  if answer == "name comparison":
    first = input("Enter the first name to analyze: ")
    second = input("Enter the second name to analyze: ")
    first_sum = 0
    second_sum = 0

#opening file and summing values associated with names
    with open("usa_baby_names.csv", "r") as file:
      for row in csv.reader(file):
        if row[1] == first:
          first_sum += int(row[4])


        if row[1] == second:
          second_sum += int(row[4])

#printing out name comparison totals
      if first_sum >= second_sum:
        print(first, "was more popular than", second,"(", first_sum, "to", second_sum, ")")

      else:
        print(second, "was more popular than", first,"(", second_sum, "to", first_sum, ")")

    repeat = input("Would you like to run another analysis (yes/no)?: ").lower()

#repeat error checking
    if repeat != "yes" and repeat != "no":
      print("Invalid response, try again!")
      repeat = "yes"

#MAXIMUM POPULARITY
  elif answer == "maximum popularity":
    name = input("Enter the name to analyze: ")
    freq = []
    year = []

#opening files and appending frequency and year values to lists for freq and year
    with open("usa_baby_names.csv", "r") as file:
      for row in csv.reader(file):
        if row[1] == name:
          freq.append(int(row[4]))
          year.append(row[2])

#finding max frequency and index of that max to find the associated year with that max
    maxf = max(freq)
    index = freq.index(maxf)

    print(name, "was most popular in", year[index], "with a frequency of", maxf)

    repeat = input("Would you like to run another analysis (yes/no)?: ").lower()

#repeat error checking
    if repeat != "yes" and repeat != "no":
      print("Invalid response, try again!")
      repeat = "yes"

#ANALYSIS ERROR CHECKING
  else:
    print("Sorry, that type of analysis is not supported.")
    repeat = input("Would you like to run another analysis (yes/no)?: ").lower()

#repeat error checking
    if repeat != "yes" and repeat != "no":
      print("Invalid response, try again!")
      repeat = "yes"

print("Goodbye!")
