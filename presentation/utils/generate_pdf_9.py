from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os

# --- Output path ---
output_path = "/app/presentation/output/presentation_9.pdf"

# --- Styles ---
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="SlideTitle", fontSize=18, leading=22, spaceAfter=12, alignment=1, textColor=colors.HexColor("#003366"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="SlideSubTitle", fontSize=13, leading=18, spaceAfter=8, textColor=colors.HexColor("#004C99"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="NormalText", fontSize=11, leading=15, spaceAfter=6, fontName="Helvetica"))
styles.add(ParagraphStyle(name="ListItem", fontSize=11, leftIndent=20, leading=15, spaceAfter=4, fontName="Helvetica"))

# --- Document ---
doc = SimpleDocTemplate(output_path, pagesize=A4,
                        rightMargin=50, leftMargin=50,
                        topMargin=50, bottomMargin=50)

elements = []

# --- Title ---
elements.append(Paragraph("Characteristics of the Refrigeration Station", styles["SlideTitle"]))
elements.append(Spacer(1, 6))

# --- Subtitle ---
elements.append(Paragraph("Main Hazards and Equipment Characteristics", styles["SlideSubTitle"]))
elements.append(Spacer(1, 12))

# --- Image ---
image_path = "/app/presentation/assets/images/ERP_28.jpg"
if os.path.exists(image_path):
    img = Image(image_path, width=5.5*inch, height=3.5*inch)
    img.hAlign = "CENTER"
    elements.append(img)
    elements.append(Spacer(1, 12))
else:
    elements.append(Paragraph("⚠️ Image ERP_28.jpg not found.", styles["NormalText"]))
    elements.append(Spacer(1, 12))

# --- Text content ---
text_content = """
<b>1. Characteristics of the refrigeration station.</b><br/><br/>
The refrigeration station (CS) is a part of the compressor and mechanical workshop.<br/><br/>
It is located on the territory of OJSC “APRMP” in a separate brick building (18.0×12.0×6.0 m, built in 2004), surrounded by:<br/>
• North – 40–50 m: main production building<br/>
• South – 40 m: fence and warehouse buildings<br/>
• West – 25 m: container storage<br/>
• East – 15 m: boiler room<br/><br/>
The CS includes:<br/>
– 2 ammonia refrigeration units (AXA type “RAS163 HF-A”)<br/>
– “Ice” water pumps (for evaporators and consumers)<br/>
– Recirculating water pumps and tanks (60 m³ and 20 m³)<br/>
– Switchboard room and ventilation chambers<br/>
– Cooling tower “VXT-N510” (on the 2nd floor)<br/>
Each group of pumps has a reserve.<br/><br/>
Each AXA chiller is a hermetic system containing 80–85 kg of ammonia.
"""
elements.append(Paragraph(text_content, styles["NormalText"]))
elements.append(Spacer(1, 12))

# --- Section 1.1 ---
section_1_1 = """
<b>1.1 Main hazards of the refrigeration plant (brief)</b><br/><br/>
Fire safety category: “A”, fire resistance degree: II.<br/>
Ammonia vapors in contact with oily fabrics may cause explosive mixtures.<br/>
High ammonia concentration can lead to respiratory arrest; at 15–28%, even a static spark can cause an explosion.<br/>
Refrigeration equipment operates under high pressure (up to 2.6 MPa).
"""
elements.append(Paragraph(section_1_1, styles["NormalText"]))
elements.append(Spacer(1, 12))

# --- Section 1.2 ---
section_1_2 = """
<b>1.2 Equipment characteristics (brief)</b><br/><br/>
The CS is equipped with two YORK “RAS163 HF-A” ammonia units.<br/>
Each operates automatically without continuous staff presence.<br/>
Main parameters are displayed on a computer in the boiler room.<br/>
Monitoring and safe operation are ensured by duty operators working in three shifts.
"""
elements.append(Paragraph(section_1_2, styles["NormalText"]))

# --- Build PDF ---
doc.build(elements)

print(f"✅ PDF generated successfully at {output_path}")
