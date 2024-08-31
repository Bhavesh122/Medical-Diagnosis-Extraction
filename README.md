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
