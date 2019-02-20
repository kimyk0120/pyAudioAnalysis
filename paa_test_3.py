import subprocess
'''
    Classification and Regression

k Nearest Neighbor kNN (implemented in the library itself)
Support Vector Machines
Random forests
Extra trees
Gradient boosting
'''

'''
    Train Segment Classifier From Data
'''
# list_of_dirs:        list of paths of directories.
# Each directory contains a signle audio class whose samples are stored in seperate WAV files.
# mt_win, mt_step:        mid-term window length and step
# st_win, st_step:        short-term window and step
# classifier_type:        "svm" or "knn" or "randomforest" or "gradientboosting" or "extratrees"
# model_name:        name of the model to be saved

'''
# Example: MusicGenre, Classes , 폴더면이 클래스명이 됨
from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["/home/tyiannak/Desktop/MusicGenre/Classical/","/home/tyiannak/Desktop/MusicGenre/Electronic/","/home/tyiannak/Desktop/MusicGenre/Jazz/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmMusicGenre3", True)
aT.featureAndTrain(["/home/tyiannak/Desktop/MusicGenre/Classical/","/home/tyiannak/Desktop/MusicGenre/Electronic/","/home/tyiannak/Desktop/MusicGenre/Jazz/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", "knnMusicGenre3", True)
aT.featureAndTrain(["/home/tyiannak/Desktop/MusicGenre/Classical/","/home/tyiannak/Desktop/MusicGenre/Electronic/","/home/tyiannak/Desktop/MusicGenre/Jazz/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "extratrees", "etMusicGenre3", True)
aT.featureAndTrain(["/home/tyiannak/Desktop/MusicGenre/Classical/","/home/tyiannak/Desktop/MusicGenre/Electronic/","/home/tyiannak/Desktop/MusicGenre/Jazz/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "gradientboosting", "gbMusicGenre3", True)
aT.featureAndTrain(["/home/tyiannak/Desktop/MusicGenre/Classical/","/home/tyiannak/Desktop/MusicGenre/Electronic/","/home/tyiannak/Desktop/MusicGenre/Jazz/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", "rfMusicGenre3", True)
aT.featureAndTrain(["/home/tyiannak/Desktop/5Class/Silence/","/home/tyiannak/Desktop/5Class/SpeechMale/","/home/tyiannak/Desktop/5Class/SpeechFemale/","/home/tyiannak/Desktop/5Class/ObjectsOther/","/home/tyiannak/Desktop/5Class/Music/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svm5Classes")
aT.featureAndTrain(["/home/tyiannak/Desktop/5Class/Silence/","/home/tyiannak/Desktop/5Class/SpeechMale/","/home/tyiannak/Desktop/5Class/SpeechFemale/","/home/tyiannak/Desktop/5Class/ObjectsOther/","/home/tyiannak/Desktop/5Class/Music/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", "knn5Classes")
aT.featureAndTrain(["/home/tyiannak/Desktop/5Class/Silence/","/home/tyiannak/Desktop/5Class/SpeechMale/","/home/tyiannak/Desktop/5Class/SpeechFemale/","/home/tyiannak/Desktop/5Class/ObjectsOther/","/home/tyiannak/Desktop/5Class/Music/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "extratrees", "et5Classes")
aT.featureAndTrain(["/home/tyiannak/Desktop/5Class/Silence/","/home/tyiannak/Desktop/5Class/SpeechMale/","/home/tyiannak/Desktop/5Class/SpeechFemale/","/home/tyiannak/Desktop/5Class/ObjectsOther/","/home/tyiannak/Desktop/5Class/Music/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "gradientboosting", "gb5Classes")
aT.featureAndTrain(["/home/tyiannak/Desktop/5Class/Silence/","/home/tyiannak/Desktop/5Class/SpeechMale/","/home/tyiannak/Desktop/5Class/SpeechFemale/","/home/tyiannak/Desktop/5Class/ObjectsOther/","/home/tyiannak/Desktop/5Class/Music/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", "rf5Classes")

# Command-line use: SM - Speeach / Music 
# python audioAnalysis.py trainClassifier -i <directory1> ... <directoryN> --method <svm, svm_rbf, knn, extratrees, gradientboosting or randomforest> -o <modelName> --beat (optional for beat extraction)
# python audioAnalysis.py trainClassifier -i classifierData/speech/ classifierData/music/ --method svm -o data/svmSM
# python audioAnalysis.py trainClassifier -i classifierData/speech/ classifierData/music/ --method knn -o data/knnSM

# python audioAnalysis.py trainClassifier -i /media/tyiannak/My\ Passport/ResearchData/AUDIO/musicGenreClassificationData/ALL_DATA/WAVs/Electronic/ /media/tyiannak/My\ Passport/ResearchData/AUDIO/musicGenreClassificationData/ALL_DATA/WAVs/Classical/ /media/tyiannak/My\ Passport/ResearchData/AUDIO/musicGenreClassificationData/ALL_DATA/WAVs/Jazz/ --method svm --beat -o data/svmMusicGenre3
# python audioAnalysis.py trainClassifier -i /media/tyiannak/My\ Passport/ResearchData/AUDIO/musicGenreClassificationData/ALL_DATA/WAVs/Electronic/ /media/tyiannak/My\ Passport/ResearchData/AUDIO/musicGenreClassificationData/ALL_DATA/WAVs/Classical/ /media/tyiannak/My\ Passport/ResearchData/AUDIO/musicGenreClassificationData/ALL_DATA/WAVs/Jazz/ --method knn --beat -o data/knnMusicGenre3
'''



# Command-Line
# subprocess.call("cd pyAudioAnalysis; "
#                 "python audioAnalysis.py ", shell=True)


