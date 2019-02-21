'''
    Segmentation

'''


import subprocess
from pyAudioAnalysis import audioSegmentation as aS

'''
    Fixed-segment Segmentation & Classification
'''

# [flagsInd, classesAll, acc, CM] = aS.mtFileClassification("../../audio-source/SMTest/voice_speech.mp3", "pyAudioAnalysis/data/svmSM", "svm", True, 'output/voice_speech.segments')
[flagsInd, classesAll, acc, CM] = aS.mtFileClassification("pyAudioAnalysis/data/scottish.wav", "pyAudioAnalysis/data/svmSM", "svm", True, 'output/scottish.segments')

# Command-line use:
# python audioAnalysis.py segmentClassifyFile -i <inputFile> --model <model type (svm or knn)> --modelName <path to classifier model>
# Example:
# python audioAnalysis.py segmentClassifyFile -i data/scottish.wav --model svm --modelName data/svmSM

# subprocess.call("cd pyAudioAnalysis; "
#                 "python audioAnalysis.py segmentClassifyFile -i data/scottish.wav --model svm --modelName data/svmSM", shell=True)

