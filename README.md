# Python Automation

A collection of Python scripts for automating files, PDFs, APIs, emails, web browsers, financial data, and applications.

## Contents

- [📄 PDF Automation](#-pdf-automation--00pdf)
- [🌐 API Automation](#-api-automation--01apis)
- [📁 Files & Folders](#-files--folders--02_files_and_folders)
- [📧 Email Automation](#-email-automation--03emails)
- [📈 Stock Automation](#-stock-automation--04stocks)
- [🌍 Browser Automation](#-browser-automation--05browser_automation)
- [🐍 Modern Python Tools](#-modern-python-tools--06modern_python_tools)
- [🖥️ Web Apps & Desktop GUI Apps](#-web-apps--desktop-gui-apps--07web_apps_and_desktop_gui_apps)

---

## 📄 PDF Automation — `00pdf`

Scripts for creating and processing PDF documents.

| File | Description |
|---|---|
| [`00create_pdf.py`](00pdf/00create_pdf.py) | Creates a PDF document with text and images. |
| [`01create_pdf_from_excel.py`](00pdf/01create_pdf_from_excel.py) | Creates PDF documents from Excel data. |
| [`02extract_text_from_pdf.py`](00pdf/02extract_text_from_pdf.py) | Extracts text from PDF files. |
| [`03extract_tables_from_pdf.py`](00pdf/03extract_tables_from_pdf.py) | Extracts tables from PDFs and exports them to Excel/CSV. |

---

## 🌐 API Automation — `01apis`

Examples of interacting with web APIs and creating REST APIs.

| File | Description |
|---|---|
| [`00get_news_from_open_news.py`](01apis/00get_news_from_open_news.py) | Retrieves news articles through a news API. |
| [`01weather_forecast_api.py`](01apis/01weather_forecast_api.py) | Retrieves weather forecast data and saves it to CSV. |
| [`02create_your_own_rest_api.py`](01apis/02create_your_own_rest_api.py) | Creates a REST API using Flask. |
| [`03grammar_correction.py`](01apis/03grammar_correction.py) | Checks text and retrieves grammar corrections through an API. |

---

## 📁 Files & Folders — `02_files_and_folders`

Scripts for automating common filesystem operations.

| File | Description |
|---|---|
| [`00add_prefix_to_all_filenames_in_folder.py`](02_files_and_folders/00add_prefix_to_all_filenames_in_folder.py) | Adds a prefix to filenames in a folder. |
| [`01rename_all_files_based_on_folder.py`](02_files_and_folders/01rename_all_files_based_on_folder.py) | Renames files based on their parent folder. |
| [`02add_date_created_to_filenames.py`](02_files_and_folders/02add_date_created_to_filenames.py) | Adds the file creation date to filenames. |
| [`03change_file_extensions.py`](02_files_and_folders/03change_file_extensions.py) | Changes file extensions in bulk. |
| [`04create_empty_files_and_delete_forever.py`](02_files_and_folders/04create_empty_files_and_delete_forever.py) | Creates files and demonstrates permanent deletion. |
| [`05zip_archive.py`](02_files_and_folders/05zip_archive.py) | Creates and extracts ZIP archives. |
| [`06search_file_in_computer.py`](02_files_and_folders/06search_file_in_computer.py) | Searches recursively for files on a computer. |
| [`07delete_files_forever.py`](02_files_and_folders/07delete_files_forever.py) | Deletes files programmatically. |

> **Warning:** Some scripts permanently delete files. Use them carefully.

---

## 📧 Email Automation — `03emails`

Scripts for automating email-related tasks.

| File | Description |
|---|---|
| [`00sending_email.py`](03emails/00sending_email.py) | Sends automated emails using Python. |
| [`02send_email_to_csv_contacts.py`](03emails/02send_email_to_csv_contacts.py) | Sends personalized emails to contacts stored in CSV. |
| [`03sending_email_with_attachment.py`](03emails/03sending_email_with_attachment.py) | Sends HTML emails with file attachments. |
| [`01schedule a Python script`](03emails/01schedule%20a%20Python%20script/) | Examples for scheduling Python scripts to run automatically. |

---

## 📈 Stock Automation — `04stocks`

Scripts for retrieving financial and stock-market information.

| File | Description |
|---|---|
| [`scraper.py`](04stocks/scraper.py) | Uses Selenium to scrape stock-market information from the Zagreb Stock Exchange. |

---

## 🌍 Browser Automation — `05browser_automation`

Python scripts for automating web browsers.

| Folder / File | Description |
|---|---|
| [`05browser_automation`](05browser_automation/) | Browser automation examples using Python and Selenium. |

---

## 🐍 Modern Python Tools — `06modern_python_tools`

Examples demonstrating modern Python development tools and techniques.

| Folder / File | Description |
|---|---|
| [`06modern_python_tools`](06modern_python_tools/) | Examples using modern Python tools and development techniques. |

---

## 🖥️ Web Apps & Desktop GUI Apps — `07web_apps_and_desktop_gui_apps`

Examples of building applications with Python.

| Folder / File | Description |
|---|---|
| [`07web_apps_and_desktop_gui_apps`](07web_apps_and_desktop_gui_apps/) | Python web applications and desktop GUI applications. |

---

## 🛠️ Technologies

- Python
- Selenium
- Pandas
- Flask
- Requests
- FPDF
- PyMuPDF
- Tabula
- Yagmail
- Web scraping
- REST APIs
- JSON
- CSV
- Excel
- PDF processing
- Filesystem automation
- Email automation
- Browser automation
- Desktop GUI development
- Web application development

---

## 📂 Project Structure

```text
python-automation/
│
├── 00pdf/
│   ├── 00create_pdf.py
│   ├── 01create_pdf_from_excel.py
│   ├── 02extract_text_from_pdf.py
│   └── 03extract_tables_from_pdf.py
│
├── 01apis/
│   ├── 00get_news_from_open_news.py
│   ├── 01weather_forecast_api.py
│   ├── 02create_your_own_rest_api.py
│   └── 03grammar_correction.py
│
├── 02_files_and_folders/
│   ├── 00add_prefix_to_all_filenames_in_folder.py
│   ├── 01rename_all_files_based_on_folder.py
│   ├── 02add_date_created_to_filenames.py
│   ├── 03change_file_extensions.py
│   ├── 04create_empty_files_and_delete_forever.py
│   ├── 05zip_archive.py
│   ├── 06search_file_in_computer.py
│   └── 07delete_files_forever.py
│
├── 03emails/
│   ├── 00sending_email.py
│   ├── 02send_email_to_csv_contacts.py
│   ├── 03sending_email_with_attachment.py
│   └── 01schedule a Python script/
│
├── 04stocks/
│   └── scraper.py
│
├── 05browser_automation/
│
├── 06modern_python_tools/
│
└── 07web_apps_and_desktop_gui_apps/
