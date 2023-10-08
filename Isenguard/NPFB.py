
import requests
import pandas as pd





def weap(city):
 request_url = f"https://api.weatherapi.com/v1/current.json?key=829ab5bc7a314cdabe9153842230710&q="+city+"&aqi=yes"
 response = requests.get(request_url)
   
 if response.status_code == 200:
    
    return response.json()
 



def application(city):
 wa=dict(weap(city))
 we=wa["current"]

 temperature=(we["temp_c"])
 day=(we["is_day"])
 wind_kph=(we["wind_kph"])
 #wind_degree=(we["wind_degree"])
 #wind_dir=(we["wind_dir"])
 #pressure_mb=(we["pressure_mb"])
 humidity=(we["humidity"])
 #feelslike_c=(we["feelslike_c"])
 #vis_km=(we["vis_km"])
 air_quality=(we["air_quality"])

 risk=0
 
 if humidity<15:
  risk+=1
 if day==1:
  risk+=1
 if air_quality["pm2_5"]>15:
  risk+=1
 if air_quality["pm10"]>40:
  risk+=1
 if air_quality["co"]>420:
  risk+=1
 if air_quality["o3"]<20:
  risk+=1
 if air_quality["so2"]>10:
  risk+=1
 if air_quality["no2"]>6.6:
  risk+=1
 if temperature>18:
  risk+=1
 if wind_kph>25:
  risk+=1

 print(risk)
 return risk,temperature,day,wind_kph,humidity,air_quality["pm2_5"],air_quality["pm10"],air_quality["co"],air_quality["o3"],air_quality["so2"],air_quality["no2"]
     
