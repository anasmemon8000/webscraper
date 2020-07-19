import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/dp/B0794JD9JS?ref=MarsFS_AUCC_Echoplus'

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

def checker():

    page = requests.get(url , headers = headers)

    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup.prettify())
    title = soup.find(id = 'productTitle').get_text()
    #print(title.strip())

    price = soup.find(id = "priceblock_ourprice").get_text()
    p = price[2:10]
    price = float(p.replace(',' , ''))#price is now converted to a numerical value

    if price < 10000.00:
        send_mail()
        print("product name :" , title.strip())
        print("current price:" , "Rs.", price)
        print("-------------------- Reduction Reduction Reduction observed --------------------")
    else:
        print("product name :" , title.strip())
        print("current price:" , "Rs.", price)
        print("-------------------- No Reduction in price observed. --------------------")



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("anasmemon9000@gmail.com" , 'asjwzdjrpyatxvnq')

    subject = "Reduction in Price has been observed on your product!"
    body = '''
    There has been a reduction in the price observed of your selected product on amazon!
    visit now : https://www.amazon.in/dp/B0794JD9JS?ref=MarsFS_AUCC_Echoplus
    '''
    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
    'anasmemon9000@gmail.com',
    'anasmemon8000@gmail.com',
    msg
    )

    print("Email has been sent!!")
    server.quit()

while True:
    checker()
    time.sleep(24*60*60)#works once a day !
