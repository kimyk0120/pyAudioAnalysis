


'''
    Single File Classification

'''

from pyAudioAnalysis import audioTrainTest as aT

Result, P, classNames = aT.fileClassification("../../audio-source/wave/a2002011001-e02.wav", "pyAudioAnalysis/data/svmMusicGenre6","svm")
# Result, P, classNames = aT.fileClassification("../../audio-source/wave/noexcuses.wav", "pyAudioAnalysis/data/svmMusicGenre6","svm")
print(Result) # 1.0  class ID
print(P) # [0.08675024 0.55253466 0.1331328  0.04243957 0.16545349 0.01968925] probability estimate
print(classNames) # ['Blues', 'Classical', 'Electronic', 'Jazz', 'Rap', 'Rock']

# Command-line use:
# python audioAnalysis.py classifyFile -i <inputFilePath> --model <svm, svm_rbf, knn, extratrees, gradientboosting or randomforest> --classifier <pathToClassifierModeL>
# Examples:
# python audioAnalysis.py classifyFile -i bach.wav --model svm --classifier data/svmMusicGenre3
# python audioAnalysis.py classifyFile -i bach.wav --model knn --classifier data/knnMusicGenre3


'''
    Folder Classification
'''








