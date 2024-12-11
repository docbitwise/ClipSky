from atproto import Client
from steam import webapi
import os

from bsky_helpers import BskyEasyClient
from misc_helpers import getPNGfromImgUrl, getPNGsFromImgUrls

# from bsky_helpers import BskyEasyClient
# from misc_helpers import getPNGfromImgUrl

# You'll need to create a Steam Web API key and add it to your .env file
# in the format STEAM_WEB_API_KEY=your_api_key
# Create one here - https://steamcommunity.com/dev/apikey
# To find your Steam account key, look here - https://store.steampowered.com/account/

steam_web_api_key = os.getenv("STEAM_WEB_API_KEY")
steam_account_key = os.getenv("STEAM_ACCOUNT_KEY")
# print("steam_web_api_key:", steam_web_api_key)
# print("steam_account_key:", steam_account_key)

steamAPI = webapi.WebAPI(steam_web_api_key)

player_summary_response = steamAPI.call(
    'ISteamUser.GetPlayerSummaries', steamids=steam_account_key)

player_name = player_summary_response["response"]["players"][0]["personaname"]
avatar_full_url = player_summary_response["response"]["players"][0]["avatarfull"]

recent_games_response = steamAPI.call(
    'IPlayerService.GetRecentlyPlayedGames', steamid=steam_account_key, count=0)

game_controller_emoji = "🎮"
hashtag = "#DrBotwise"
post_header = f"Steam 2-week recap {hashtag}\n\n"

# post_text = post_header + "I'm " + player_name + " and I'm playing " + \
#     str(len(recent_games_response["response"]["games"])) + " games!\n\n"
post_text = f"{post_header}Here is my recent game activiy in Steam {
    game_controller_emoji}\n\n"
post_text += "(Playtime in minutes)"

game_images_urls = []
for game in recent_games_response["response"]["games"]:
    post_text += "\n- " + \
        game["name"] + " (" + str("{:,}".format(game["playtime_2weeks"])) + ")"
    hash = game["img_icon_url"]
    appid = game["appid"]
    # game_images_urls.append(f"http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{hash}.jpg")
    game_images_urls.append(
        f"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/{appid}/header.jpg")

print(post_text)
print(len(post_text))

game_pngs = getPNGsFromImgUrls(game_images_urls)
game_pngs.append(getPNGfromImgUrl(avatar_full_url))


# BlueSky login and post
BEC = BskyEasyClient()
# BEC.postWithImages(text=post_text, images=game_pngs, tags=[hashtag])
