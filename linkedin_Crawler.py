
import sqlite3
import re
import requests
from bs4 import BeautifulSoup
import time

start = time.time()

# connect to database
db = sqlite3.connect('linkedIn.db')
cursor = db.cursor()


# get the URL to crawl
url = input("Enter URL: ")

db_name = str(url)
# Create database
cursor.execute("CREATE TABLE IF NOT EXISTS" + db_name + " (URL varchar(255), Title varchar(255), connections varchar(255))")

all_urls = []
all_urls.append(url)

def extract_conections(soup):
#    Extract required data for crawled page
    title = soup.title.string
    try:
        connections = soup.find('link', {'rel':'connections'})['href']
    except:
        connections = "Null"

    contents_dirty = soup.text
    contents = contents_dirty.replace("\n","")
    return (title, contents, connections)


def extract_links(soup):
#    Extract links
    links = soup.find_all('a')
    for link in links:
        if str(link.get('href')).startswith(url) == True and link.get('href') not in all_urls:
            continue
        else:
                all_urls.append(link.get('href'))

    return (len(links))


def insert_data(extracted_data):
#    Insert the crawled data into the database
    url,title, contents, connections = extracted_data

    cursor.execute("INSERT INTO " + db_name + " (URL, Title, connections) VALUES(?,?,?)",(url, title,contents, connections))
    db.commit()


link_counter = 0
while link_counter < len(all_urls):

    try:
        print(str(link_counter) + " crawling: " + all_urls[link_counter])
        r = requests.get(all_urls[link_counter])
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            no_of_links = extract_links(soup)
            title, contents, connections = extract_conections(soup)
            insert_data((all_urls[link_counter], title, contents, no_of_links,connections))

        link_counter += 1

    except Exception as e:
        link_counter += 1
        print(str(e))


cursor.close()
db.close()
end = time.time()
print(end - start)
