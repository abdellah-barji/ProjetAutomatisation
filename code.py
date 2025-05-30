from twilio.rest import Client
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

weather_url = "https://wttr.in/?format=3" 
try:
    weather_response = requests.get(weather_url)
    weather_info = weather_response.text.strip()
except Exception as e:
    print("Error fetching weather data:", e)
    weather_info = "Weather data unavailable"


if "rain" in weather_info.lower():
    print("It's raining; the form submission will not proceed.")


account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
auth_token = "XXXXXXXXXXXXXXXXe"            
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=weather_info,
    from_="+1971XXXXXXX", 
    to="+21264XXXXXXX"   
)

print("SMS Sent. ID:", message.sid)
