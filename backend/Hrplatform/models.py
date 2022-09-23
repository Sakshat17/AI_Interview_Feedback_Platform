from django.db import models
class Audio_store1(models.Model):
    video=models.FileField()
    #title = models.CharField(max_length=120,default='my file')
    wpm=models.IntegerField(blank=True, null=True)
    pauses=models.IntegerField(blank=True, null=True)
    meanpitch=models.CharField(max_length=120,default='')
    #Meanpitch=models.IntegerField(blank=True, null=True)
    duration=models.FloatField(blank=True,null=True)
    pronunciation=models.FloatField(blank=True,null=True)
    balance=models.FloatField(blank=True,null=True)
    Spotwords=models.CharField(max_length=120,default='')
    Sensitivewords=models.CharField(max_length=120,default='')
    Fillerwords=models.CharField(max_length=120,default='')
    freq=models.IntegerField(blank=True, null=True)

    class Meta:
        db_table='Audio_store1'