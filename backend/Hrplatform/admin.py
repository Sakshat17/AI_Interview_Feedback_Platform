from django.contrib import admin
from .models import Audio_store1

class AudioAdmin(admin.ModelAdmin):
    list_display=('id','video','wpm','pauses','meanpitch','duration','pronunciation','balance','Spotwords','Sensitivewords','Fillerwords','freq')

# Register your models here.
admin.site.register(Audio_store1,AudioAdmin)

