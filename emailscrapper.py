Open in Linux terminal

nano emailscrapper.py

from collection import deque
import re 

from bs4 import BeautifulSoup
import requests
import urllib.parse

user_url = str(Input('[+] Masukkan url : '))
urls = deque([user_url])
scrapped_urls = set()
email = set()
count = 0

try :
  while true :
    count += 1
    if count > 10 :
      break

url = urls.popleft()
scrapped_urls.add(url)
parts = urllib.parse.urlsplit(url)
base_url = f'{parts.scheme}://{parts.netloc}'
path = url [:url.rfind('/')+1] if '/' in parts.path
  else url
  print(f'{count} memproses {url}')
  
try :
  response = request.get(url)
  
except(request.exceptions.missingschema, request.exceptions.ConnectionError);
  continue
  
new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.+[a-z\.]+',response.text, re.I))
emails.update(new_emails)

soup = BeautifulSoup(response.text, 'html.parser')
for anchor in soup.find_all('a'):
          link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
          if link.startswith('/'):
             link = base_url + link
          elif not link.startswith('http'):
              link = path + link
              
          if not link in urls and not link in scrapped_urls:
                 urls.append(link)

except KeyboardInterrupt :
       print('[-]Closing!')
    
print('\n Proses Selesai!')
print(f'\n{len(emails)} Email Ditemukan \n ==================')

for mail in emails:
        print(' '+mail)

print('\n')
