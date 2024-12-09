from atproto import Client
import os

# To run this for your own account, you need to create a .env file with your username and password
# in the format BSKY_USERNAME=username and BSKY_PASSWORD=password

username = os.getenv("BSKY_USERNAME")
password = os.getenv("BSKY_PASSWORD")

print("username:", username)
print("password:", password)

# first, login
client = Client()
client.login(username, password)

# write a loop to get the last 5 posts from the feed
author_feed = client.get_author_feed(actor=username, limit=5)
for post in author_feed.feed:
    print(post["post"]["record"]["text"])
    
    
# get profile
profile_response = client.get_profile(actor=username)
# get number of followers
print("followers:", profile_response.followers_count)
try:
    print("How many via Starter Pack:", profile_response.joined_via_starter_pack.joined_all_time_count)
except AttributeError:
    print("Not via Starter Pack")

# post = client.send_post("Test post again via Python SDK")