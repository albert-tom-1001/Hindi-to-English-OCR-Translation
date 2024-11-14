
# Hindi to English OCR Translation with Layout Preservation

## Overview
This project provides an OCR platform to translate Hindi text in PDF documents to English, while preserving the original layout, font size, and non-text elements. It utilizes OCR to extract text, translates the text from Hindi to English, and replaces it in the document, retaining the document’s appearance.

## Features
- Extracts Hindi text from PDF files using OCR (Tesseract)
- Translates Hindi text to English using the Google Translate API
- Replaces original Hindi text with English translation while preserving layout, font size, and non-text elements
- Outputs a new PDF with translated text in the same format as the original document

## Setup

### Dependencies
To run the platform, ensure the following Python libraries are installed:
- `pdf2image` - Converts PDF pages to images
- `pytesseract` - OCR engine for text detection
- `PIL (Pillow)` - Handles image processing and drawing
- `OpenCV` - Image manipulation and thresholding
- `Deep Translator` - Provides translation via Google Translate API
- `Streamlit` - Web interface for user interaction
- `ReportLab` - Converts processed images back into PDF format

Install these dependencies using pip:
```bash
pip install pdf2image pytesseract pillow opencv-python deep-translator streamlit reportlab
```

### Tesseract Setup
Tesseract is the OCR engine for text extraction. Install Tesseract based on your operating system:

- **Windows**: Download the installer from the [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).
- **Linux**: Install via package manager:
  ```bash
  sudo apt install tesseract-ocr
  ```

If Tesseract is not in your system PATH, configure its executable path in your code:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows example
```

## Usage

1. **Upload PDF**: Launch the application and upload a PDF containing Hindi text.
2. **Specify Page Range**: Specify a page range (e.g., "1-5") or process all pages if no range is specified.
3. **OCR and Translation**: Each page is converted to an image, text is extracted using OCR, translated to English, and the translated text replaces the original Hindi text while maintaining layout.
4. **Download Translated PDF**: Download the translated PDF, which preserves the layout and formatting of the original document.

## Challenges
1. **Text Detection Accuracy**: OCR accuracy depends on PDF quality. Low-quality scans or handwritten text may result in inaccuracies.
2. **Layout Preservation**: Fitting translated text within the original layout is challenging, especially with varying text lengths.
3. **Language Handling**: Google Translate may lack contextual accuracy, especially for technical or domain-specific texts.
4. **Complex PDF Structures**: Documents with images, tables, or multi-columns present additional layout-preservation challenges.

## Potential Improvements
1. **Enhanced OCR Accuracy**: Custom-trained OCR models or deep-learning-based OCR could improve accuracy.
2. **Complex Layout Handling**: Implementing layout analysis or advanced OCR could better handle multi-column or complex PDF layouts.
3. **Contextual Translation**: Domain-specific translation models could improve translation quality.
4. **Multi-Language Support**: Expanding support for additional languages could enhance platform versatility.
5. **Text Replacement Precision**: Improved algorithms for text fitting could enhance layout preservation.
6. **Performance Optimization**: Parallel processing or caching mechanisms could speed up processing for large PDFs.
7. **Interactive Feedback**: A user review option for translations could improve translation accuracy over time.

## Conclusion
This OCR platform enables Hindi to English translation in PDFs with layout preservation. Despite challenges, the platform offers a robust solution for document translation and preservation. Continuous improvements could make it an even more powerful tool for versatile document processing.
