import bs4, requests

def getSakuga():
  url = "https://www.sakugabooru.com/post/random"
  bUrl = "https://www.sakugabooru.com/data/"

  response = requests.get(url)
  response.raise_for_status()
  soup = bs4.BeautifulSoup(response.text, 'html.parser')
  divSak = soup.find(class_='original-file-unchanged')
  sakD = divSak.find(bUrl)
  fSak = str(divSak.get('href'))
  if bUrl in fSak:
    print(fSak)
    return fSak
