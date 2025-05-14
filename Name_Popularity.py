'''
*@file Name Popularity.py
*@brief Fetches up-to-date name information from SSA.gov to compare popularity of two names and print the total sum of their frequencies.
* Also figures out maximum popularity of a name and prints out associated year and frequency.
*
*@author Chandler Lyon
*@OriginalAuthor Tina Kordahi
*@date February 10, 2021
*@date revised May 14, 2025
*@bug None
*
'''
import csv
import io
import zipfile
import urllib.request

print("Welcome to the baby name analyzer!")

# Download and read SSA baby names data
def get_baby_name_data():
    url = "https://www.ssa.gov/oact/babynames/names.zip"
    print("Getting up-to-date records on baby names from 1880 to current.");
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.ssa.gov/oact/babynames/",
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        with zipfile.ZipFile(io.BytesIO(response.read())) as z:
            data = []
            for filename in z.namelist():
                if filename.startswith("yob") and filename.endswith(".txt"):
                    year = filename[3:7]
                    with z.open(filename) as f:
                        for row in csv.reader(io.TextIOWrapper(f)):
                            data.append((
                              row[0].lower(),# name lowercased
                              year,# year of data
                              row[1].lower(),# gender data 
                              int(row[2]) # frequency
                            ));
            return data

baby_data = get_baby_name_data()

repeat = "yes"
while repeat == "yes":
  try:
    answer = int(input("What would you like to run?\n1: name comparison\n2: maximum popularity\n "))

    if answer == 1:
        first = input("Enter the first name to analyze: ").lower()
        second = input("Enter the second name to analyze: ").lower()
        first_sum = sum(row[3] for row in baby_data if row[0] == first)
        second_sum = sum(row[3] for row in baby_data if row[0] == second)

        if first_sum >= second_sum:
            print(f"{first} was more popular than {second} ({first_sum} to {second_sum})")
        else:
            print(f"{second} was more popular than {first} ({second_sum} to {first_sum})")

    elif answer == 2:
        name = input("Enter the name to analyze: ").lower()
        name_data = [(row[1], row[3]) for row in baby_data if row[0] == name]
        if not name_data:
            print("Name not found.")
        else:
            year, maxf = max(name_data, key=lambda x: x[1])
            print(f"{name} was most popular in {year} with a frequency of {maxf}")
    else:
        print("Thats not a valid option, please enter 1 for name comparison or 2 for maximum popularity.")

    repeat = input("Would you like to run another analysis (yes/no)?: ").lower()
    if repeat not in ["yes", "no"]:
        print("Invalid response, try again!")
        repeat = "yes"
    
  except ValueError:
    print("Sorry, thats not a valid option, please enter 1 for name comparison or 2 for maximum popularity.")
       


print("Goodbye!")
