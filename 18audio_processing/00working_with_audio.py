import pydub
#py -m pip install pydub    

from pydub import AudioSegment

# Load an audio file
audio = AudioSegment.from_wav("beat.wav")
# Reverse the audio
reverse_audio = audio.reverse()
# Export the reversed audio
audio.export("reverse.wav", format="wav")

# Extract the first two seconds of the audio
first_two_seconds_audio = audio[:2000]
first_two_seconds_audio.export("first_two_seconds.wav", format="wav")

# Merge the reversed audio twice with the first two seconds of the original audio with a one-second silence in between
merged_audio = reverse_audio * 2 + AudioSegment.silent(duration=1000) + first_two_seconds_audio
merged_audio.export("merged.wav", format="wav")

# Increase the volume of the merged audio
louder_merged_audio = merged_audio + 10
louder_merged_audio.export("louder_merged.wav", format="wav")