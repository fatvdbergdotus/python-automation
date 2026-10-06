from pydub import AudioSegment, effects

# Load an audio file
audio = AudioSegment.from_wav("beat.wav")

# Apply a low-pass filter
low_passed_audio = effects.low_pass_filter(audio, cutoff=2000)
low_passed_audio.export("low_passed.wav", format="wav")

# Convert to mono
mono_audio = audio.set_channels(1)
mono_audio.export("mono.wav", format="wav")

# Convert to stereo
stereo_audio = audio.set_channels(2)
stereo_audio.export("stereo.wav", format="wav")