import requests

channelID = 693123727772352552
headers = {"authorization": "//your token"}

file = open("text.txt", "r")
lines = file.readline()

for line in lines:
    r = requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", headers = headers, json = {"content": lines})

