import pytesseract
from PIL import Image
import pandas as pd
import re
import os

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
    # Clean the text first
    text = clean_text(text)

    diagnosis = None

  
    diagnosis_match = re.search(r'Provisional Diagnosis\s*[:\-]?\s*(.*)', text, re.IGNORECASE)
    
    if diagnosis_match:
        diagnosis = diagnosis_match.group(1).strip()
    else:
        
        possible_diagnoses = re.findall(r'(diagnosis[:\-]?\s*(.*))', text, re.IGNORECASE)
        if possible_diagnoses:
            diagnosis = possible_diagnoses[0][1].strip()

    return diagnosis


def save_to_csv(data, output_path):
    df = pd.DataFrame(data, columns=["file_name", "provisional_diagnosis"])
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

def main(image_path, output_csv):
  
    text = extract_text_from_image(image_path)
    
   
    provisional_diagnosis = extract_provisional_diagnosis(text)
    
   
    file_name = os.path.basename(image_path)
    

    data = [(file_name, provisional_diagnosis)]
    

    save_to_csv(data, output_csv)

if __name__ == "__main__":

    image_path = "/Users/bhaveshreddy/Downloads/PS2-Samples-HackRX5 2/Sample7.png"
    output_csv = "hb.csv"
    
    main(image_path, output_csv)
