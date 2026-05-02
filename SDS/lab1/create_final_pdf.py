#!/usr/bin/env python3
"""
Create comprehensive PDF from Exp1A and Exp1B notebooks
"""

import json
import re
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

def read_notebook(filepath):
    """Read and parse Jupyter notebook"""
    with open(filepath, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook.get('cells', [])
    return cells

def extract_cell_content(cell):
    """Extract content from a cell"""
    cell_type = cell.get('cell_type')
    
    if cell_type == 'markdown':
        content = ''.join(cell.get('source', []))
        return 'markdown', content
    elif cell_type == 'code':
        source = ''.join(cell.get('source', []))
        outputs = cell.get('outputs', [])
        return 'code', (source, outputs)
    
    return None, None

def parse_markdown_to_text(md_text):
    """Parse markdown to plain text, preserving structure"""
    # Remove markdown headers and format them
    lines = md_text.split('\n')
    parsed = []
    
    for line in lines:
        if line.startswith('# '):
            parsed.append(('h1', line[2:]))
        elif line.startswith('## '):
            parsed.append(('h2', line[3:]))
        elif line.startswith('### '):
            parsed.append(('h3', line[4:]))
        elif line.startswith('**') and line.endswith('**'):
            parsed.append(('bold', line[2:-2]))
        elif line.startswith('- '):
            parsed.append(('bullet', line[2:]))
        elif line.strip():
            parsed.append(('text', line))
    
    return parsed

def create_pdf_from_notebooks():
    """Create PDF from both notebooks"""
    
    # Read notebooks
    exp1a_cells = read_notebook(r'c:\Dev\DJS_Labs\SDS\lab1\Exp1A.ipynb')
    exp1b_cells = read_notebook(r'c:\Dev\DJS_Labs\SDS\lab1\Exp1B.ipynb')
    
    # Create PDF
    pdf_filename = r'c:\Dev\DJS_Labs\SDS\lab1\SDS_Lab1_Complete_Solutions.pdf'
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading1_style = ParagraphStyle(
        'Heading1Custom',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#2e5c8a'),
        spaceAfter=10,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'Heading2Custom',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#3d6b99'),
        spaceAfter=8,
        spaceBefore=6,
        fontName='Helvetica-Bold'
    )
    
    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=6,
        spaceBefore=4,
        fontName='Helvetica-Bold'
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        fontName='Courier',
        spaceAfter=6,
        spaceBefore=3,
        leftIndent=20,
        rightIndent=10,
        backColor=colors.HexColor('#f5f5f5')
    )
    
    normal_style = ParagraphStyle(
        'NormalCustom',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    # Build content
    story = []
    
    # Title Page
    story.append(Paragraph("STATISTICS FOR DATA SCIENCE", title_style))
    story.append(Paragraph("(DJS23DPC253L)", normal_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Department of Computer Science and Engineering", heading2_style))
    story.append(Paragraph("(Data Science)", heading2_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("S.Y. B.Tech. Semester IV", normal_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Lab Experiment Solutions", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Experiment 1A: Data Structures in Python", heading1_style))
    story.append(Paragraph("Experiment 1B: Measures of Central Tendency and Dispersion", heading1_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y')}", normal_style))
    story.append(PageBreak())
    
    # Process Exp1A
    story.append(Paragraph("EXPERIMENT 1A: DATA STRUCTURES IN PYTHON", title_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Add header info
    story.append(Paragraph("Date: February 3, 2026", normal_style))
    story.append(Paragraph("Aim: To study data types in Python and its functions.", normal_style))
    story.append(Paragraph("Software: Google Colab / Jupyter Notebook", normal_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Process Exp1A cells
    question_counter_a = 1
    current_section = ""
    
    for idx, cell in enumerate(exp1a_cells):
        cell_type, content = extract_cell_content(cell)
        
        if cell_type == 'markdown':
            if '**Q' in content and '.**' in content:
                # This is a question
                q_text = content.replace('**', '').strip()
                story.append(Paragraph(f"Q{question_counter_a}. {q_text}", question_style))
                question_counter_a += 1
            elif '###' in content:
                # Section header
                section_text = content.replace('###', '').replace('**', '').strip()
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph(section_text, heading2_style))
                story.append(Spacer(1, 0.08*inch))
            elif '##' in content:
                # Major header
                header_text = content.replace('##', '').replace('**', '').strip()
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph(header_text, heading1_style))
            elif content.strip():
                story.append(Paragraph(content.replace('**', ''), normal_style))
        
        elif cell_type == 'code':
            source, outputs = content
            if source.strip():
                # Add code
                code_lines = source.split('\n')
                for line in code_lines:
                    if line.strip():
                        code_text = line.replace('<', '&lt;').replace('>', '&gt;')
                        story.append(Paragraph(code_text, code_style))
                story.append(Spacer(1, 0.08*inch))
    
    story.append(PageBreak())
    
    # Process Exp1B
    story.append(Paragraph("EXPERIMENT 1B: MEASURES OF CENTRAL TENDENCY AND DISPERSION", title_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Add header info
    story.append(Paragraph("Date: February 3, 2026", normal_style))
    story.append(Paragraph("Aim: To measure central tendency and dispersion of data using Python.", normal_style))
    story.append(Paragraph("Software: Google Colab / Jupyter Notebook", normal_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Process Exp1B cells
    question_counter_b = 1
    
    for idx, cell in enumerate(exp1b_cells):
        cell_type, content = extract_cell_content(cell)
        
        if cell_type == 'markdown':
            if '**Q' in content and '.**' in content:
                # This is a question
                q_text = content.replace('**', '').strip()
                story.append(Paragraph(f"Q{question_counter_b}. {q_text}", question_style))
                question_counter_b += 1
            elif '###' in content:
                # Section header
                section_text = content.replace('###', '').replace('**', '').strip()
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph(section_text, heading2_style))
                story.append(Spacer(1, 0.08*inch))
            elif '##' in content:
                # Major header
                header_text = content.replace('##', '').replace('**', '').strip()
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph(header_text, heading1_style))
            elif content.strip():
                story.append(Paragraph(content.replace('**', ''), normal_style))
        
        elif cell_type == 'code':
            source, outputs = content
            if source.strip():
                # Add code
                code_lines = source.split('\n')
                for line in code_lines:
                    if line.strip():
                        code_text = line.replace('<', '&lt;').replace('>', '&gt;')
                        story.append(Paragraph(code_text, code_style))
                story.append(Spacer(1, 0.08*inch))
    
    # Conclusion page
    story.append(PageBreak())
    story.append(Paragraph("CONCLUSION", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    conclusion_text = """
    This laboratory exercise has successfully demonstrated:
    <br/><br/>
    <b>Experiment 1A - Data Structures in Python:</b>
    <br/>• Understanding of Python's built-in data structures (lists, tuples, dictionaries, sets)
    <br/>• Practical application of data structure operations and manipulations
    <br/>• Implementation of control flow and functions in Python
    <br/>• Best practices for data organization and retrieval
    <br/><br/>
    <b>Experiment 1B - Central Tendency and Dispersion:</b>
    <br/>• Calculation of statistical measures for data analysis
    <br/>• Understanding of how central tendency and dispersion describe datasets
    <br/>• Practical implementation using NumPy and other statistical libraries
    <br/>• Application of statistical concepts to real-world data problems
    <br/><br/>
    Both experiments provide foundational knowledge essential for data science and statistical analysis applications.
    """
    
    story.append(Paragraph(conclusion_text, normal_style))
    story.append(Spacer(1, 0.4*inch))
    
    # Signature section
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Name: ____________________________", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("SAP ID: ____________________________", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Signature of Faculty: ____________________________", normal_style))
    
    # Build PDF
    doc.build(story)
    print(f"✅ PDF created successfully: {pdf_filename}")
    return pdf_filename

if __name__ == '__main__':
    pdf_path = create_pdf_from_notebooks()
    print(f"\n📄 Final PDF: {pdf_path}")
