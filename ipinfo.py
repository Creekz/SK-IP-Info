import requests
import json

def start():
  print("""
  ___           ___            __         
 |_ _|  _ __   |_ _|  _ __    / _|   ___  
  | |  | '_ \   | |  | '_ \  | |_   / _ \ 
  | |  | |_) |  | |  | | | | |  _| | (_) |
 |___| | .__/  |___| |_| |_| |_|    \___/ 
       |_|                               
 
 by Creekz
  """)
  ip = input(" Enter IP: ")
  response = requests.get("https://ipinfo.io/{}".format(ip))
  data = response.json()
  print("IP: "+data["ip"])
  print("Hostname: "+data["hostname"])
  print("City: "+data["city"])
  print("Region: "+data["region"])
  print("Country: "+data["country"])
  print("Location: "+data["loc"])
  print("Organisation: "+data["org"])
  input()

if __name__ == "__main__":
  start()