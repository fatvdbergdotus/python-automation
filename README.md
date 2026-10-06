# Python Automation

A collection of practical Python examples covering automation, APIs, files and folders, email, browser automation, web and desktop applications, Google Sheets, image processing, natural language processing, databases, SMS, audio, computer control, and miscellaneous utilities.

**Python files documented: 72**

## Contents

- [00pdf](#00pdf)
- [01apis](#01apis)
- [02_files_and_folders](#02filesandfolders)
- [03emails](#03emails)
- [04stocks](#04stocks)
- [05browser_automation](#05browserautomation)
- [06modern_python_tools](#06modernpythontools)
- [07web_apps_and_desktop_gui_apps](#07webappsanddesktopguiapps)
- [08working_with_google_sheets](#08workingwithgooglesheets)
- [09image_processing](#09imageprocessing)
- [10blur_faces](#10blurfaces)
- [11text_processing](#11textprocessing)
- [12regular_expressions](#12regularexpressions)
- [13natural_language_processing](#13naturallanguageprocessing)
- [14chatbot](#14chatbot)
- [15downloading_uploading_and_sharing](#15downloadinguploadingandsharing)
- [16sql](#16sql)
- [17sms](#17sms)
- [18audio_processing](#18audioprocessing)
- [19controlling_the_computer_audio_mouse_keyboard_and_screenshotting](#19controllingthecomputeraudiomousekeyboardandscreenshotting)
- [20miscellaneous](#20miscellaneous)

## Python files

Every Python file in the repository is listed below. Descriptions are based on the source code in the repository.

### `00pdf/`

| Python file | Description |
|---|---|
| [`00create_pdf.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/00pdf/00create_pdf.py) | Creates a PDF document with FPDF, including sample text and formatting. |
| [`01create_pdf_from_excel.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/00pdf/01create_pdf_from_excel.py) | Reads tabular data with Pandas and writes the data into a PDF document with FPDF. |
| [`02extract_text_from_pdf.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/00pdf/02extract_text_from_pdf.py) | Opens a PDF with PyMuPDF (`fitz`) and extracts and prints text from its pages. |
| [`03extract_tables_from_pdf.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/00pdf/03extract_tables_from_pdf.py) | Uses Tabula to extract tables from PDF documents and work with the resulting tabular data. |

### `01apis/`

| Python file | Description |
|---|---|
| [`00get_news_from_open_news.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/01apis/00get_news_from_open_news.py) | Calls a news API with `requests` and processes the returned news information. |
| [`01weather_forecast_api.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/01apis/01weather_forecast_api.py) | Calls a weather API with `requests` and retrieves forecast information. |
| [`02create_your_own_rest_api.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/01apis/02create_your_own_rest_api.py) | Demonstrates a Flask REST API and retrieving web data with Requests/Beautiful Soup. |
| [`03grammar_correction.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/01apis/03grammar_correction.py) | Sends text to an external grammar-correction service through an HTTP request and displays the result. |

### `02_files_and_folders/`

| Python file | Description |
|---|---|
| [`00add_prefix_to_all_filenames_in_folder.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/00add_prefix_to_all_filenames_in_folder.py) | Adds a configurable prefix to files in a directory using `pathlib`. |
| [`01rename_all_files_based_on_folder.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/01rename_all_files_based_on_folder.py) | Renames files using the name of their containing folder. |
| [`02add_date_created_to_filenames.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/02add_date_created_to_filenames.py) | Reads file creation timestamps and adds the date to filenames. |
| [`03change_file_extensions.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/03change_file_extensions.py) | Changes file extensions in a directory using `pathlib`. |
| [`04create_empty_files_and_delete_forever.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/04create_empty_files_and_delete_forever.py) | Demonstrates creating empty files and permanently deleting files; use with test data only. |
| [`05zip_archive.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/05zip_archive.py) | Creates ZIP archives from files or directories using Python's `zipfile` module. |
| [`06search_file_in_computer.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/06search_file_in_computer.py) | Recursively searches the filesystem for files using `pathlib`. |
| [`07delete_files_forever.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/07delete_files_forever.py) | Permanently deletes selected files from the filesystem. |
| [`test.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/02_files_and_folders/test.py) | Small test/helper script in the filesystem-automation section. |

### `03emails/`

| Python file | Description |
|---|---|
| [`00sending_email.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/03emails/00sending_email.py) | Sends email messages with Yagmail and demonstrates repeated/scheduled email activity. |
| [`02send_email_to_csv_contacts.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/03emails/02send_email_to_csv_contacts.py) | Reads contacts from a CSV file with Pandas and sends email messages to the listed contacts. |
| [`03sending_email_with_attachment.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/03emails/03sending_email_with_attachment.py) | Sends email messages with file attachments using Yagmail. |

### `04stocks/`

| Python file | Description |
|---|---|
| [`scraper.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/04stocks/scraper.py) | Uses Selenium to collect stock information from a website and can send notifications by email. |

### `05browser_automation/`

| Python file | Description |
|---|---|
| [`00scraping_simple_text.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/05browser_automation/00scraping_simple_text.py) | Uses Selenium to open a webpage and extract simple text from it. |
| [`01login_scrape_logout.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/05browser_automation/01login_scrape_logout.py) | Automates browser login, page interaction/scraping, and logout with Selenium. |
| [`02download_stock_data.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/05browser_automation/02download_stock_data.py) | Uses Selenium to interact with a website and download stock data, then processes it with Pandas. |
| [`03scrape_currency_rate_beautiful_soup.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/05browser_automation/03scrape_currency_rate_beautiful_soup.py) | Uses Requests and Beautiful Soup to scrape a currency exchange rate from a webpage. |

### `06modern_python_tools/`

| Python file | Description |
|---|---|
| [`00create_and_publish_website.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/06modern_python_tools/00create_and_publish_website.py) | Minimal Flask example for creating a Python web application/website. |

### `07web_apps_and_desktop_gui_apps/`

| Python file | Description |
|---|---|
| [`00volume_calculator_flask.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/07web_apps_and_desktop_gui_apps/00volume_calculator_flask.py) | Flask web application that calculates a volume from user-provided dimensions. |
| [`01sentence_builder_gui_app_pyqt6.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/07web_apps_and_desktop_gui_apps/01sentence_builder_gui_app_pyqt6.py) | PyQt6 desktop GUI demonstrating a simple sentence-builder interface. |
| [`02currency_converter_app_pyqt6.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/07web_apps_and_desktop_gui_apps/02currency_converter_app_pyqt6.py) | PyQt6 currency-converter GUI that retrieves exchange rates from the web and converts an entered amount. |
| [`03advanced_gui_layout.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/07web_apps_and_desktop_gui_apps/03advanced_gui_layout.py) | More advanced PyQt6 currency-converter example demonstrating nested vertical/horizontal layouts and web-based exchange rates. |
| [`04file_destroyer_gui_pyqt6.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/07web_apps_and_desktop_gui_apps/04file_destroyer_gui_pyqt6.py) | PyQt6 GUI for selecting files and demonstrating file deletion; the destructive deletion code is commented out by default. |
| [`05english_dictionary_gui_app.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/07web_apps_and_desktop_gui_apps/05english_dictionary_gui_app.py) | PyQt6 dictionary GUI that loads definitions from a JSON file and looks up matching words. |

### `08working_with_google_sheets/`

| Python file | Description |
|---|---|
| [`00open_a_google_sheet.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/08working_with_google_sheets/00open_a_google_sheet.py) | Demonstrates reading public Google Sheets as CSV and accessing private Google Sheets with `gspread`, including cell, row, column, and regex searches. |
| [`01edit_a_google_sheet.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/08working_with_google_sheets/01edit_a_google_sheet.py) | Demonstrates editing Google Sheets with `gspread`, updating cells/ranges, calculating a column mean, and continuously watching a cell for changes. |

### `09image_processing/`

| Python file | Description |
|---|---|
| [`00_convert_images_to_greyscale.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/09image_processing/00_convert_images_to_greyscale.py) | Converts JPEG images in the current directory to grayscale versions with OpenCV. |
| [`01resize_images.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/09image_processing/01resize_images.py) | Resizes JPEG images in the current directory to 800×600 using OpenCV. |
| [`02detect_human_faces.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/09image_processing/02detect_human_faces.py) | Uses an OpenCV Haar cascade to detect human faces, draw bounding boxes, and report face counts across images. |
| [`03adding_watermark_to_image.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/09image_processing/03adding_watermark_to_image.py) | Overlays a semi-transparent watermark in the bottom-right corner of an image. |
| [`04changing_image_background.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/09image_processing/04changing_image_background.py) | Replaces pixels matching a selected background color with pixels from a replacement background image. |
| [`05create_collage_from_multiple_images.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/09image_processing/05create_collage_from_multiple_images.py) | Loads images from a directory, arranges them into a square-ish grid, and saves the resulting collage. |

### `10blur_faces/`

| Python file | Description |
|---|---|
| [`00blur_faces.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/10blur_faces/00blur_faces.py) | Processes a video frame by frame with OpenCV face detection and produces three outputs: blurred faces, blacked-out faces, and faces replaced by a resized image. |

### `11text_processing/`

| Python file | Description |
|---|---|
| [`00create_text_file_and_write_and_read_content.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/11text_processing/00create_text_file_and_write_and_read_content.py) | Creates a text file, writes and reads content, and demonstrates removing the final character with file seek/truncate operations. |
| [`01replace_word_from_multiple_files.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/11text_processing/01replace_word_from_multiple_files.py) | Replaces a word in every file in a directory and then demonstrates reversing the replacement. |
| [`02merge_txt_and_csv_files.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/11text_processing/02merge_txt_and_csv_files.py) | Merges all TXT and CSV files in a directory into combined files, with one version retaining headers and another removing the first line from each input. |
| [`03replace_line_from_txt_file.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/11text_processing/03replace_line_from_txt_file.py) | Replaces a specified line number in a text file and writes the updated contents back to disk. |

### `12regular_expressions/`

| Python file | Description |
|---|---|
| [`00extract_information.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/12regular_expressions/00extract_information.py) | Uses regular expressions to extract structured information such as email addresses, URLs, IP addresses, and phone numbers from text. |
| [`01filter_files.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/12regular_expressions/01filter_files.py) | Filters filenames with a regular expression to select files matching a November date pattern between the 1st and 20th. |
| [`02find_in_text.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/12regular_expressions/02find_in_text.py) | Uses regular expressions to find records containing specific locations and combinations of email addresses or phone numbers. |

### `13natural_language_processing/`

| Python file | Description |
|---|---|
| [`00_finding_lemma.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/13natural_language_processing/00_finding_lemma.py) | Uses NLTK lemmatization and TF-IDF/cosine similarity to compare words and sentences based on their normalized forms. |
| [`01sentiment_analysis.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/13natural_language_processing/01sentiment_analysis.py) | Uses NLTK VADER to classify text as positive, negative, or neutral and prints sentiment scores for sample text and tweets. |
| [`02mood_from_speech.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/13natural_language_processing/02mood_from_speech.py) | Transcribes an audio file with SpeechRecognition and applies VADER sentiment analysis to estimate the mood expressed in the speech. |
| [`03translate.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/13natural_language_processing/03translate.py) | Demonstrates local English-to-Dutch translation with Argos Translate. |

### `14chatbot/`

| Python file | Description |
|---|---|
| [`00wikipedia.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/14chatbot/00wikipedia.py) | Builds a simple Wikipedia-based question-answering chatbot using NLTK lemmatization and TF-IDF/cosine similarity against Wikipedia article text. |

### `15downloading_uploading_and_sharing/`

| Python file | Description |
|---|---|
| [`download_and_upload_and_share_a_file.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/15downloading_uploading_and_sharing/download_and_upload_and_share_a_file.py) | Downloads a file with Requests and demonstrates uploading a file to Filestack and obtaining its hosted URL. |

### `16sql/`

| Python file | Description |
|---|---|
| [`00retrieve_data.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/16sql/00retrieve_data.py) | Queries a SQLite database table named `ips` with several SELECT, filtering, ordering, and LIKE examples. |
| [`01output_to_csv_excel_and_pdf.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/16sql/01output_to_csv_excel_and_pdf.py) | Reads SQLite data into Pandas and exports the result to CSV, Excel, and PDF formats. |
| [`02insert_data_in_sql_table.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/16sql/02insert_data_in_sql_table.py) | Inserts a sample row into the SQLite `ips` table and commits the transaction. |

### `17sms/`

| Python file | Description |
|---|---|
| [`00send_sms.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/17sms/00send_sms.py) | Sends an SMS through the Twilio API using a small reusable `send_sms` function. |
| [`01amazon_price_sms_and_email_notifier.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/17sms/01amazon_price_sms_and_email_notifier.py) | Scrapes an Amazon product price and repeatedly checks for changes, sending an email notification when the observed price changes. |

### `18audio_processing/`

| Python file | Description |
|---|---|
| [`00working_with_audio.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/18audio_processing/00working_with_audio.py) | Uses Pydub to reverse, slice, concatenate, add silence to, and change the volume of WAV audio. |
| [`01overlaying_mixing_music_audio.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/18audio_processing/01overlaying_mixing_music_audio.py) | Mixes and overlays multiple WAV tracks with Pydub and exports the resulting audio. |
| [`02adding_audio_effects_low_pass_filter_mono_and_stereo.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/18audio_processing/02adding_audio_effects_low_pass_filter_mono_and_stereo.py) | Applies a low-pass filter and demonstrates converting audio between mono and stereo. |
| [`03speech_recognition.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/18audio_processing/03speech_recognition.py) | Recognizes speech from a WAV file with Google Speech Recognition and translates the recognized English text into Dutch with Argos Translate. |

### `19controlling_the_computer_audio_mouse_keyboard_and_screenshotting/`

| Python file | Description |
|---|---|
| [`00screenshots.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/19controlling_the_computer_audio_mouse_keyboard_and_screenshotting/00screenshots.py) | Captures full-screen, partial-screen, monitor-specific, and repeated screenshots with MSS. |
| [`01record_transcribe_synthesize_audio.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/19controlling_the_computer_audio_mouse_keyboard_and_screenshotting/01record_transcribe_synthesize_audio.py) | Records microphone audio, saves it as WAV, transcribes it with SpeechRecognition, and uses text-to-speech to synthesize spoken output. |
| [`02controlling_the_mouse_keyboard_and_clipboard.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/19controlling_the_computer_audio_mouse_keyboard_and_screenshotting/02controlling_the_mouse_keyboard_and_clipboard.py) | Automates mouse movement/clicks, keyboard input, hotkeys, and clipboard operations with PyAutoGUI and Pyperclip. |
| [`03accessing_cpu_ram_and_harddisk_stats.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/19controlling_the_computer_audio_mouse_keyboard_and_screenshotting/03accessing_cpu_ram_and_harddisk_stats.py) | Reports CPU usage/core count, RAM usage, and disk-space statistics with Psutil. |
| [`04drawing.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/19controlling_the_computer_audio_mouse_keyboard_and_screenshotting/04drawing.py) | Uses PyAutoGUI mouse movement and dragging to draw a simple geometric shape on the screen. |

### `20miscellaneous/`

| Python file | Description |
|---|---|
| [`00translate_between_human_languages.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/20miscellaneous/00translate_between_human_languages.py) | Downloads and installs an Argos Translate language model when needed and translates text between specified languages. |
| [`01create_an_english_dictionary.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/20miscellaneous/01create_an_english_dictionary.py) | Loads an English dictionary from JSON and prints definitions for a word entered by the user. |
| [`02scan_and_detect_qr_code.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/20miscellaneous/02scan_and_detect_qr_code.py) | Detects and decodes a QR code from an image with OpenCV and opens the decoded URL in a web browser. |
| [`03generate_qr_code.py`](https://github.com/fatvdbergdotus/python-automation/blob/main/20miscellaneous/03generate_qr_code.py) | Generates QR-code images for a URL and for every URL listed in `urls.txt`. |

## Repository structure

```text
python-automation/
├── 00pdf/
│   └── 00create_pdf.py
│   └── 01create_pdf_from_excel.py
│   └── 02extract_text_from_pdf.py
│   └── 03extract_tables_from_pdf.py
├── 01apis/
│   └── 00get_news_from_open_news.py
│   └── 01weather_forecast_api.py
│   └── 02create_your_own_rest_api.py
│   └── 03grammar_correction.py
├── 02_files_and_folders/
│   └── 00add_prefix_to_all_filenames_in_folder.py
│   └── 01rename_all_files_based_on_folder.py
│   └── 02add_date_created_to_filenames.py
│   └── 03change_file_extensions.py
│   └── 04create_empty_files_and_delete_forever.py
│   └── 05zip_archive.py
│   └── 06search_file_in_computer.py
│   └── 07delete_files_forever.py
│   └── test.py
├── 03emails/
│   └── 00sending_email.py
│   └── 02send_email_to_csv_contacts.py
│   └── 03sending_email_with_attachment.py
├── 04stocks/
│   └── scraper.py
├── 05browser_automation/
│   └── 00scraping_simple_text.py
│   └── 01login_scrape_logout.py
│   └── 02download_stock_data.py
│   └── 03scrape_currency_rate_beautiful_soup.py
├── 06modern_python_tools/
│   └── 00create_and_publish_website.py
├── 07web_apps_and_desktop_gui_apps/
│   └── 00volume_calculator_flask.py
│   └── 01sentence_builder_gui_app_pyqt6.py
│   └── 02currency_converter_app_pyqt6.py
│   └── 03advanced_gui_layout.py
│   └── 04file_destroyer_gui_pyqt6.py
│   └── 05english_dictionary_gui_app.py
├── 08working_with_google_sheets/
│   └── 00open_a_google_sheet.py
│   └── 01edit_a_google_sheet.py
├── 09image_processing/
│   └── 00_convert_images_to_greyscale.py
│   └── 01resize_images.py
│   └── 02detect_human_faces.py
│   └── 03adding_watermark_to_image.py
│   └── 04changing_image_background.py
│   └── 05create_collage_from_multiple_images.py
├── 10blur_faces/
│   └── 00blur_faces.py
├── 11text_processing/
│   └── 00create_text_file_and_write_and_read_content.py
│   └── 01replace_word_from_multiple_files.py
│   └── 02merge_txt_and_csv_files.py
│   └── 03replace_line_from_txt_file.py
├── 12regular_expressions/
│   └── 00extract_information.py
│   └── 01filter_files.py
│   └── 02find_in_text.py
├── 13natural_language_processing/
│   └── 00_finding_lemma.py
│   └── 01sentiment_analysis.py
│   └── 02mood_from_speech.py
│   └── 03translate.py
├── 14chatbot/
│   └── 00wikipedia.py
├── 15downloading_uploading_and_sharing/
│   └── download_and_upload_and_share_a_file.py
├── 16sql/
│   └── 00retrieve_data.py
│   └── 01output_to_csv_excel_and_pdf.py
│   └── 02insert_data_in_sql_table.py
├── 17sms/
│   └── 00send_sms.py
│   └── 01amazon_price_sms_and_email_notifier.py
├── 18audio_processing/
│   └── 00working_with_audio.py
│   └── 01overlaying_mixing_music_audio.py
│   └── 02adding_audio_effects_low_pass_filter_mono_and_stereo.py
│   └── 03speech_recognition.py
├── 19controlling_the_computer_audio_mouse_keyboard_and_screenshotting/
│   └── 00screenshots.py
│   └── 01record_transcribe_synthesize_audio.py
│   └── 02controlling_the_mouse_keyboard_and_clipboard.py
│   └── 03accessing_cpu_ram_and_harddisk_stats.py
│   └── 04drawing.py
├── 20miscellaneous/
│   └── 00translate_between_human_languages.py
│   └── 01create_an_english_dictionary.py
│   └── 02scan_and_detect_qr_code.py
│   └── 03generate_qr_code.py
└── README.md
```

## Main topics

- **PDF automation** — creating PDFs and extracting text/tables.
- **API automation** — consuming APIs and building a REST API.
- **Files and folders** — renaming, searching, archiving, and deleting files.
- **Email** — sending messages, attachments, and CSV-based mail.
- **Stocks and browser automation** — Selenium and web scraping.
- **Web and desktop applications** — Flask and PyQt6 examples.
- **Google Sheets** — reading, searching, editing, and monitoring spreadsheets.
- **Image processing** — grayscale conversion, resizing, face detection, watermarks, backgrounds, and collages.
- **Video privacy** — detecting and obscuring faces in video.
- **Text processing and regular expressions** — manipulating text files and extracting structured information.
- **Natural language processing** — lemmatization, sentiment analysis, speech mood analysis, and translation.
- **Chatbots** — a simple Wikipedia-based similarity chatbot.
- **SQL** — SQLite queries, inserts, and data exports.
- **SMS** — Twilio messaging and price notifications.
- **Audio** — editing, mixing, effects, and speech recognition.
- **Computer control** — screenshots, audio, mouse/keyboard automation, system statistics, and drawing.
- **Miscellaneous utilities** — translation, dictionaries, and QR codes.

## Installation

Most scripts are standalone examples and require different dependencies. Install only the packages needed by the example you want to run. Examples include:

```bash
pip install requests pandas fpdf pymupdf tabula-py
pip install flask selenium beautifulsoup4
pip install pyqt6
pip install gspread
pip install opencv-python numpy
pip install nltk scikit-learn
pip install argostranslate wikipedia
pip install filestack-python
pip install twilio yagmail
pip install pydub SpeechRecognition
pip install mss sounddevice wavio pyttsx3 pyautogui pyperclip psutil
pip install qrcode
```

Some examples also require external programs, data files, browser drivers, API credentials, Google service-account credentials, or local media files.

## Running an example

From the directory containing the script, run:

```bash
python path/to/script.py
```

Many examples expect input files in the current working directory. Check the source code for filenames such as `database.db`, `dictionary.json`, `dictionary_data.json`, media files, images, or supporting model files before running an example.

## Security and credentials

Some scripts interact with external services and therefore require credentials or API keys. **Credentials should never be committed to a public repository.** Use environment variables or a local configuration file that is excluded by `.gitignore`.

Before publishing this repository, review scripts that contain service credentials, passwords, API keys, phone numbers, email addresses, or other secrets and rotate any credentials that may already have been exposed.

Scripts that delete files, control the mouse/keyboard, send email/SMS, upload files, or access external accounts should be tested carefully before use.

## Notes

- These are primarily educational and practical automation examples rather than a single integrated Python application.
- Dependency versions may need adjustment as third-party libraries change.
- Some examples depend on websites or APIs whose HTML, endpoints, authentication requirements, or terms may change.
- Several scripts use hard-coded example filenames and paths; adapt them to your environment before execution.

## Repository

[fatvdbergdotus/python-automation](https://github.com/fatvdbergdotus/python-automation)
