from bs4 import BeautifulSoup
import re
import os

# Path to the HTML file

file_path = '/Users/sidharthbasam/PycharmProjects/htmlb4/mysecondhtmlpage.html'


# Ensure the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")

# Read the HTML content from the file
with open(file_path, 'r') as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# a. The text of the HTML page title.
title_text = soup.title.string if soup.title else "No title found"
print("a.", title_text)

# b. The text of the second list item element "li" below "To show off"?
second_li_text = soup.find_all('li')[3].string if len(soup.find_all('li')) > 3 else "Not enough list items"
print("b.", second_li_text)

# c. All cells of the first row of the table.
first_row_cells = [td.get_text() for td in soup.find_all('tr')[0].find_all('td')] if soup.find_all('tr') else []
print("c.", first_row_cells)

# d. All h2 headings text that includes the word “tutorial”.
h2_tutorial_texts = [h2.get_text() for h2 in soup.find_all('h2', string=re.compile(".*tutorial.*"))]
print("d.", h2_tutorial_texts)

# e. All text that includes the “HTML” word.
html_texts = soup.find_all(string=re.compile(".*HTML.*"))
print("e.", html_texts)

# f. All cells text of the second row of the table.
second_row_cells = [td.get_text() for td in soup.find_all('tr')[1].find_all('td')] if len(soup.find_all('tr')) > 1 else []
print("f.", second_row_cells)

# g. All images from the table.
table_images = [img['src'] for img in soup.find_all('table')[0].find_all('img')] if soup.find_all('table') else []
print("g.", table_images)