import os
import pdf2image
import pytesseract
from PIL import Image, ImageDraw
import io
import streamlit as st
import cv2
import numpy as np
from deep_translator import GoogleTranslator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class OCRPlatform:
    def __init__(self, translator_service='google'):
        self.translator = GoogleTranslator(source='hi', target='en') if translator_service == 'google' else None

    def process_pdf(self, pdf_path, page_range=None):
        """
        Process PDF to extract, translate, and replace text within bounding boxes while preserving layout.
        """
        # Converting the  input files (pdf's) to images
        images = pdf2image.convert_from_path(pdf_path)
        if page_range:
            start, end = page_range
            images = images[start - 1:end]

        # Preparing  each pages
        translated_pages = []
        for image in images:
            processed_image = self.translate_text_in_image(image)
            translated_pages.append(processed_image)

        # Convert processed images back to PDF
        output_pdf = self.images_to_pdf(translated_pages)
        return output_pdf

    def translate_text_in_image(self, image):
        """
        Translate text within detected bounding boxes in an image.
        """
        
        gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Detect text boxes using pytesseract
        d = pytesseract.image_to_data(binary_image, lang='hin', output_type=pytesseract.Output.DICT)
        draw = ImageDraw.Draw(image)

        # Translate and replace text within each bounding box
        for i, text in enumerate(d['text']):
            if text.strip():
                # Extract the bounding box coordinates
                x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
                original_text = text.strip()
                
                # Translate text
                translated_text = self.translate_text(original_text)

                # Clear the original text area by drawing a white rectangle over it
                draw.rectangle([x, y, x + w, y + h], fill="white")

                # Add the translated text in the same location
                draw.text((x, y), translated_text, fill="black")

        return image

    def translate_text(self, text):
        """
        Translate Hindi text to English.
        """
        try:
            return self.translator.translate(text)
        except Exception as e:
            return text  

    def images_to_pdf(self, images):
        """
        Convert processed images back to a PDF.
        """
        output = io.BytesIO()
        c = canvas.Canvas(output, pagesize=letter)
        
        for img in images:
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img:
                # Save the image to a temporary file
                img.save(temp_img, format="PNG")
                temp_img_path = temp_img.name
            
            # Draw the temporary image file on the canvas
            c.drawImage(temp_img_path, 0, 0, width=letter[0], height=letter[1])
            c.showPage()
            
            # Clean up the temporary file
            os.remove(temp_img_path)
        
        c.save()
        output.seek(0)
        return output

def main():
    st.set_page_config(page_title="Hindi to English OCR Translator")
    st.title("Hindi to English OCR Translator with Layout Preservation")

    # File upload
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save uploaded file
        pdf_path = os.path.join("uploads", uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Page range input
        page_range = st.sidebar.text_input("Enter page range (e.g., 1-5)", "1-")
        try:
            start_page, end_page = map(int, page_range.split("-"))
        except ValueError:
            st.error("Please enter a valid page range (e.g., 1-5)")
            return

        # Process the PDF
        ocr_platform = OCRPlatform()
        translated_pdf = ocr_platform.process_pdf(pdf_path, (start_page, end_page))

        # Provide download link
        st.download_button(
            label="Download Translated PDF",
            data=translated_pdf,
            file_name=f"{uploaded_file.name.split('.')[0]}_translated.pdf",
            mime="application/pdf",
        )

if __name__ == "__main__":
    main()
