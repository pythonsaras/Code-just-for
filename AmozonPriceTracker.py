from lxml import html
import requests
from time import sleep
import time
import schedule
import smtplib

receiver_email_id="sarasyadav420@gmail.com"

def check(url):
    hearders={'User-Agent':'Mozila/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/42.9.2311.90 Safari/537.36'}
    
    page=requests.get(url,headers=hearders)
    for i in range(20):
        sleep(3)
        doc=html.fromstring(page.content)
        
        XPATH_AVAILABILITY='//div[@id ="availability"]//text()'
        RAw_AVAALABILITY=doc.xpath(XPATH_AVAILABILITY)
        AVAILABILITY=''.join(RAw_AVAALABILITY).strip() if RAw_AVAALABILITY else None
        return AVAILABILITY


def sendMail(ans,product):
    USERNAME="ENTER USERNAME"
    USERPASSWORD="PASSWORD"
    recipient=receiver_email_id
    body_of_email=ans
    email_subject=product+'product availability'
    s=smtplib.SMTP('smtpp.gmail.com',587)
    s.starttls()
    s.login(USERNAME,USERPASSWORD)
    headers="\r\n".join(["from:"+USERNAME,"suject:"+email_subject,
                         "to:"+recipient,
                         'mime-version: 1.0',
                         'content-type:text/html'])
    content=headers+'r\n\r\n'+body_of_email
    s.sendmail(USERNAME,recipient,content)
    s.quit()
def ReadAsin():
    Asin='B077PWK5BT'
    url='http://www.amazon.in/dp/'+Asin
    print("Processing:"+url)
    ans=check(url)
    arr=["1",'2','3']
    print(ans)
    if ans in arr:
        sendMail(ans,Asin)
        
def job():
    print("Tracking...")
    ReadAsin()
schedule.every(1).minutes.do(job)
        
while True:
    schedule.run_pending()
    time.sleep(1)


   
        
        
        