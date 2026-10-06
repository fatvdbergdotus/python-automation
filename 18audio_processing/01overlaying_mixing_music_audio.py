# Overlaying and mixing music/audio using pydub
import pydub
from pydub import AudioSegment

# Load two audio files
audio1 = AudioSegment.from_wav("beat.wav")
audio1 = audio1 * 2
audio2 = AudioSegment.from_wav("sax.wav")

# Overlay audio2 on top of audio1
overlayed_audio = audio1.overlay(audio2)
overlayed_audio.export("overlayed.wav", format="wav")

final = audio1 + overlayed_audio * 2 + audio2 + audio1 + audio2
final.export("final.wav", format="wav")