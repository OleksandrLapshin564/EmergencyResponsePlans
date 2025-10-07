from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os


def generate_slide_8():
    # Path to the source PDF
    output_dir = "/app/presentation/output"
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "presentation_8.pdf")

    # Creating a PDF
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4),
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=22,
        leading=28,
        spaceAfter=20
    )
    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading2"],
        fontSize=16,
        leading=22,
        alignment=TA_LEFT,
        spaceBefore=12,
        spaceAfter=6
    )
    text_style = ParagraphStyle(
        "TextStyle",
        parent=styles["Normal"],
        fontSize=12,
        leading=18,
        alignment=TA_LEFT
    )

    story = []

    # Title
    story.append(Paragraph("Analytical Part", title_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CONTENTS", section_style))
    story.append(Spacer(1, 14))

    # Main text (all content as in the assignment)
    text = """
    <b>SECTION 1</b><br/>
    1. Terms and Definitions<br/>
    <br/>
    <b>SECTION 2</b><br/>
    2. Characteristics of the Enterprise<br/>
    2.1 General characteristics.<br/>
    2.2 Situational plan of the territory of the region affected by the hazardous effects of ammonia.<br/>
    2.3 Enterprise plan.<br/>
    <br/>
    <b>SECTION 3</b><br/>
    3. Hazard Analysis of the Enterprise<br/>
    3.1 Overview of the circumstances and causes of individual accidents that occurred at this and other enterprises.<br/>
    3.2 List of possible types of accidents at the enterprise.<br/>
    <br/>
    <b>SECTION 4 – REFRIGERATION PLANT</b><br/>
    1. Block diagram of the refrigeration plant.<br/>
    2. Characteristics of the refrigeration plant.<br/>
    2.1 Main hazards of the refrigeration plant and their characteristics.<br/>
    2.2 Characteristics of the refrigeration plant equipment.<br/>
    2.2.1 Block diagram of ammonia refrigeration units.<br/>
    2.2.2 Description of the technological process in ammonia refrigeration units.<br/>
    2.2.3 Hazard card of ammonia refrigeration unit.<br/>
    2.2.4 Characteristics of hazardous substances in ammonia refrigeration units.<br/>
    2.2.5 List of possible emergency situations in ammonia refrigeration unit.<br/>
    2.2.6 Forecasting scenarios of emergency situations (accidents) at AXA.<br/>
    2.2.7 Scenarios of gradual occurrence and development of an accident at AXA.<br/>
    2.2.8 Recognizable signs of an accident at AXA.<br/>
    2.3 Means of prevention and localization of possible accidents at a refrigeration plant.<br/>
    2.4 Analysis of the actions of production personnel and specialized units.<br/>
    2.5 Assessment of the adequacy of existing measures.<br/>
    2.6 Calculations and assessments of the hazard analysis of a refrigeration plant.<br/>
    <br/>
    <b>CHAPTER 4</b><br/>
    Recommendations for the Implementation of the PLAS<br/>
    1. Basic provisions of the PLAS for its implementation.<br/>
    2. General measures for the implementation of the PLAS.<br/>
    3. Obligations of the owner (manager) of the enterprise (facility).<br/>
    <br/>
    <b>CHAPTER 5</b><br/>
    Appendices<br/>
    """

    story.append(Paragraph(text, text_style))
    story.append(Spacer(1, 20))

    # Add a picture (ERP_27.jpg)
    image_path = "/app/presentation/assets/images/ERP_27.jpg"
    if os.path.exists(image_path):
        story.append(Spacer(1, 15))
        story.append(Image(image_path, width=24 * cm, height=14 * cm))
    else:
        story.append(Paragraph(f"⚠️ Image not found: {image_path}", text_style))

    # Створення PDF
    doc.build(story)
    print(f"✅ PDF generated successfully at {pdf_path}")


if __name__ == "__main__":
    generate_slide_8()
