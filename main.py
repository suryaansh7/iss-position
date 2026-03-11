import requests
from datetime import datetime
import smtplib

response=requests.get(url="http://api.sunrise-sunset.org/json")
response.raise_for_status()

data=response.json()
lat=float(data["iss_position"]["latitude"])
lon=float(data["iss_position"]["longitude"])
pos=(lat,lon)
MY_LAT=22.572645
MY_LONG=88.363892
paramters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response=requests.get(url="http://api.sunrise-sunset.org/json", params=paramters)
response.raise_for_status()
data=response.json()

sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now=datetime.now()
k=0
j=0

t=MY_LAT+5
R=MY_LAT-5

M=MY_LONG+5
N=MY_LONG-5
if lat>=R and lat<=t:
    if lon>=N and lon<=M:
        j=1




if sunset==time_now.hour:
    k=1


if k==1 and j==1:
    my_email="suryaanshpoddar1@gmail.com"
    pwd="xxqdcxuxltdiejvp"
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=pwd)
    connection.sendmail(from_addr=my_email,to_addrs="suryaanshpoddar2@gmail.com",msg="look up")
    connection.close()




