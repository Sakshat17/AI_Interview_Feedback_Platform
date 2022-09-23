from numpy.core.records import record
from backend.settings import BASE_DIR
from django.shortcuts import render,redirect
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse
#from models import Recording
from .forms import AudioForm
from rest_framework import viewsets
from .serializers import AudioSerializer
from .models import Audio_store1
import requests
import json
import myprosody as mysp
import pickle
import crepe
from scipy.io import wavfile
import winsound    
from urllib.request import urlretrieve
import speech_recognition as sr
import librosa
from playsound import playsound
import parselmouth
#from parselmouth.praat import call, run_file
import glob
import pandas as pd
import numpy as np
import scipy
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
import os
from urllib.parse import quote
from .models import Audio_store1

class AudioView(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    queryset = Audio_store1.objects.all()


def run_praat_file(m, p):
    """
    p : path to dataset folder
    m : path to file
    returns : objects outputed by the praat script
    """
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"

    assert os.path.isfile(sound), "Wrong path to audio file"
    assert os.path.isfile(sourcerun), "Wrong path to praat script"
    assert os.path.isdir(path), "Wrong path to audio files"

    try:
        objects= parselmouth.praat.run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        return z2
    except:
        z3 = 0
        print ("Try again the sound of the audio was not clear")

def mysppron(m,p):
    """
    Pronunciation posteriori probability score percentage
    """

    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= parselmouth.praat.run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[13]) # will be the integer number 10
        z4=float(z2[14]) # will be the floating point number 8.3
        db= binom.rvs(n=10,p=z4,size=10000)
        a=np.array(db)
        b=np.mean(a)*100/10
        #print ("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (b))
        return b
    except:
        print ("Try again the sound of the audio was not clear")
    return 0

def mysppaus(m,p):
    """
    Detect and count number of fillers and pauses
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[1]) # will be the integer number 10
    z4=float(z2[3]) # will be the floating point number 8.3
    return z3

def myspsr(m,p):
    """
    Measure the rate of speech (speed)
    """
    z2 = run_praat_file(m, p)
    z3=int(float(z2[2])) # will be the integer number 10
    z4=float(z2[3]) # will be the floating point number 8.3
    return z3

def myspatc(m,p):
    """
    Measure the articulation (speed)
    """
    z2 = run_praat_file(m, p)
    z3=int(float(z2[3])) # will be the integer number 10
    z4=float(z2[3]) # will be the floating point number 8.3
    return z3

def myspbala(m,p):
    """
    Measure ratio between speaking duration and total speaking duration
    """
    z2 = run_praat_file(m, p)
    z3=int(float(z2[3])) # will be the integer number 10
    z4=float(z2[6]) # will be the floating point number 8.3
    return z4

def myspod(m,p):
    """
    Measure total speaking duration (inc. fillers and pauses)
    """
    z2 = run_praat_file(m, p)
    z3=int(float(z2[3])) # will be the integer number 10
    z4=float(z2[5]) # will be the floating point number 8.3
    return z4


def Audio_store(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            filename2 = form.cleaned_data['video']# name of file +.wav
            #new_path = settings.MEDIA_ROOT + "\\" + filename2  # complete path
            new_path2 =r"C:\Users\Priyanshi\Desktop\New folder (2)\backend\myprosody" # path for myprosody
            p2=str(filename2)
            filename3=p2[0:len(p2)-4] # removed .wav 
            print(filename3)
            pron=mysppron(filename3,new_path2)
            pause=mysppaus(filename3,new_path2)
            sr=myspsr(filename3,new_path2)
            atc=myspatc(filename3,new_path2)
            balance=myspbala(filename3,new_path2)
            dur=myspod(filename3,new_path2)
            
            New_obj=Audio_store1(video=filename2)
            New_obj.wpm=atc
            New_obj.pronunciation=pron
            New_obj.balance=balance
            New_obj.duration=dur
            New_obj.pauses=pause
            New_obj.save()
            return redirect("result/"+str(New_obj.id))
    else: 
        form = AudioForm() 
    return render(request, 'index.html',{'form' : form}) 


def result(request,obj_id):
    obj=Audio_store1.objects.get(pk=obj_id)
    context=dict(video_info=obj)
    return render(request,'result.html',context)

def home(request):
    response = requests.get('http://127.0.0.1:8000/api/Audio/')
    audio = response.json()
    file2=audio[len(audio) -1]   # index of json
    response2=file2['video']  # url to audio file
    id1=file2['id']
    url = response2
    filename2 = url.split("/")[-1]  # name of file +.wav
    new_path = settings.MEDIA_ROOT + "\\" + filename2  # complete path
    new_path2 =r"C:\Users\Priyanshi\Desktop\New folder (2)\backend\myprosody" # path for myprosody
    p=response2
    filename3=filename2[0:len(filename2)-4] # removed .wav 
    print(filename3)
    #playsound(new_path)
    print('playing sound using  playsound')
    pron=mysppron(filename3,new_path2)
    print("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (pron))
    pause=mysppaus(filename3,new_path2)
    print ("number_of_pauses=",pause)
    sr=myspsr(filename3,new_path2)
    print ("rate_of_speech=",sr,"# syllables/sec original duration")
    atc=myspatc(filename3,new_path2)
    print ("articulation_rate=",atc,"# syllables/sec speaking duration")
    balance=myspbala(filename3,new_path2)
    print ("balance=",balance,"# ratio (speaking duration)/(original duration)")
    dur=myspod(filename3,new_path2)
    print ("original_duration=",dur,"# sec total speaking duration with pauses")

    id=Audio_store1.objects.get(pk=id1)
    id.wpm=atc
    id.pauses=pause
    id.balance=balance
    id.pronunciation=pron
    id.duration=dur
    id.save()
    
    return render(request, 'home.html', {
        'file': 'hey',
    })