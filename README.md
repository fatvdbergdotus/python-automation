# Python Automation

A collection of practical Python scripts for automating repetitive tasks, processing files and data, interacting with APIs, sending emails, automating web browsers, and building web and desktop applications.

The repository contains small, focused Python examples that demonstrate how Python can be used to automate everyday tasks and build useful applications.

## Contents

- [📄 PDF Automation](#-pdf-automation--00pdf)
- [🌐 API Automation](#-api-automation--01apis)
- [📁 Files & Folders](#-files--folders--02_files_and_folders)
- [📧 Email Automation](#-email-automation--03emails)
- [📈 Stock Automation](#-stock-automation--04stocks)
- [🌍 Browser Automation](#-browser-automation--05browser_automation)
- [🐍 Modern Python Tools](#-modern-python-tools--06modern_python_tools)
- [🖥️ Web Apps & Desktop GUI Apps](#-web-apps--desktop-gui-apps--07web_apps_and_desktop_gui_apps)
- [🛠️ Technologies](#-technologies)
- [🚀 Getting Started](#-getting-started)
- [📂 Project Structure](#-project-structure)
- [🎯 Purpose](#-purpose)

---

## 📄 PDF Automation — `00pdf`

Scripts for creating and processing PDF documents.

| File | Description |
|---|---|
| [`00create_pdf.py`](00pdf/00create_pdf.py) | Creates a PDF document with text and images. |
| [`01create_pdf_from_excel.py`](00pdf/01create_pdf_from_excel.py) | Creates PDF documents from Excel data. |
| [`02extract_text_from_pdf.py`](00pdf/02extract_text_from_pdf.py) | Extracts text from PDF files. |
| [`03extract_tables_from_pdf.py`](00pdf/03extract_tables_from_pdf.py) | Extracts tables from PDF files. |

**Technologies:** FPDF, Pandas, PyMuPDF, Tabula

---

## 🌐 API Automation — `01apis`

Examples of interacting with web APIs and creating REST APIs.

| File | Description |
|---|---|
| [`00get_news_from_open_news.py`](01apis/00get_news_from_open_news.py) | Retrieves news articles through an API. |
| [`01weather_forecast_api.py`](01apis/01weather_forecast_api.py) | Retrieves weather forecast information and saves it to CSV. |
| [`02create_your_own_rest_api.py`](01apis/02create_your_own_rest_api.py) | Creates a REST API using Flask. |
| [`03grammar_correction.py`](01apis/03grammar_correction.py) | Checks text for grammar errors using an API. |

**Technologies:** Requests, Flask, Pandas, REST APIs

---

## 📁 Files & Folders — `02_files_and_folders`

Scripts for automating common filesystem operations.

| File | Description |
|---|---|
| [`00add_prefix_to_all_filenames_in_folder.py`](02_files_and_folders/00add_prefix_to_all_filenames_in_folder.py) | Adds a prefix to filenames in a folder. |
| [`01rename_all_files_based_on_folder.py`](02_files_and_folders/01rename_all_files_based_on_folder.py) | Renames files based on their containing folder. |
| [`02add_date_created_to_filenames.py`](02_files_and_folders/02add_date_created_to_filenames.py) | Adds the file creation date to filenames. |
| [`03change_file_extensions.py`](02_files_and_folders/03change_file_extensions.py) | Changes file extensions. |
| [`04create_empty_files_and_delete_forever.py`](02_files_and_folders/04create_empty_files_and_delete_forever.py) | Creates empty files and demonstrates permanent deletion. |
| [`05zip_archive.py`](02_files_and_folders/05zip_archive.py) | Creates ZIP archives. |
| [`06search_file_in_computer.py`](02_files_and_folders/06search_file_in_computer.py) | Searches for files on the computer. |
| [`07delete_files_forever.py`](02_files_and_folders/07delete_files_forever.py) | Permanently deletes files. |

> ⚠️ **Warning:** Some scripts permanently delete files. Test them on non-critical files first.

**Technologies:** `pathlib`, `os`, `shutil`, ZIP archives

---

## 📧 Email Automation — `03emails`

Scripts for sending and scheduling emails using Python.

| File / Folder | Description |
|---|---|
| [`00sending_email.py`](03emails/00sending_email.py) | Sends an email using Python. |
| [`02send_email_to_csv_contacts.py`](03emails/02send_email_to_csv_contacts.py) | Sends emails to contacts stored in a CSV file. |
| [`03sending_email_with_attachment.py`](03emails/03sending_email_with_attachment.py) | Sends an email with an attachment. |
| [`01schedule a Python script`](03emails/01schedule%20a%20Python%20script/) | Examples for scheduling Python scripts. |

**Technologies:** SMTP, email, CSV

---

## 📈 Stock Automation — `04stocks`

Scripts for retrieving and processing stock-market information.

| File | Description |
|---|---|
| [`scraper.py`](04stocks/scraper.py) | Scrapes stock-market information using Selenium. |

**Technologies:** Selenium, web scraping

---

## 🌍 Browser Automation — `05browser_automation`

Examples of browser automation, web scraping, authentication, downloading data, and extracting information from websites.

| File | Description |
|---|---|
| [`00scraping_simple_text.py`](05browser_automation/00scraping_simple_text.py) | Simple browser-based web scraping. |
| [`01login_scrape_logout.py`](05browser_automation/01login_scrape_logout.py) | Logs into a website, scrapes information, and logs out. |
| [`02download_stock_data.py`](05browser_automation/02download_stock_data.py) | Downloads stock-market data using browser automation. |
| [`03scrape_currency_rate_beautiful_soup.py`](05browser_automation/03scrape_currency_rate_beautiful_soup.py) | Scrapes currency exchange rates using Beautiful Soup. |
| [`products.txt`](05browser_automation/products.txt) | Example product data used by the automation scripts. |
| [`stock_data.csv`](05browser_automation/stock_data.csv) | Stock data generated by the automation scripts. |

**Technologies:** Selenium, Beautiful Soup, web scraping

---

## 🐍 Modern Python Tools — `06modern_python_tools`

Examples of modern Python development and application-building tools.

| File | Description |
|---|---|
| [`00create_and_publish_website.py`](06modern_python_tools/00create_and_publish_website.py) | Creates and publishes a website using Python. |
| [`01streamlit.md`](06modern_python_tools/01streamlit.md) | Notes and examples for building applications with Streamlit. |

**Technologies:** Python, Streamlit, web applications

---

## 🖥️ Web Apps & Desktop GUI Apps — `07web_apps_and_desktop_gui_apps`

Examples of Python web applications and desktop GUI applications.

| File | Description |
|---|---|
| [`00volume_calculator_flask.py`](07web_apps_and_desktop_gui_apps/00volume_calculator_flask.py) | Volume calculator implemented as a Flask web application. |
| [`01sentence_builder_gui_app_pyqt6.py`](07web_apps_and_desktop_gui_apps/01sentence_builder_gui_app_pyqt6.py) | Sentence-builder desktop application using PyQt6. |
| [`02currency_converter_app_pyqt6.py`](07web_apps_and_desktop_gui_apps/02currency_converter_app_pyqt6.py) | Currency-converter desktop application using PyQt6. |
| [`03advanced_gui_layout.py`](07web_apps_and_desktop_gui_apps/03advanced_gui_layout.py) | Demonstrates an advanced PyQt6 GUI layout. |
| [`04file_destroyer_gui_pyqt6.py`](07web_apps_and_desktop_gui_apps/04file_destroyer_gui_pyqt6.py) | File-management GUI application using PyQt6. |
| [`05english_dictionary_gui_app.py`](07web_apps_and_desktop_gui_apps/05english_dictionary_gui_app.py) | English dictionary desktop application. |
| [`templates/index.html`](07web_apps_and_desktop_gui_apps/templates/index.html) | HTML template used by the Flask application. |

**Technologies:** Flask, PyQt6, HTML

---

## 🛠️ Technologies

This repository demonstrates a broad range of Python technologies and libraries:

- Python
- Pandas
- Selenium
- Beautiful Soup
- Flask
- Requests
- FPDF
- PyMuPDF
- Tabula
- Streamlit
- PyQt6
- SMTP / email
- REST APIs
- Web scraping
- JSON
- CSV
- Excel
- PDF processing
- Filesystem automation
- Browser automation
- Desktop GUI development
- Web application development

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/fatvdbergdotus/python-automation.git
cd python-automation
