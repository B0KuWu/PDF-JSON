import os
import json
from pdf2image import convert_from_path
import pytesseract

def ocr_pdf_to_json(pdf_path, json_path, lang='eng', poppler_path=None):
    """
    Convert a scanned PDF to a JSON file using OCR.
    
    Args:
        pdf_path (str): Path to the input PDF file.
        json_path (str): Path to the output JSON file.
        lang (str): Language for OCR. Default is 'eng'.
        poppler_path (str): Path to the Poppler 'bin' folder (optional, needed on Windows).
    """
    try:
        print(f"[INFO] Converting PDF to images: {pdf_path}")
        images = convert_from_path(pdf_path, poppler_path=poppler_path)

        extracted_data = []

        for i, image in enumerate(images):
            print(f"[INFO] Performing OCR on page {i + 1}...")
            text = pytesseract.image_to_string(image, lang=lang)
            extracted_data.append({
                "page": i + 1,
                "text": text.strip()
            })

        print(f"[INFO] Writing extracted text to JSON: {json_path}")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(extracted_data, f, ensure_ascii=False, indent=4)

        print("[SUCCESS] PDF converted to JSON successfully!")

    except Exception as e:
        print(f"[ERROR] {str(e)}")

# ------------------------
# 🧪 Example usage:
# ------------------------
if __name__ == "__main__":
    input_pdf = r"C:\Users\brian\OneDrive\Desktop\JSONCOnvert\FASA 7905 - Shadowrun Companion - Beyond the Shadows.pdf"
    output_json = "output.json"

    # 👇 Set this only if you're on Windows and Poppler is not in your PATH
    poppler_bin_path = r"C:\Users\brian\OneDrive\Desktop\JSONCOnvert\poppler-24.08.0\Library\bin"  # <-- change this as needed

    ocr_pdf_to_json(input_pdf, output_json, poppler_path=poppler_bin_path)
    images = convert_from_path(pdf_path, poppler_path=poppler_bin_path)
