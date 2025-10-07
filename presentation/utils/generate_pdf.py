from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
import os

# Шлях до папки assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '../assets')

def generate_presentation(output_path="/app/output/presentation.pdf"):
    # Переконайтеся, що папка output існує
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Створюємо PDF документ
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    # ===============================
    # Перші два слайди тут уже існують
    # content.append(Paragraph(...))
    # ===============================

    # ======= ТРЕТІЙ СЛАЙД =========
    third_slide_text = """
    On June 22, 2023, the State Emergency Service of the State Emergency Service of Ukraine,
    together with the technical managers and chief specialists of PrJSC "TSGZK" and PJSC "ArcelorMittal Kryvyi Rih",
    held a meeting to agree on plans for liquidation of accidents.
    <br/><br/>
    The issues were considered:
    <ul>
        <li>the possibility of backup water supply (in case of disconnection of centralized water supply)
            of surface fire-fighting tanks located on the territory of industrial sites of mines
            from the mine drainage network;</li>
        <li>the possibility of performing emergency and rescue operations in mining operations
            in the event of a global long-term power outage at the facilities of the mine management
            for underground ore mining (as mines) and DF-3,4 RU of the General Directorate of PJSC "ArcelorMittal Kryvyi Rih";</li>
        <li>results of comprehensive inspections of the readiness of mines to rescue people,
            eliminate accidents and minimize their consequences before developing and agreeing on the PLA;</li>
        <li>agreement and determination of the forces and means necessary to implement
            the operational part of the mine accident elimination plans.</li>
    </ul>
    """
    content.append(Paragraph(third_slide_text, styles['Normal']))
    content.append(Spacer(1, 1*cm))

    # Додаємо зображення
    images = ["ERP_3.jpg", "ERP_4.jpg", "ERP_5.jpg", "ERP_6.jpg", "ERP_7.jpg"]
    for img_name in images:
        img_path = os.path.join(ASSETS_DIR, 'images', img_name)
        if os.path.exists(img_path):
            content.append(Image(img_path, width=18*cm, height=10*cm))
            content.append(Spacer(1, 0.5*cm))
        else:
            print(f"⚠️ Image not found: {img_path}")

    # Генеруємо PDF
    doc.build(content)
    print(f"✅ PDF generated successfully at {output_path}")

if __name__ == "__main__":
    generate_presentation()
