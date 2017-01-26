import urllib.request
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient #SMS API Package
import time

account_sid = "AC5d88a649c63801497370cbd97a704697" #Your Twilio account ID
auth_token = "539f1ccc3d82f482e52ca7e8cfd548e6"    #Your secret API Token
 
client = TwilioRestClient(account_sid, auth_token)
url = input('Enter the Url of Product Page: ')
your_price = input('Enter the price your you want: ')
contact_info = input('Your Contact Info: ')

while True:
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")
    current_price = soup.find("span",attrs = {"id":"priceblock_ourprice"})
    for string in current_price.stripped_strings:
        curr_price = repr(string)[1:-4]
    if(curr_price <= your_price): 
        msg = client.messages.create(to=contact_info, from_="+14843094282", body="rush to Amazon, Price of Headsets are below your price") #Will send SMS to your phone number
        print("SMS Sent Thanks....quitting application")
        quit()
    else:
        time.sleep(20) #sleep for 20 seconds
        
