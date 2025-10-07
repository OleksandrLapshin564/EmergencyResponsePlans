# presentation/utils/generate_pdf_6.py

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
import os

# Resource folder (image)
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '../assets/images')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../output')  # Now the PDF will be here

def generate_slide_6(output_path=None):
    if output_path is None:
        output_path = os.path.join(OUTPUT_DIR, 'presentation_6.pdf')

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    # Text for the slide
    text_lines = [
        "What you need to know when starting to develop a PLAS",
        "1. A feature of the PLAS development is that it is more convenient to develop it as a single document for the entire enterprise. This approach guarantees the definition of a clear analysis of the enterprise's hazard, taking into account the hazard of each hazardous facility located on the territory of the enterprise.",
        "2. Taking into account the above, the PLAS should consist of the following separate documents:",
        " - an analytical part, which describes all the characteristics of the enterprise and the hazardous facilities located on its territory;",
        " - separate operational parts for levels 'A', 'B', 'C', developed as separate books for each hazardous facility.",
        "3. The development of the PLAS in this form allows:",
        " - to ensure a quick search for information regarding the hazard of a specific facility;",
        " - in the event of an accident, use exactly the book that is intended for the corresponding level of accident at a specific facility;",
        " - to keep the relevant books with the managers of those facilities to which they directly relate;",
        " - to ensure a high-quality study of the entire PLAS.",
        "Sample PLAS on the example of JSC 'APRM', on the territory of which there are 2 hazardous facilities:",
        " - ammonia refrigeration station;",
        " - fuel and lubricants warehouse (gas station).",
        "BOOK 1. ANALYTICAL PART for JSC 'APRM'",
        "Refrigeration station",
        "BOOK 2. OPERATIONAL PART for level 'A'",
        "BOOK 3. OPERATIONAL PART for level 'B'",
        "BOOK 4. OPERATIONAL PART for level 'B'",
        "Fuel and lubricants warehouse (gas station)",
        "BOOK 5. OPERATIONAL PART for level 'A'",
        "BOOK 6. OPERATIONAL PART for level 'B'",
        "BOOK 7. OPERATIONAL PART for level 'B'"
    ]

    # Adding text to PDF
    for line in text_lines:
        content.append(Paragraph(line, styles['Normal']))
        content.append(Spacer(1, 12))

    # Add a picture after all the text
    img_file = "ERP_22.jpg"
    img_path = os.path.join(ASSETS_DIR, img_file)
    if os.path.exists(img_path):
        # indent before image
        content.append(Spacer(1, 24))
        content.append(Image(img_path, width=18*cm, height=10*cm))
    else:
        print(f"Warning: Image {img_file} not found in {ASSETS_DIR}")

    # PDF generation
    doc.build(content)
    print(f"✅ PDF generated successfully at {output_path}")

if __name__ == "__main__":
    generate_slide_6()
