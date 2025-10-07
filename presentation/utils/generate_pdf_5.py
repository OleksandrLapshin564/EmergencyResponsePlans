# presentation/utils/generate_pdf_5.py

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
import os

# Resource folder (image)
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '../assets/images')

def generate_slide_5(output_path='presentation_5.pdf'):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    # Title
    title = "Lyceum students became mine rescuers for a day"
    content.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    content.append(Spacer(1, 12))

    # Main text
    text_lines = [
        "Young students of the Kryvyi Rih Lyceum of Security Orientation and National-Patriotic Education of the DonSUVS spent an exciting day in the State Paramilitary Mine Rescue Detachment of the State Emergency Service of Ukraine.",
        "This trip was not just an excursion, but a real immersion in the world of professional rescuers.",
        "Lyceum students not only learned about the everyday work of mine rescuers, but also got a unique opportunity to see everything with their own eyes.",
        "They watched the personnel training, which took place in the training mine and at a height. This allowed them to feel the atmosphere of work, where every movement and every decision can save a life.",
        "Such meetings not only broaden the horizons, but also inspire future defenders."
    ]

    for line in text_lines:
        content.append(Paragraph(line, styles['Normal']))
        content.append(Spacer(1, 12))

    # Image
    images = [
        "ERP_14.jpg", "ERP_15.jpg", "ERP_16.jpg", "ERP_17.jpg",
        "ERP_18.jpg", "ERP_19.jpg", "ERP_20.jpg", "ERP_21.jpg"
    ]

    for img_file in images:
        img_path = os.path.join(ASSETS_DIR, img_file)
        if os.path.exists(img_path):
            content.append(Image(img_path, width=18*cm, height=10*cm))
            content.append(Spacer(1, 12))
        else:
            print(f"⚠️ Warning: Image {img_file} not found in {ASSETS_DIR}")

    # PDF generation
    doc.build(content)
    print(f"✅ PDF generated successfully at {output_path}")


if __name__ == "__main__":
    generate_slide_5()
