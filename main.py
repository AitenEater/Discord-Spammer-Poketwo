from webserver import keep_alive
import requests

channelID = 1185699952639348877
headers = {
    "authorization":
    "MTE4NTcwMjU1MjY5Njc5MTIwMg.G7OgUU.LUMwkbuKSNhuOYmBk6N2n3RCWzU8PYWZVUl4jc"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
