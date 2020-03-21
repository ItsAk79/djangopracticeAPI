from rest_framework import serializers
from .models import Song

class SongSerialiser(serializers.HyperlinkedModelSerializer):

        class Meta:
            model = Song
            fields = ('id','url','title','thumbnail','artist','duration')

