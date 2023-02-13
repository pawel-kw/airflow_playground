import requests

base_url_param = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
query_param = "Red%20Ribbon%20Bakeshop"
radius_param = "20"
location_param = "32.9136713813233%2C-117.13166108295"
api_key = "AIzaSyAt2jC6p1CJza2ri6NDbZ8sxNzPMH1BexQ"

url = f"{base_url_param}&query={query_param}&location={location_param}&radius={radius_param}&key={api_key}"

#url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=mongolian&inputtype=textquery&locationbias=circle%3A2000%4047.6918452%2C-122.2226413&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={api_key}"
#url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=123%20main%20street&location=42.3675294%2C-71.186966&radius=10000&key={api_key}"


print(url)

payload={}
headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# place_id = response.json()["results"][0]["place_id"]
place_id = "ChIJQxljRuH424ARfa4Rmw_22zk"

# with open("response.json", "w") as outfile:
#     outfile.write(response.text)
# print(place_id)

base_url_param = "https://maps.googleapis.com/maps/api/place/details/json?"
fields_param = "opening_hours"
url = f"{base_url_param}fields={fields_param}&place_id={place_id}&key={api_key}"

response = requests.request("GET", url, headers=headers, data=payload)
with open("response_details.json", "w") as outfile:
    outfile.write(response.text)
print(response.text)

