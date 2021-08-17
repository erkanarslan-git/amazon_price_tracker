import requests
from bs4 import BeautifulSoup
import smtplib
import time

#This link is the link we want to track
URL="https://www.amazon.de/-/en/SanDisk-Extreme-Pro-SDSSDXPM2-500G-G25-500gb/dp/B07BSSFB4N/ref=psdc_430168031_t3_B07MH2P5ZD"
# Google the "User-Agent" and you will get your user-agent
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

#Get the price from the site / scraping
def Get_Price():
    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.content, "html.parser")
    #title = soup.find(id="productTitle")
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    convertedPrice = price[1:5]#Four character
    #print(convertedPrice.strip())
    
    if(float(convertedPrice) < 90.0):# if price falls, 
        Send_Mail() #send mail


# Before start to send mail the gmail 2-Step Verification must be activated
def Send_Mail():
    server = smtplib.SMTP("smtp.gmail.com",587)#Default settings for gmail mail sender services
    server.ehlo() # :)
    server.starttls()
    server.ehlo()

    server.login("SenderMail", "The App Key")# --> This key has been created from App Google Account
    subject = "Hey! Price Fell Down!"
    body="Check The Amazon Link! https://www.amazon.de/-/en/SanDisk-Extreme-Pro-SDSSDXPM2-500G-G25-500gb/dp/B07BSSFB4N/ref=psdc_430168031_t3_B07MH2P5ZD"
    message = f"Subject: {subject}\n\n {body}"
    server.sendmail("SenderMail", "ReceiverMail", message)

    print("YEHHOO EMAIL HAS BEEN SENT!")
    server.quit()

while(True):
    Get_Price()# Start the app with this method. 
    time.sleep(5)
#PUT YOUR LINK THAT YOU WANT TO TRACK AND GRAB THE PRODUCT :)


