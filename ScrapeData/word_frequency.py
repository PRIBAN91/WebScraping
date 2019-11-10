from bs4 import BeautifulSoup
import urllib2
import re

# URL to be parsed/scraped
url = 'https://hiverhq.com/'
response = urllib2.urlopen(url)
page = response.read()
# read it into bs4
soup = BeautifulSoup(page, 'html.parser')
# print soup.prettify()
body = soup.find('body')
# print body.contents
# Frequency Dictionary to store word frequencies
freq_dict = dict()


def populate_dict(line):
    line = re.sub(r'[.?\-";,*()]+', "", line)
    words = line.split()
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1


for content in body.contents:
    content = str(content)
    if content == "\n":
        continue
    if re.match(r"<[^>]+>", content):
        line = re.sub(r'<[^>]+>', "", content)
        populate_dict(line)
    else:
        populate_dict(content)

# print freq_dict
# List of Tuple to store sorted Frequency dictionary based on frequency in descending order
sorted_freq = [(key, value) for key, value in sorted(freq_dict.iteritems(), key=lambda (k, v): (v, k), reverse=True)]

# Print the Top 5 words and their corresponding frequencies
print "Top 5 occurrence of words in the given website along with their frequencies are given below."
for i, freq in enumerate(sorted_freq):
    print "Word: " + freq[0] + " :::: Frequency: " + str(freq[1])
    if i == 4:
        break
