import requests
from bs4 import BeautifulSoup
import youtube_dl
import json

songs = []
res = []

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True
}

query = input("Enter song name: ")

response = requests.get(
    f"https://www.youtube.com/results?search_query={query} song")

soup = BeautifulSoup(response.text, 'html.parser')

for aas in soup.find_all('a'):
    if(aas['href'].startswith('/watch?v=')):
        songs.append(aas['href'])

for sngs in songs[:5]:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(
            f"https://www.youtube.com{sngs}", download=False)
        video_url = info_dict.get("url", None)
        video_duration = info_dict.get("duration", None)
        video_title = info_dict.get("title", None)
        video_thumbnail = info_dict.get("thumbnail", None)
        video_artist = info_dict.get("artist", None)
        info = {
            "url": video_url,
            "title": video_title,
            "thumbnail": video_thumbnail,
            "artist": video_artist,
            "duration": video_duration
        }
        res.append(info)
j = json.dumps(res)
print(j)

#with open('j.json','w') as f:
#   json.dump(j,f)