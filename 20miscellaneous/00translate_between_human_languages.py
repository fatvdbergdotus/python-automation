import argostranslate.translate
import argostranslate.package
# py -m pip install argostranslate


# install translation package if not already installed
def install_translation_package(source: str, target: str):

    print(f"Searching translation model: {source} -> {target}")

    available_packages = argostranslate.package.get_available_packages()

    package = next(
        (
            p for p in available_packages
            if p.from_code == source and p.to_code == target
        ),
        None
    )

    if package is None:
        raise ValueError(
            f"No translation package available: {source} -> {target}"
        )

    print("Downloading translation model...")

    download_path = package.download()

    argostranslate.package.install_from_path(download_path)

    print("Translation model installed successfully.")


# translate text using the installed translation package
def translate_text(
    text: str,
    source: str,
    target: str
) -> str:
    install_translation_package(source, target)

    languages = argostranslate.translate.get_installed_languages()

    source_language = next(
        (lang for lang in languages if lang.code == source),
        None
    )

    target_language = next(
        (lang for lang in languages if lang.code == target),
        None
    )

    if source_language is None or target_language is None:
        raise ValueError("Source or target language is not installed.")

    translation = source_language.get_translation(target_language)

    if translation is None:
        raise ValueError(
            f"Translation unavailable: {source} -> {target}. "
            "Install the corresponding language package."
        )

    return translation.translate(text)


# Example usage of the translation functions
# Define the text to be translated
english_text = "Good morning, how are you doing today?"

# Translate the text into different languages
for target_language in ["de", "nl", "es"]:
    print(translate_text(english_text, "en", target_language))