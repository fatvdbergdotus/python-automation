import argostranslate.translate

text = "The weather is beautiful today."

translated = argostranslate.translate.translate(
    text,
    "en",
    "nl"
)

print(translated)