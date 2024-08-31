# Team Name: Cyber Spartans
# Chama Bhavesh Reddy| 2025 | VIT VELLORE
# Avala Ajitesh Reddy | 2025 | VIT VELLORE


# OCR-Based Provisional Diagnosis Extraction

This project extracts text from images, specifically focusing on identifying and extracting provisional diagnoses. The extracted text is cleaned using regular expressions to ensure accuracy. Finally, the results are saved to a CSV file.

## Features

- **Text Extraction**: Uses `pytesseract` to extract text from images.
- **Text Cleaning**: Regular expressions are applied to correct common OCR errors.
- **Provisional Diagnosis Extraction**: Searches for the provisional diagnosis in the extracted text.
- **CSV Output**: Saves the extracted data to a CSV file.

## Requirements

- Python 3.x
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow](https://pypi.org/project/Pillow/)
- [pandas](https://pypi.org/project/pandas/)


## Problem Statement

Medical Diagnosis Extraction
1. Description
Develop a solution to accurately extract medical diagnoses from handwritten medical forms to digitize medical forms and improve the efficiency as well as accuracy of claims processing.

2. Requirements
Implement a system to recognize and identify medical diagnoses from handwritten input medical forms.
Extract the value of each identified diagnosis on the handwritten form.

## Input
<img width="600" alt="image" src="https://github.com/user-attachments/assets/cc9b36ca-5c50-4771-9378-164688af8883">

## Output
In hb.csv

<img width="1267" alt="image" src="https://github.com/user-attachments/assets/6dbb15bf-918b-4eb9-ae7c-aa7c8dd1aa24">

[hb.csv](https://github.com/user-attachments/files/16825164/hb.csv)



