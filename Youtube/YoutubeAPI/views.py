
import requests
from bs4 import BeautifulSoup
import youtube_dl
import json
from django.shortcuts import render
from rest_framework import viewsets
from .models import Song  #import song class from models
from .serializer import SongSerialiser #import serializer from serialiser file
from rest_framework.response import Response #response library to give to response
from rest_framework.views import APIView #its just a apiview
from rest_framework import generics
# Create your views here.
global data

data =[
    {
        "url": "https://r2---sn-po4g5uxa-5hql.googlevideo.com/videoplayback?expire=1584724856&ei=GKd0Xu2AB5juogPBvoDADg&ip=43.248.36.67&id=o-AB3Ec-RDRr7eF9oe0IhyAHm7pNamZ_bxq4x5yYEGSiPb&itag=251&source=youtube&requiressl=yes&mh=cf&mm=31%2C29&mn=sn-po4g5uxa-5hql%2Csn-cvh76ned&ms=au%2Crdu&mv=m&mvi=1&pl=24&gcr=in&initcwndbps=456250&vprv=1&mime=audio%2Fwebm&gir=yes&clen=3306185&dur=198.901&lmt=1580821815401401&mt=1584703185&fvip=5&keepalive=yes&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ABSNjpQwRAIgMtq5s5aRpWIrnkdqMdfFXyWweFliEpFavX85R_B-70ECIGbN-WqDT6CnfyVor_sGsJDqipgThdf1HBOh236FQeEO&sig=ADKhkGMwRgIhALJKfq7OOHKa_XGXwm7eVEKjuKXAbcwVePhutvbHlo-BAiEA7I-CKEcCj9YrnT--W7v79htA8rM7ZKLB_LEttGYuws4=&ratebypass=yes",
        "title": "Ariana Grande - One Last Time (Lyric Video)",
        "thumbnail": "https://i.ytimg.com/vi/Wg92RrNhB8s/maxresdefault.jpg",
        "artist": "Ariana Grande",
        "duration": 199
    },

    {
        "url": "https://r2---sn-po4g5uxa-5hql.googlevideo.com/videoplayback?expire=1585363026&ei=8mN-XtvBHZiEssUPsfyg2A4&ip=45.126.144.229&id=o-AAl1d9hXeP4wpYnhI9hd-hKHGo5xIwW9jRSPcHdZwwer&itag=251&source=youtube&requiressl=yes&mh=cf&mm=31%2C29&mn=sn-po4g5uxa-5hql%2Csn-cvh76ned&ms=au%2Crdu&mv=m&mvi=1&pl=24&gcr=in&initcwndbps=705000&vprv=1&mime=audio%2Fwebm&gir=yes&clen=3306185&dur=198.901&lmt=1580821815401401&ns=mSgvk66Yi86MrHWPw-mes-QB&mt=1585341359&fvip=5&keepalive=yes&c=WEB&txp=5531432&n=03CLeGtXL8WqsD1VZvg&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt%2Cns&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ABSNjpQwRQIgDHviUOl4ln_iCZ2XFSont_5TlZPonkzp4yg67Bb6bFQCIQDZw85Xgy_xlAJtk0SFFDNugEHanzecxP9J6fGq6FVGxQ%3D%3D&sig=ADKhkGMwRAIga1fEEZfdLcoejyBJxshFWlb1DFqAsL9b1iMJ3dxUdeMCIDRSrzJbDH1oeHM0qHv4KfVdAK1iOvReQ1blmE9ayhxL&ratebypass=yes",
        "title": "Ariana Grande - One Last Time (Lyric Video)",
        "thumbnail": "https://i.ytimg.com/vi/Wg92RrNhB8s/maxresdefault.jpg",
        "artist": "Ariana Grande",
        "duration": 199
    },

    {
        "url": "https://r1---sn-po4g5uxa-5hql.googlevideo.com/videoplayback?expire=1585363027&ei=82N-XquQGOOC3LUP_cqe4Ao&ip=45.126.144.229&id=o-ABmk3RCvLGJKnS-jMs6fW6ye3e97bV_9gnxcEXwSe1cB&itag=251&source=youtube&requiressl=yes&mh=wA&mm=31%2C29&mn=sn-po4g5uxa-5hql%2Csn-cvh76nez&ms=au%2Crdu&mv=m&mvi=0&pl=24&gcr=in&initcwndbps=705000&vprv=1&mime=audio%2Fwebm&gir=yes&clen=3992372&dur=249.461&lmt=1574721441255236&mt=1585341252&fvip=3&keepalive=yes&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ABSNjpQwRQIhAPDvX8w5Y0H63T3xErZHPdixP-_TqTGXQtyUBNKYBPU6AiBgS38Ptb6r855KLpl4CmyBpwLHOh1CTHxW56rauqz5Yg%3D%3D&sig=ADKhkGMwRAIgP54Soc8onhXQ3B_Driqgfe7Yt8RXUyYqdLTik8KgR5gCIHFBQppYv9RqlGALEqt8AQfmNYqrYuWhOEQJHqLyOren&ratebypass=yes",
        "title": "Ariana Grande - One Last Time (Official)",
        "thumbnail": "https://i.ytimg.com/vi/BPgEgaPk62M/maxresdefault.jpg",
        "artist": "Ariana Grande",
        "duration": 249
    },

    {
        "url": "https://r1---sn-po4g5uxa-5hql.googlevideo.com/videoplayback?expire=1585363028&ei=9GN-Xv3yCPGEz7sPkeS72AY&ip=45.126.144.229&id=o-ABovUydhkqYnA-WZKWX_JkZPrJSjIe6qhJz_PSzH78ui&itag=251&source=youtube&requiressl=yes&mh=wA&mm=31%2C29&mn=sn-po4g5uxa-5hql%2Csn-cvh76nez&ms=au%2Crdu&mv=m&mvi=0&pcm2cms=yes&pl=24&gcr=in&initcwndbps=705000&vprv=1&mime=audio%2Fwebm&gir=yes&clen=3992372&dur=249.461&lmt=1574721441255236&mt=1585341252&fvip=3&keepalive=yes&fexp=23882514&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=ABSNjpQwRgIhAMNhzEQCJufaPg9ncUGz9CXaMDRtjYCaqLbAZRQsa5mLAiEAwKO2CQXVV8WfeqXy9XmWoCqA4aBDeTIApwEOPj0WBqk%3D&sig=ADKhkGMwRQIhAOYz_3M3FVq3kgGl4IBEWiJSghNm85TOOqX4N2RZt8Q6AiB5bKdHUfwEoP_Soq7Ube5UV9OtAmL4_fgLG84oCdf4_A==&ratebypass=yes",
        "title": "Ariana Grande - One Last Time (Official)",
        "thumbnail": "https://i.ytimg.com/vi/BPgEgaPk62M/maxresdefault.jpg",
        "artist": "Ariana Grande",
        "duration": 249
    },

    {
        "url": "https://r2---sn-po4g5uxa-5hql.googlevideo.com/videoplayback?expire=1585363028&ei=9GN-XvPxOc-Q1AaS95PADQ&ip=45.126.144.229&id=o-AA9C7WSzizVdJnevusD2yq9_ezrs_KKeozTvchVRdcGL&itag=251&source=youtube&requiressl=yes&mh=TS&mm=31%2C29&mn=sn-po4g5uxa-5hql%2Csn-cvh7knez&ms=au%2Crdu&mv=m&mvi=1&pl=24&pcm2=no&initcwndbps=705000&vprv=1&mime=audio%2Fwebm&gir=yes&clen=3300139&dur=201.741&lmt=1574982703109799&mt=1585341252&fvip=5&keepalive=yes&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ABSNjpQwRQIgFmYntY-BC7BpDLSQ_mA7ek9CQmd2qrJs5ripONR1AVICIQDkHMf1rVGWBJVVi4fJl8iUH-b2DTFvByTCGAN9mR81Lg%3D%3D&sig=ADKhkGMwRQIgYRwLWH2hSRXP6n_vdCmFYEJ2V9IwCJPTfNn4XUT-L1UCIQDuWCM_36SeScXdW0dTbfIBn8-9XrL5LySmXJIoyu9PSA==&ratebypass=yes",
        "title": "Ariana Grande - One Last Time (Lyrics)",
        "thumbnail": "https://i.ytimg.com/vi/efDDY0zh0FE/maxresdefault.jpg",
        "artist": "Ariana Grande",
        "duration": 202
    }


]

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True
}


class Song(APIView):
    queryset = Song.objects.all()
    serializer_class = SongSerialiser #here i listed serialiser

    def get(self,request,format=None): #creat function
        songs = []
        res = []
        query = request.GET["query"]
        count = int(request.GET["count"])

        print(query)
        response = requests.get(
            f"https://www.youtube.com/results?search_query={query} song")

        soup = BeautifulSoup(response.text, 'html.parser')

        for aas in soup.find_all('a'):
            if aas['href'].startswith('/watch?v='):
                if aas['href'] not in songs:
                    songs.append(aas['href'])

        for sngs in songs[:count]:
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
        message = {
            'data' : res

            }

        return Response(message)
