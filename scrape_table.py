import requests
from bs4 import BeautifulSoup
import os

def scrape_table(data,date):

    # load data into bs4
    soup =BeautifulSoup(data, 'html.parser')

    # extract only the table from page
    table = soup.find('table', { 'id': 'headFixed' })
    tbody = table.find('tbody')

    #Check for empty table
    row_count = len(tbody.find_all('tr'))
    if row_count < 2:
        print("No record for ",date)
        return False
    

    # Intilalize variables
    head_row =[
        'Symbol',
        'Date',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume'
    ]
    # Create a new file and write title row
 
    filename = date + '.csv'
    with open(filename, "w") as outfile:
        
        outfile.write(str(head_row))
        outfile.write("\n")

    row_data = []

    for tr in tbody.find_all('tr'):
        #Serial_no = tr.find_all('td')[0].text.strip()
        symbol = tr.find_all('td')[1].text.strip()
        open_price = tr.find_all('td')[3].text.strip()
        high_price = tr.find_all('td')[4].text.strip()
        low_price  = tr.find_all('td')[5].text.strip()
        close_price= tr.find_all('td')[6].text.strip()
        Vol = tr.find_all('td')[8].text.strip()
        #row_data.append(Serial_no)
        row_data.append(symbol)
        row_data.append(date)
        row_data.append(open_price)
        row_data.append(high_price)
        row_data.append(low_price)
        row_data.append(close_price)
        row_data.append(Vol)

        with open(filename, "a+") as outfile:
            outfile.write(str(row_data))
            outfile.write("\n")

        row_data.clear()
    return True