import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# Lists to store data
Job_Titles = []
Dates = []
Locations = []

# Request page
response = requests.get("https://wuzzuf.net/search/jobs/?q=machine%20learning&a=hpb")
src = response.content

# Parse HTML
soup = BeautifulSoup(src, "lxml")

# Find elements
job_titles = soup.find_all("h2", {"class": "css-m604qf"})  # Check if this class exists
dates = soup.find_all("div", {"class": "css-do6t5g"})
locations = soup.find_all("span", {"class": "css-5wys0k"})

# Make sure all lists are the same length
num_jobs = min(len(job_titles), len(dates), len(locations))

for i in range(num_jobs):
    Job_Titles.append(job_titles[i].text.strip())
    Dates.append(dates[i].text.strip())
    Locations.append(locations[i].text.strip())

# Save to CSV
exported = zip_longest(Job_Titles, Dates, Locations)

csv_path = r"C:\Users\AdminOS\Documents\jobs.csv"  # Use a valid file path

with open(csv_path, "w", newline="", encoding="utf-8") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Titles", "Dates", "Locations"])
    wr.writerows(exported)

print("CSV file saved successfully!")
