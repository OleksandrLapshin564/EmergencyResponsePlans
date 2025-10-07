# presentation/utils/generate_pdf_7.py

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
import os

# Resource folder (image)
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '../assets/images')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../output')

def generate_slide_7(output_filename='presentation_7_new.pdf'):
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Text for the slide
    text_lines = [
        "GENERAL PART",
        "1. The requirements of this plan for the elimination of emergency situations and accidents "
        "(hereinafter referred to as the PLAS) apply to all states of the equipment of potentially hazardous facilities of JSC 'APRM': start-up, operation, shutdown and repair.",
        "1.1. The main direction of action and implementation of the PLAS provides for the implementation "
        "of mandatory measures to ensure the localization and elimination of emergency situations (accidents) "
        "on technological equipment in the technologically prescribed mode of its operation.",
        "1.2. The PLAS provides for the procedure for the personnel of JSC 'APRM' in the event of emergencies "
        "and accidents at potentially hazardous facilities, namely: ammonia refrigeration station; gas station.",
        "1.3. The main requirements for stopping in normal mode: "
        "ammonia refrigeration unit PAC 163 HF-A are given in the Refrigeration Unit Operation Manual, 0172-100-RU, 0173-150-RUS, 0178-445-RUS, 0178-190-EN; "
        "gas station are given in the technological regulations for gas station equipment.",
        "1.4. Operational parts of the PLC for levels 'A', 'B', 'B' for the ammonia refrigeration station are given in books 2, 3, 4 of this PLC, respectively.",
        "1.5. Operational parts of the PLC for levels 'A', 'B', 'B' for the gas station are given in books 5, 6, 7 of this PLC, respectively.",
        "1.6. Considering that, in the case of commissioning and repair of the equipment of an ammonia refrigeration station and a gas station, "
        "specialists from third-party organizations may be present on the territory of the enterprise to commission, adjust or repair the equipment, "
        "their actions are provided for in the relevant sections of the operational parts of the PLAS."
    ]

    for line in text_lines:
        story.append(Paragraph(line, styles['Normal']))
        story.append(Spacer(1, 12))

    # Image
    images = ["ERP_23.jpg", "ERP_24.jpg", "ERP_25.jpg", "ERP_26.jpg"]
    for img_file in images:
        img_path = os.path.join(ASSETS_DIR, img_file)
        if os.path.exists(img_path):
            story.append(Spacer(1, 12))  # extra space before the picture
            story.append(Image(img_path, width=18*cm, height=10*cm))
            story.append(Spacer(1, 12))  # space after image
        else:
            print(f"⚠️ Warning: Image {img_file} not found in {ASSETS_DIR}")

    # PDF generation
    doc.build(story)
    print(f"✅ PDF generated successfully at {output_path}")


if __name__ == "__main__":
    generate_slide_7()
