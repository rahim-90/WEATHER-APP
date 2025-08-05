import requests
import json
import pyttsx3 as py

city = input("Enter the name of city:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=0d0e69209e044643baf110744250108&q={city}"
a = requests.get(url)
#print(a.text)
dic = json.loads(a.text)
w = dic["current"]["temp_c"]
b = py.init()
b.say(f"The current weather in {city} is {w} degrees")
print(f"The current weather in {city} is {w} degrees ")
b.runAndWait()