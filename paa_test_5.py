'''
    Regression

'''


'''
    Train Regression Models for Audio Segments
    
    
    featureAndTrainRegression(). It calls functions dirsWavFeatureExtraction() to extract the audio features and then 
    repetivelly calls evaluateRegression() to extract one optimized regression model for each learned parameter.
'''

import subprocess
from pyAudioAnalysis import audioTrainTest as aT

aT.featureAndTrainRegression("pyAudioAnalysis/data/speechEmotion/", 1, 1, aT.shortTermWindow, aT.shortTermStep, "svm", "output/svmSpeechEmotion", False)


'''
Regression task valence
Param		MSE		T-MSE		R-MSE
0.0010		0.37		0.45		0.42
0.0050		0.30		0.32		0.43
0.0100		0.29		0.28		0.43 		 best
0.0500		0.30		0.20		0.44
0.1000		0.33		0.18		0.44
0.2500		0.46		0.16		0.42
0.5000		0.62		0.15		0.44
1.0000		0.86		0.14		0.41
5.0000		1.70		0.13		0.44
10.0000		2.41		0.12		0.42
Selected params: 0.01000
Regression task arousal
Param		MSE		T-MSE		R-MSE
0.0010		0.22		0.34		0.24
0.0050		0.17		0.25		0.24 		 best
0.0100		0.20		0.22		0.26
0.0500		0.23		0.16		0.26
0.1000		0.25		0.14		0.24
0.2500		0.25		0.12		0.26
0.5000		0.30		0.11		0.25
1.0000		0.36		0.11		0.25
5.0000		0.64		0.10		0.24
10.0000		0.76		0.10		0.25
Selected params: 0.00500

The first column represents the resulting MSE for the respective SVM C param. 
The second comuns shows the MSE achieved on the training dataset (this is to provide a level of "overfitting"), 
while the last column shows the "baseline" MSE, i.e. the MSE achieved when the unknown variable is always set equal 
to the average value of the training set.

'''

# command-line use:
# subprocess.call("cd pyAudioAnalysis; "
#                 "python audioAnalysis.py trainRegression -i data/speechEmotion/ --method svm -o data/svmSpeechEmotion", shell=True)








