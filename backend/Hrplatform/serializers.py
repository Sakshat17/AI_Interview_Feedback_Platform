from rest_framework import serializers
from .models import Audio_store1

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio_store1
        fields = ('id', 'video','wpm','pauses','meanpitch','duration','pronunciation','balance','Spotwords','Sensitivewords','Fillerwords','freq')
        