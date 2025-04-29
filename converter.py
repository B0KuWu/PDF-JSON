import pdfplumber
import json

def extract_text_from_pdf(file_path):
    text_data = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            text_data.append({
                "page": i + 1,
                "text": text.strip() if text else ""
            })
    return text_data

def save_as_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def pdf_to_json(pdf_path, json_path):
    text_data = extract_text_from_pdf(pdf_path)
    save_as_json(text_data, json_path)

if __name__ == "__main__":
    input_pdf = "FASA 7905 - Shadowrun Companion - Beyond the Shadows.pdf"       # Replace with your actual PDF file
    output_json = "output.json"     # Desired output filename
    pdf_to_json(input_pdf, output_json)
    print(f"Converted '{input_pdf}' to '{output_json}'")