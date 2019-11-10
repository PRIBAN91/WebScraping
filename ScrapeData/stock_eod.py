from bs4 import BeautifulSoup
import urllib2
import re
import pandas as pd
import datetime

# url = "https://www.moneyworks4me.com/best-index/nse-stocks/top-nse500-companies-list"

# URLs to be parsed/scraped
urls = {
    "MidCap": "https://www.moneyworks4me.com/comp-peer/index/index/order/netsales/sort/desc/fid//type//seid//indexid//marketcapid/2/industryid//pagelimit/204",
    "LargeCap": "https://www.moneyworks4me.com/comp-peer/index/index/order/netsales/sort/desc/fid//type//seid//indexid//marketcapid/1/industryid//pagelimit/143",
    "SmallCap": "https://www.moneyworks4me.com/comp-peer/index/index/order/netsales/sort/desc/fid//type//seid//indexid//marketcapid/3/industryid//pagelimit/3324"}

for k, url in urls.iteritems():

    response = urllib2.urlopen(url)
    page = response.read()
    # print page
    # read it into bs4
    soup = BeautifulSoup(page, "lxml")
    # print soup.prettify()
    # body = soup.find('body')
    # print body.contents
    # # Frequency Dictionary to store word frequencies
    #
    data = []
    header = soup.find('table', attrs={"style": "width:987px;", "class": "left"})
    header_rows = header.find_all('tr')
    # print header_rows
    for row in header_rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # print data

    table = soup.find('table', attrs={"style": "width:987px; margin-top:-1px;"})
    # print table
    # # table_body = table.find('tbody')
    #
    rows = table.find_all('tr')
    # print rows
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # extra_data = page.strip("</html>")[1]
    # print extra_data

    # print data

    df = pd.DataFrame(data=data[1:], columns=data[0])

    # df.to_csv(r"D:\Stock Data\Test.csv")

    df["Latest Price(Rs.)"] = pd.to_numeric(df["Latest Price(Rs.)"].map(lambda x: x.replace(",", "")), errors='coerce')

    df1 = df[df["Latest Price(Rs.)"] < 400]

    # df = pd.to_numeric()

    df1.to_csv(r"D:\Stock Data\Filtered_{}_{}.csv".format(k, str(datetime.date.today())))
