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

    }
]


class Song(APIView):
    queryset = Song.objects.all()
    serializer_class = SongSerialiser #here i listed serialiser

    def get(self,request,format=None): #creat function
        message = {
            'data' : data

            }

        return Response(message)





