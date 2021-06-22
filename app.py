#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:32:32 2019

@author: sakbarian
"""

from flask import Flask, render_template,request
from flask import Flask, flash, request, redirect, url_for
import numpy as np
import re
from scipy.io.wavfile import write
from scipy.io.wavfile import read
import sys 
import os
import random
import io
from werkzeug.utils import secure_filename
import soundfile as sf
import speech_recognition as sr
global google_sentence_1 
global google_sentence_2
r = sr.Recognizer()
global participant_score

participant_score=0
def Q_A_Voice(audio_file,participant_score):

    
    r.energy_threshold = 4000
    voice = sr.AudioFile(audio_file)
    with voice as source:
      #r.adjust_for_ambient_noise(source)
      audio = r.record(source)

        # recognize (convert from speech to text)
    try:
            MyText = r.recognize_google(audio)
    except:
                MyText ="Error"
    MyText = MyText.lower()
    Predted_text=MyText.split(" ")
    Sentense_1=["hello", "how", "are", "you", "today", "is", "july", "1st", "2019"]
    if len(list(set(Sentense_1)-set(Predted_text)))==0 and len(Sentense_1)-len(Predted_text) ==0:
        participant_score=participant_score+1
    else:
        print("Wrong Sentence")


    return MyText,participant_score

    
app = Flask(__name__)

@app.route('/')
def index():
	print("Here")
	global participant_score
	global google_sentence_1 
	global google_sentence_2

	participant_score=0
	return render_template("main_1.html")

@app.route('/wait_1/',methods=['GET','POST'])
def wait_1():
	global participant_score
	global google_sentence_1 
	global google_sentence_2
	print("wait")
	print(request.files['file'])
	if request.method == 'POST':
		if 'file' not in request.files:
		    return render_template("main_1.html")
		file = request.files['file']
		if file.filename == '':
			return render_template("main_1.html")
		else:
			print(file)
			filename = secure_filename(file.filename)
			in_memory_file = io.BytesIO()
			file_audio=np.asarray(read(file))
			
			write(in_memory_file, file_audio[0], file_audio[1])
			google_sentence_1,participant_score=Q_A_Voice(in_memory_file,participant_score)
			print(participant_score)
			return render_template("main_2.html")
			#return render_template("predict.html",result=str(google_sentence))


@app.route('/wait_2/',methods=['GET','POST'])
def wait_2():
	print("wait_2")
	global google_sentence_1 
	global google_sentence_2
	global participant_score
	print(request.files['file'])
	if request.method == 'POST':
		if 'file' not in request.files:
		    return render_template("main_1.html")
		file = request.files['file']
		if file.filename == '':
			return render_template("main_1.html")
		else:
			print(file)
			filename = secure_filename(file.filename)
			in_memory_file = io.BytesIO()
			file_audio=np.asarray(read(file))
			
			write(in_memory_file, file_audio[0], file_audio[1])
			google_sentence_2,participant_score=Q_A_Voice(in_memory_file,participant_score)
			print(participant_score)
			return render_template("main_3.html")

@app.route('/wait_3/',methods=['GET','POST'])
def wait_3():
	global google_sentence_1,google_sentence_2
	print("wait_3")
	global participant_score
	print(request.files['file'])
	if request.method == 'POST':
		if 'file' not in request.files:
		    return render_template("main_1.html")
		file = request.files['file']
		if file.filename == '':
			return render_template("main_1.html")
		else:
			print(file)
			filename = secure_filename(file.filename)
			in_memory_file = io.BytesIO()
			file_audio=np.asarray(read(file))
			
			write(in_memory_file, file_audio[0], file_audio[1])
			google_sentence_3,participant_score=Q_A_Voice(in_memory_file,participant_score)
			print(participant_score)
			
			return render_template("predict.html",google_sentence_3=str(google_sentence_3),participant_score=participant_score,google_sentence_1=str(google_sentence_1),google_sentence_2=str(google_sentence_2))

if __name__ == '__main__':
    app.run()
