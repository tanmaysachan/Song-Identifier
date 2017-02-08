from bs4 import BeautifulSoup
import requests

qry = input("Enter the lyrics: ")
query = ""
for i in qry:
	if i == ' ':
		query += '%20'
	else:
		query += i
url = 'https://www.musixmatch.com/search/' + query + '/lyrics'
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
url = url.strip()
code = requests.get(url, headers=headers)
src_code = code.content
soup = BeautifulSoup(src_code, 'html.parser')
Song_Name = ''
Artist = ''
try:
	d = soup.find_all('div' ,class_="media-card-text")[0]
	a = d.find('a', class_='artist')
	aa = d.find('a', class_='title')
	Artist = a.string
	Song_Name = aa.string
	print("The Name of the song is -> " + Song_Name)
	print("The artist is -> " + Artist)
except:
	print("Sorry, Song not found")

