# Large-Scale-Audio-dataset
This repository basically represent the  audio dataset for emergency vehicle sirens and different road noises found in real-time environment.  This Audio dataset is consist of  two classes namely as emergency ambulance siren and traffic road noises. We have designed our protocol which consist of collection of this dataset through manually by integrating  microphone sensors with the laptop. 


## How we created a Audio Dataset

Initially we've installed the bullet cameras integrated with microphone sensors at different locations nearest to hospitals and busy traffic street. We measure the distances and calibrated the sound quality by recording those audios by placing our sensors nearest to the sounds and away from it. 

![recording device](https://user-images.githubusercontent.com/49900380/194926907-fa4ea9d6-1a8f-414d-ab1c-788c1f7efb21.png)


## Conversions of file
use the videoToWav.py and run it by using python3 videoToWav.py.

## Extract the features from Wav files
use the csv_creation.py to extract the features of the audio file by using the following command:
"python3 csv_creation.py"

![methodology](https://user-images.githubusercontent.com/49900380/194927123-c86f8d85-9137-42a1-a3bf-5318e9f69028.png)


## Bland Altman Representaion 

use this python Bland_altaman_spectrograms.ipynb for visualizing and verification of the data with another data by means of Standard deviation and Mean Bias.

![Ambulance_Final_Bland-Altaman_plot_](https://user-images.githubusercontent.com/49900380/154791218-cf10f8b2-97d5-4d75-bfd7-51039fb0ae03.png)

### Emergency vehicle Siren 
![emergency vehicle siren](https://user-images.githubusercontent.com/49900380/194926968-b835de25-4ed5-463b-8d83-f78e54566c06.png)


## Published Research Paper

Asif, Muhammad, Muhammad Usaid, Munaf Rashid, Tabarka Rajab, Samreen Hussain, and Sarwar Wasi. "Large-scale audio dataset for emergency vehicle sirens and road noises." Scientific Data 9, no. 1 (2022): 1-9. 
Link: https://doi.org/10.1038/s41597-022-01727-2


