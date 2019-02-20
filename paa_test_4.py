


'''
    Single File Classification

'''
import subprocess
from pyAudioAnalysis import audioTrainTest as aT

Result, P, classNames = aT.fileClassification("../../audio-source/wave/a2002011001-e02.wav", "pyAudioAnalysis/data/svmMusicGenre6","svm")
# Result, P, classNames = aT.fileClassification("../../audio-source/wave/noexcuses.wav", "pyAudioAnalysis/data/svmMusicGenre6","svm")
# print(Result) # 1.0  class ID
# print(P) # [0.08675024 0.55253466 0.1331328  0.04243957 0.16545349 0.01968925] probability estimate
# print(classNames) # ['Blues', 'Classical', 'Electronic', 'Jazz', 'Rap', 'Rock']

# Command-line use:
# python audioAnalysis.py classifyFile -i <inputFilePath> --model <svm, svm_rbf, knn, extratrees, gradientboosting or randomforest> --classifier <pathToClassifierModeL>
# Examples:
# python audioAnalysis.py classifyFile -i bach.wav --model svm --classifier data/svmMusicGenre3
# python audioAnalysis.py classifyFile -i bach.wav --model knn --classifier data/knnMusicGenre3


'''
    Folder Classification
'''

# Command-line use examples:
# python audioAnalysis.py classifyFolder -i testFolder/ --model svm --classifier data/svmSM            (only generates freq counts for each audio class)
# python audioAnalysis.py classifyFolder -i testFolder/ --model svm --classifier data/svmSM --details  (also outputs the result of each singe WAV file)

# Command-Line
# ex) data/speechEmotion/
# speech              		47
# music               		0
subprocess.call("cd pyAudioAnalysis; "
                "python audioAnalysis.py classifyFolder -i ../../../audio-source/SMTest/ --model svm --classifier data/svmSM --details", shell=True)








