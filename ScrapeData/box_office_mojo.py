import requests
import pandas as pd
import urllib2
from bs4 import BeautifulSoup


url = "https://www.boxofficemojo.com/movies/?page=intl&id=marvel2019.htm"
response = urllib2.urlopen(url)
page = response.read()
# read it into bs4
soup = BeautifulSoup(page, 'html.parser')
print soup.prettify()
# body = soup.find('body')
# print body

# chose the correct table from the result
# tabular_data = content[3]
#
# # drop the row with the title
# tabular_data = tabular_data.drop(0)
#
# # housekeeping renamer
# tabular_data.columns = ['title', 'studio', 'total_gross', 'total_theaters',
#                         'opening_gross', 'opening_theaters', 'opening_date']
