from __future__ import print_function
import requests
from bs4 import BeautifulSoup as bs
import random
import os
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import command
import os.path
from sys import argv


os.remove("wallpaper.png")
os.remove("output.txt")
url = "https://www.espn.in/football/transfers"
page = requests.get(url, headers = {'User-Agent':'Mozilla/5.0'})
soup = bs(page.content, 'html.parser')
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
# wallpaper background
image = Image.open('background.jpg')
draw = ImageDraw.Draw(image)
# desired size
font = ImageFont.truetype('RobotoSlab-Bold.ttf', size=15)
# starting position of the message
(x, y) = (50, 50)
# News Api Key
api_key = "GetYourOwnDamnApiKey"
a = "a"
fb1 = a
fb2 = a
fb3 = a
fb4 = a
fb5 = a
fb1var = 0
fb2var = 0
fb3var = 0
fb4var = 0
fb5var = 0
fb1fromvar = 0
fb2fromvar = 0
fb3fromvar = 0
fb4fromvar = 0
fb5fromvar = 0
fb1tovar = 0
fb2tovar = 0
fb3tovar = 0
fb4tovar = 0
fb5tovar = 0
fb1from = a
fb2from = a
fb3from = a
fb4from = a
fb5from = a
fb1to = a
fb2to = a
fb3to = a
fb4to = a
fb5to = a
quote = a
newsapi = ""
list = []
txt = a
language = 'en'
global mail
mail = None
def main():
   
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['IMPORTANT'], maxResults=1).execute()
    messages = results.get('messages', [])
    

    if not messages:
        print ("No messages found.")
    else:
        for message in messages:
            msg1 = (service.users().messages().get(userId='me', id=message['id'], format="full", metadataHeaders=None).execute())
            headers=msg1["payload"]["headers"]
            subject= [i['value'] for i in headers if i["name"]=="Subject"]
            print(subject)
            list.extend("Latest Email" + "\n")
            list.extend(subject)
            list.extend("\n" + "\n")

if __name__ == '__main__':
    main()



def NewsFromBBC(): 
      
    # BBC news api 
    main_url = "https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=" + api_key
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i]) 
        list.extend(str(i+1) + " " +  results[i])
        list.extend("\n")
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()

        

for strong_tag in soup.find_all("a"):
    fb1 = (strong_tag.text)
    fb1var = fb1var + 1
    if(fb1var == 24):
    	print(fb1)
    	break
for strong_tag in soup.find_all("a"):
    fb1from = (strong_tag.text)
    fb1fromvar = fb1fromvar + 1
    if(fb1fromvar == 25):
    	print(fb1from[4:])
    	break
for strong_tag in soup.find_all("a"):
    fb1to = (strong_tag.text)
    fb1tovar = fb1tovar + 1
    if(fb1tovar == 26):
    	print(fb1to[3:])
    	break
for strong_tag in soup.find_all("a"):
    fb2 = (strong_tag.text)
    fb2var = fb2var + 1
    if(fb2var == 27):
    	print(fb2)
    	break
for strong_tag in soup.find_all("a"):
    fb2from = (strong_tag.text)
    fb2fromvar = fb2fromvar + 1
    if(fb2fromvar == 28):
    	print(fb2from[4:])
    	break
for strong_tag in soup.find_all("a"):
    fb2to = (strong_tag.text)
    fb2tovar = fb2tovar + 1
    if(fb2tovar == 29):
    	print(fb2to[3:])
    	break
for strong_tag in soup.find_all("a"):
    fb3 = (strong_tag.text)
    fb3var = fb3var + 1
    if(fb3var == 30):
    	print(fb3)
    	break
for strong_tag in soup.find_all("a"):
    fb3from = (strong_tag.text)
    fb3fromvar = fb3fromvar + 1
    if(fb3fromvar == 31):
    	print(fb3from[3:])
    	break
for strong_tag in soup.find_all("a"):
    fb3to = (strong_tag.text)
    fb3tovar = fb3tovar + 1
    if(fb3tovar == 32):
    	print(fb3to[4:])
    	break
for strong_tag in soup.find_all("a"):
    fb4 = (strong_tag.text)
    fb4var = fb4var + 1
    if(fb4var == 33):
    	print(fb4)
    	break
for strong_tag in soup.find_all("a"):
    fb4from = (strong_tag.text)
    fb4fromvar = fb4fromvar + 1
    if(fb4fromvar == 34):
    	print(fb4from[3:])
    	break
for strong_tag in soup.find_all("a"):
    fb4to = (strong_tag.text)
    fb4tovar = fb4tovar + 1
    if(fb4tovar == 35):
    	print(fb4to[3:])
    	break
for strong_tag in soup.find_all("a"):
    fb5 = (strong_tag.text)
    fb5var = fb5var + 1
    if(fb5var == 36):
    	print(fb5)
    	break
for strong_tag in soup.find_all("a"):
    fb5from = (strong_tag.text)
    fb5fromvar = fb5fromvar + 1
    if(fb5fromvar == 37):
    	print(fb5from[4:])
    	break
for strong_tag in soup.find_all("a"):
    fb5to = (strong_tag.text)
    fb5tovar = fb5tovar + 1
    if(fb5tovar == 38):
    	print(fb5to[3:])
    	break

list.extend(("\n",
"Here Ya Go. Football Transfers", "\n",
fb1 + "  " + "From" + "  " + 
fb1from[4:] + "  " + "To" + "  " + 
fb1to[3:] + "  " ,
"\n",
fb2 + "  " + "From" + "  " + 
fb2from[4:] + "  " + "To" + "  " + 
fb2to[3:] + "  " ,
"\n",
fb3 + "  " + "From" + "  " + 
fb3from[3:] + "  " + "To" + "  " + 
fb3to[4:] + "  " ,
"\n",
fb4 + "  " + "From" + "  " + 
fb4from[3:] + "  " + "To" + "  " + 
fb4to[3:] + "  " ,
"\n",
fb5 + "  " + "From" + "  " + 
fb5from[4:] + "  " + "To" + "  " + 
fb5to[3:] + "  "))
"\n",

# QUOTES

quote_file = "quotes.txt"
f = open(quote_file, 'r', encoding='cp1252')
txt = f.read()
lines = txt.split('\n.\n')
quote = random.choice(lines)
print(quote)

#writing to txt
output = open("output.txt","a")
output.writelines(list)
time.sleep(30)
output.close()

# writing to img (news)
file = open('output.txt' ,mode='r')
message = file.read()   
time.sleep(10)
color = 'rgb(255, 255, 255)' # black color
draw.text((x, y), message, fill=color, font=font)
file = open('output.txt' ,mode='r')
message = file.read()   
time.sleep(10)
# Quote 
font1 = ImageFont.truetype('RobotoSlab-Bold.ttf', size=35)
draw.text((50, 500), quote, fill=color, font=font1)


# save the edited image
image.save('wallpaper.png')
# wallpaper
os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/raghs/Projects/Wallpaper_Engine/wallpaper.png")
