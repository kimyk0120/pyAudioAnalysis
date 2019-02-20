'''
    Regression

'''


import subprocess
from pyAudioAnalysis import audioTrainTest as aT


'''
    Single File Regression
'''

R, regression_names = aT.fileRegression("../../audio-source/SMTest/voice_speech.mp3", "output/svmSpeechEmotion", "svm")
# print(R, regression_names)

'''
[1.6885207442930807, 0.1414232473571424]
['valence', 'arousal']
'''

# python audioAnalysis.py regressionFile -i anger1.wav --model svm --regression data/svmSpeechEmotion


'''
    Folder Regression
'''
# loop over each WAV file in the provided folder and calls fileRegression() using the svmSpeechEmotion model.
# python audioAnalysis.py regressionFolder -i ~/ResearchData/AUDIO/emotionSpeechData/germanSegments/Anger/ --model svm --regression data/svmSpeechEmotion
# python audioAnalysis.py regressionFolder -i ~/ResearchData/AUDIO/emotionSpeechData/germanSegments/Sadness/ --model svm --regression data/svmSpeechEmotion
# python audioAnalysis.py regressionFolder -i ~/ResearchData/AUDIO/emotionSpeechData/germanSegments/Happiness/ --model svm --regression data/svmSpeechEmotion

subprocess.call("cd pyAudioAnalysis; "  
                "python audioAnalysis.py regressionFolder -i ../../../audio-source/SMTest/ --model svm --regression data/svmSpeechEmotion", shell=True)

