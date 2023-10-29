from imports import *
from api_keys import *
from icon_dict import *

#parsing through command line
parser = argparse.ArgumentParser(description="Check the weather for a certain country/city") 
parser.add_argument("country", help="The country/city to check the weather for")
args = parser.parse_args()

#URL generation using base_url of Openweathermap API and unique API_key
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"
response=requests.get(url)

#No response from the server refers to the city/country not found
if response.status_code != 200:
    print("Sorry, that country/city was not found")
    exit()

#Response from the server when the country/city is found
data = response.json()
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
report = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]
weather_icon = WEATHER_ICONS.get(icon, "")
output = pyfiglet.figlet_format(f"{city}, {country}")
output += f"\nTemperature: {temperature}°C\nFeels like: {feels_like}°C\nReport:{weather_icon} {report}\n"

print(chalk.yellowBright(output))
