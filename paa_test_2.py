'''
    Feature Extraction
'''

import subprocess

# Single-file feature extraction - storing to file
# speech_music_sample.wav.csv for the mid-term features and speech_music_sample.wav_st.csv
# python audioAnalysis.py featureExtractionFile -i data/speech_music_sample.wav -mw 1.0 -ms 1.0 -sw 0.050 -ss 0.050 -o data/speech_music_sample.wav

# Feature extraction - storing to file for a sequence of WAV files stored in a given path
# python audioAnalysis.py  featureExtractionDir -i data/ -mw 1.0 -ms 1.0 -sw 0.050 -ss 0.050

# Spectrogram
# python audioAnalysis.py fileSpectrogram -i data/doremi.wav

# chromagram
# python audioAnalysis.py fileChromagram -i data/doremi.wav

# Beat extraction(--plot -> 시각화 flag)
# python audioAnalysis.py beatExtraction -i data/beat/small.wav --plot
# python audioAnalysis.py beatExtraction -i data/beat/small.wav


# Command-Line
subprocess.call("cd pyAudioAnalysis; "
                "python audioAnalysis.py beatExtraction -i data/beat/small.wav --plot", shell=True)



