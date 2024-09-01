import os
import sys
import pytesseract
from PIL import Image
import pandas as pd
import re

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def clean_text(text):
    corrections = {
        r're[\).]{0,2}[\s\(\.]*catract': 're cataract',
        r'[^\w\s]': '',
        r'\s{2,}': ' '
    }
    
    for pattern, replacement in corrections.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    return text

def extract_provisional_diagnosis(text):
    text = clean_text(text)
    diagnosis_match = re.search(r'Provisional Diagnosis\s*[:\-]?\s*(.*)', text, re.IGNORECASE)
    
    if diagnosis_match:
        diagnosis = diagnosis_match.group(1).strip()
    else:
        diagnosis = None

    return diagnosis

def save_to_csv(data, output_path):
    df = pd.DataFrame(data, columns=["file_name", "provisional_diagnosis"])
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

def process_file(image_path):
    data = []
    if image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        text = extract_text_from_image(image_path)
        provisional_diagnosis = extract_provisional_diagnosis(text)
        file_name = os.path.basename(image_path)
        data.append((file_name, provisional_diagnosis))
    
    output_csv = os.path.join(os.path.dirname(image_path), 'provisional_diagnoses.csv')
    save_to_csv(data, output_csv)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    process_file(image_path)

if __name__ == "__main__":
    main()
