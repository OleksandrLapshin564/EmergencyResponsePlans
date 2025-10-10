from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
import os

# Paths
BASE_DIR = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(BASE_DIR, "../output/presentation_12.pdf")
IMAGE_DIR = os.path.join(BASE_DIR, "../assets/images")
IMAGE_FILE = "ERP_38.jpg"

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='NormalLeft', parent=styles['Normal'], alignment=TA_LEFT, fontSize=10, leading=12))
styles.add(ParagraphStyle(name='NormalCenter', parent=styles['Normal'], alignment=TA_CENTER, fontSize=10, leading=12))

# Create document
doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
story = []

# --- Intro text ---
intro_text = """
For cooling in the ARU system, liquid ammonia is used as the refrigerant.<br/>
The ARU operates as follows:<br/>
- The compressor (1) draws in ammonia vapor and compresses it to 2.6 MPa, heating the liquid ammonia to 65°C (max 105°C).<br/>
- The heated ammonia enters the condenser (2), where it is cooled by circulating water to 40°C.<br/>
- Oil pressure in the oil system is 1.2 bar.<br/>
- Operating oil temperature in the compressor lubrication system is 45°C (min 20°C, max 65°C).
"""
story.append(Paragraph(intro_text, styles['NormalLeft']))
story.append(Spacer(1, 12))

# --- Table 1.1.1. Hazard card of the ammonia refrigeration unit ---
story.append(Paragraph("<b>Table 1.1.1.</b> Hazard card of the ammonia refrigeration unit", styles['Normal']))
story.append(Spacer(1, 6))

data1 = [
    [
        Paragraph("<b>Equipment name</b>", styles['NormalCenter']),
        Paragraph("<b>Equipment type</b>", styles['NormalCenter']),
        Paragraph("<b>Position number on block diagram</b><br/>(see section 2.2.1 of chapter 3)", styles['NormalCenter']),
        Paragraph("<b>Equipment purpose</b><br/>(typical technological operation performed in the apparatus)", styles['NormalCenter']),
    ],
    [
        Paragraph("Cylinders for refilling the ARU system", styles['NormalLeft']),
        Paragraph("Portable metal cylinders", styles['NormalLeft']),
        Paragraph("Not stored on-site; delivered and used by the ARU manufacturer on separate order", styles['NormalLeft']),
        Paragraph("Refilling the ARU system with ammonia after draining during maintenance, or when ammonia is insufficient", styles['NormalLeft']),
    ],
    [
        Paragraph("Compressor unit", styles['NormalLeft']),
        Paragraph("Screw compressor SAB 163 Hf", styles['NormalLeft']),
        Paragraph("1", styles['NormalCenter']),
        Paragraph("Screw compressor designed to create high pressure in the ARU system", styles['NormalLeft']),
    ]
]

col_widths1 = [120, 120, 140, 180]

table1 = Table(data1, colWidths=col_widths1)
table1.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.8, colors.black),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4),
]))
story.append(table1)
story.append(Spacer(1, 12))

# --- Table 1.1.2. Characteristics of hazardous substances ---
story.append(Paragraph("<b>Table 1.1.2.</b> Characteristics of hazardous substances in ammonia refrigeration units", styles['Normal']))
story.append(Spacer(1, 6))

data2 = [
    [
        Paragraph("<b>№</b>", styles['NormalCenter']),
        Paragraph("<b>Hazardous substance</b>", styles['NormalCenter']),
        Paragraph("<b>Hazard class</b>", styles['NormalCenter']),
        Paragraph("<b>MAC (mg/m³)</b>", styles['NormalCenter']),
        Paragraph("<b>Quantity (m³)</b>", styles['NormalCenter']),
        Paragraph("<b>Quantity (tons)</b>", styles['NormalCenter']),
    ],
    [Paragraph("1", styles['NormalCenter']),
     Paragraph("Ammonia", styles['NormalLeft']),
     Paragraph("4", styles['NormalCenter']),
     Paragraph("20", styles['NormalCenter']),
     Paragraph("0.36", styles['NormalCenter']),
     Paragraph("0.085", styles['NormalCenter'])]
]

col_widths2 = [30, 150, 50, 50, 50, 50]

table2 = Table(data2, colWidths=col_widths2)
table2.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.8, colors.black),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4),
]))
story.append(table2)
story.append(Spacer(1, 12))

# --- Image ERP_38.jpg ---
image_path = os.path.join(IMAGE_DIR, IMAGE_FILE)
if os.path.exists(image_path):
    img = Image(image_path, width=400, height=250)  # підбираєте розмір
    story.append(Paragraph("1.1.1. Description of the technological process in ammonia refrigeration units", styles['Normal']))
    story.append(Spacer(1, 6))
    story.append(img)
    story.append(Spacer(1, 12))
else:
    story.append(Paragraph(f"Image not found: {IMAGE_FILE}", styles['Normal']))

# --- Build PDF ---
doc.build(story)
print("✅ PDF generated successfully:", OUTPUT_PATH)
