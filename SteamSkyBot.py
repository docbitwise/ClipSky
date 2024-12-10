# You'll also need to create a Steam Web API key and add it to your .env file
# in the format STEAM_WEB_API_KEY=your_api_key
# Create one here - https://steamcommunity.com/dev/apikey
# To find your Steam account key, look here - https://store.steampowered.com/account/ 

from steam import webapi
import os

steam_web_api_key = os.getenv("STEAM_WEB_API_KEY")
steam_account_key = os.getenv("STEAM_ACCOUNT_KEY")
# print("steam_web_api_key:", steam_web_api_key)
# print("steam_account_key:", steam_account_key)

steamAPI = webapi.WebAPI(steam_web_api_key)

player_summary_response = steamAPI.call('ISteamUser.GetPlayerSummaries', steamids=steam_account_key)

player_name = player_summary_response["response"]["players"][0]["personaname"]
avatar_full_url = player_summary_response["response"]["players"][0]["avatarfull"]

recent_games_response = steamAPI.call('IPlayerService.GetRecentlyPlayedGames', steamid=steam_account_key, count=0)

post_header = "Steam 2 week recap:\n"
post_header += "#DrBotwise \n\n"
post_text = post_header + "I'm " + player_name + " and I'm playing " + str(len(recent_games_response["response"]["games"])) + " games!\n\n"
post_text += "(Playtime in minutes)"

for game in recent_games_response["response"]["games"]:
    post_text += "\n- " + game["name"] + " (" + str("{:,}".format(game["playtime_2weeks"])) + ")"

print(post_text)
print(len(post_text))

import requests
from PIL import Image
from io import BytesIO

# Fetch the image
response = requests.get(avatar_full_url)
avatar_image_data = None

# Check if the request was successful
if response.status_code == 200:
    # Open the image using Pillow
    avatar_image_data = Image.open(BytesIO(response.content))
    
    # Save the image as .jpg 
    avatar_image_data.save('avatar.jpg', format='JPEG')
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")


# BlueSky login and post
from atproto import Client

# To run this for your own account, you need to create a .env file with your username and password
# in the format BSKY_USERNAME=username and BSKY_PASSWORD=password

bsky_username = os.getenv("BSKY_USERNAME")
bsky_password = os.getenv("BSKY_PASSWORD")
# print("username:", bsky_username)
# print("password:", bsky_password)

bskyClient = Client()
bskyClient.login(bsky_username, bsky_password)

with open('avatar.jpg', 'rb') as f:
    img_data = f.read()

if img_data is not None:
    steam_recap_post_response = bskyClient.send_image(text=post_text, image=img_data, image_alt="Avatar of " + player_name)
else:
    steam_recap_post_response = bskyClient.send_post(text=post_text)

print("Posted to BlueSky:", steam_recap_post_response)