# Team Name: Cyber Spartans
# Chama Bhavesh Reddy| 2025 | VIT VELLORE
# Avala Ajitesh Reddy | 2025 | VIT VELLORE


# OCR-Based Provisional Diagnosis Extraction

This project extracts text from medical images using Optical Character Recognition (OCR), processes the extracted text to find provisional diagnoses, and saves the results to a CSV file.

## How to run the code:
1 Save the script as main.py. </br>
2  Run the script using the updated file path:
Keep the path ready </br>

On macOS or Linux: </br>

python main.py /Users/bhaveshreddy/Downloads/PS2-Samples-HackRX/Sample5.png       

</br>
On Windows (using Command Prompt or PowerShell): </br>

python main.py "C:\Users\bhaveshreddy\Downloads\PS2-Samples-HackRX\Sample5.png" </br>

Output would be in the same path , file name provisional_diagnoses.csv  </br>

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
In provisional_diagnoses.csv

<img width="1248" alt="Screenshot 2024-09-01 at 12 52 06 PM" src="https://github.com/user-attachments/assets/5759b17d-4a4d-4702-ad1a-e897ac479e88">


[provisional_diagnoses.csv](https://github.com/user-attachments/files/16827814/provisional_diagnoses.csv)

## PowerPoint Presentation


[final_submission_VIT_2025.pptx](https://github.com/user-attachments/files/16827815/final_submission_VIT_2025.pptx)



