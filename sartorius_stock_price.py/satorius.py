import requests 

API = "ztVrZ0hQ1YoyzSj9FyJ_8VYUclL1BGcR" #my api for polygon

url = 'https://api.polygon.io/v2/aggs/ticker/SOAGY/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&limit=120&apiKey='

r = requests.get(url + API) # Getting the url information with my API
data = r.json() #requesting the data in Json format 

# print(data)

#for k, v in data.items():
    #print(k, "=", v)


#print ("-------------")

print("The Sartorious Stock Price(SOAGY) in US Dollars is", data["results"][0]["h"])
