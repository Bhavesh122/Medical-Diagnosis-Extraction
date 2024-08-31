# Team Name: Cyber Spartans
# Chama Bhavesh Reddy| 2025 | VIT VELLORE
# Avala Ajitesh Reddy | 2025 | VIT VELLORE


# OCR-Based Provisional Diagnosis Extraction

This project extracts text from medical images using Optical Character Recognition (OCR), processes the extracted text to find provisional diagnoses, and saves the results to a CSV file.

## Prerequisites

### 1. Tesseract OCR

This project requires Tesseract OCR for text extraction. Follow the installation instructions for your operating system:

- **Windows**: Download the installer from [this link](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions. Ensure that Tesseract is added to your system's PATH.
- **macOS**: Install using Homebrew with:
  ```bash
  brew install tesseract
- **Linux** Install using your package manager. For Debian-based systems:
            sudo apt-get install tesseract-ocr

### 2. Python Dependencies
pip install -r requirements.txt

## Installation
1. **Clone the repository:**

   ```bash
   git clone https://github.com/Bhavesh122/PS2-Medical-Diagnosis-Extraction.git
   cd PS2-Medical-Diagnosis-Extraction

2. Install the dependencies:
   
    pip install -r requirements.txt


## Usage
1.Configure paths: Edit the image_path and output_csv variables in main.py to specify the path to your image file and the desired output CSV file.

2. Run the script

   python main.py

## Example 
Modify the paths in main.py as follows:

if __name__ == "__main__":
    image_path = "/path/to/your/image.png"
    output_csv = "output.csv"
    main(image_path, output_csv)

Replace /path/to/your/image.png with the path to your image file and output.csv with your chosen name for the output CSV file.


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



