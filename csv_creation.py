import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import pathlib
import csv
import warnings
warnings.filterwarnings('ignore')

emg_len =[]
k = "wavfiles"
for filename in os.listdir(f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/ten_nov/Ambulance/{k}'):
    songname = f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/ten_nov/Ambulance/{k}/{filename}'
    y, sr = librosa.load(songname, mono=True)
    c = librosa.get_duration(y=y , sr=sr)
    emg_len.append(c)
print(emg_len)
nonemg_len = []
g = "road final"
for filename in os.listdir(f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/ten_nov/Road/{g}'):
    songname = f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/ten_nov/Road/{g}/{filename}'
    y, sr = librosa.load(songname, mono=True)
    d = librosa.get_duration(y=y , sr=sr)
    nonemg_len.append(d)

print(min(emg_len))
print(max(emg_len))

print(min(nonemg_len))
print(max(nonemg_len))

file = open('/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/ambulance_dataset.csv', 'w', newline='')

g = "ambulance"
for filename in os.listdir(f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/archive/{g}'):
    songname = f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/archive/{g}/{filename}'
    y, sr = librosa.load(songname, mono=True, duration=1.2)
    rmse = librosa.feature.rms(y=y)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    to_append += f' {g}'
    file = open('/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/ambulance_dataset.csv', 'a', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(to_append.split())

col_names = ["filename","chroma_stft","spectral_centroid","spectral_bandwidth","rolloff","zero_crossing_rate","mfcc1","mfcc2","mfcc3","mfcc4","mfcc5","mfcc6","mfcc7","mfcc8","mfcc9","mfcc10","mfcc11","mfcc12","mfcc13","mfcc14","mfcc15","mfcc16","mfcc17","mfcc18","mfcc19","mfcc20","label" ]
data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/ambulance_dataset.csv", names=col_names)

data.head()
file_1 = open('/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/otherSire.csv', 'w', newline='')
#files to isntall

k = "otherEmg"
for filename in os.listdir(f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/archive/{k}'):
    audioname = f'/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/archive/{k}/{filename}'
    y, sr = librosa.load(audioname, mono=True, duration=42)
    rmse = librosa.feature.rms(y=y)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    to_append += f' {k}'
    file_1 = open('/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/otherSire.csv', 'a', newline='')
    with file_1:
        writer = csv.writer(file_1)
        writer.writerow(to_append.split())

col_names = ["filename","chroma_stft","spectral_centroid","spectral_bandwidth","rolloff","zero_crossing_rate","mfcc1","mfcc2","mfcc3","mfcc4","mfcc5","mfcc6","mfcc7","mfcc8","mfcc9","mfcc10","mfcc11","mfcc12","mfcc13","mfcc14","mfcc15","mfcc16","mfcc17","mfcc18","mfcc19","mfcc20","label" ]
data_1 = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Siren/Emergency_vehicle_detection_system-master/otherSire.csv", names=col_names)

data_1.head()
print(data.label.value_counts())
print(data_1.label.value_counts())
train = pd.concat([data , data_1])
print(data.shape)
print(data_1.shape)
print(train.shape)
train.label.value_counts()