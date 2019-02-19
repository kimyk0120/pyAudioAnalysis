'''
    Feature Extraction
'''

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
from pydub import AudioSegment

# streo to mono
# sound = AudioSegment.from_wav("../../audio-source/wave/a2002011001-e02.wav")
# sound = sound.set_channels(1)
# sound.export("../../output/path.wav", format="wav")

# [Fs, x] = audioBasicIO.readAudioFile("pyAudioAnalysis/data/count.wav");
[Fs, x] = audioBasicIO.readAudioFile("../../output/path.wav");
# print(Fs) # frame rate
# print(x) # numpy array
# 입력 신호를 단기간 창 (프레임)으로 분할하고 각 프레임에 대한 다수의 피처를 계산
#  using a frame size of 50 msecs and a frame step of 25 msecs (50% overlap)
F, f_names = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);

# 제로 크로싱 레이트
plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[0]);

#  에너지
plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[1]);
plt.show()
