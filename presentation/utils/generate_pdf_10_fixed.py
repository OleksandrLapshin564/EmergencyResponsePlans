from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def generate_slide_10_fixed():
    # Реєструємо DejaVu для кирилиці
    pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

    output_dir = "/tmp/output_tmp"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "presentation_10_fixed.pdf")

    doc = SimpleDocTemplate(output_file, pagesize=A4)

    # Стилі
    heading_style = ParagraphStyle(name='Heading1', fontName='DejaVu', fontSize=16, leading=20)
    normal_style = ParagraphStyle(name='Normal', fontName='DejaVu', fontSize=12, leading=15)

    story = []

    # Заголовок
    story.append(Paragraph("1.1.1. Block diagram of ammonia refrigeration units.", heading_style))
    story.append(Spacer(1, 12))

    # Таблиця
    data = [
        ["English term", "Ukrainian Translation"],
        ["discharge pipeline", "нагнітаючий трубопровід"],
        ["supply of cooling oil", "подача мастила на охолодження"],
        ["oil after cooling", "мастило після охолодження"],
        ["hexadecimal capacitor CPHE 100", "шестинчатий конденсатор CPHE 100"],
        ["liquid ammonia -1.5°C", "рідкий аміак -1,5°С"],
        ["\"Returning\" water on", "\"Оборотна\" вода на"],
        ["Option", "опція"],
        ["insulated housing", "ізольований корпус"],
        ["insulated evaporator tray", "ізольований піддон для випаровувача"],
        ["plate evaporator", "пластинчатий випаровувач"],
        ["liquid separator", "відокремлювач рідини"],
        ["ice water", "льодяна вода"],
        ["discharge line", "лінія нагнітання"],
        ["compressor SAB 163 HF", "компресор SAB 163 HF"],
    ]

    table_style = TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'DejaVu'),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ])

    table = Table(data, colWidths=[200, 200])
    table.setStyle(table_style)
    story.append(table)
    story.append(Spacer(1, 12))

    # Малюнки
    image_files = [
        "/app/presentation/images/ERP_29.jpg",
        "/app/presentation/images/ERP_30.jpg",
        "/app/presentation/images/ERP_31.jpg",
        "/app/presentation/images/ERP_32.jpg",
        "/app/presentation/images/ERP_33.jpg",
        "/app/presentation/images/ERP_34.jpg",
        "/app/presentation/images/ERP_35.jpg"
    ]

    for img_path in image_files:
        if os.path.exists(img_path):
            story.append(Image(img_path, width=400, height=300))
            story.append(Spacer(1,12))
        else:
            story.append(Paragraph(f"Image not found: {img_path}", normal_style))

    doc.build(story)
    print(f"✅ PDF generated successfully at {output_file}")

if __name__ == "__main__":
    generate_slide_10_fixed()
