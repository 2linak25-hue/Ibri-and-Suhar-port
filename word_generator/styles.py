"""
Document Styles Module
Defines all Word document styles for the EMF ML Analysis report
"""

from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def apply_styles(document):
    """Apply custom styles to the document"""
    
    # Set default font
    style = document.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.color.rgb = RGBColor(51, 51, 51)
    
    # Title style
    if 'Title' in document.styles:
        title_style = document.styles['Title']
        title_style.font.name = 'Calibri Light'
        title_style.font.size = Pt(26)
        title_style.font.color.rgb = RGBColor(44, 62, 80)
        title_style.font.bold = True
    
    # Heading 1 style
    h1_style = document.styles['Heading 1']
    h1_style.font.name = 'Calibri Light'
    h1_style.font.size = Pt(18)
    h1_style.font.color.rgb = RGBColor(44, 62, 80)
    h1_style.font.bold = True
    h1_style.paragraph_format.space_before = Pt(18)
    h1_style.paragraph_format.space_after = Pt(6)
    
    # Heading 2 style
    h2_style = document.styles['Heading 2']
    h2_style.font.name = 'Calibri Light'
    h2_style.font.size = Pt(14)
    h2_style.font.color.rgb = RGBColor(52, 73, 94)
    h2_style.font.bold = True
    h2_style.paragraph_format.space_before = Pt(12)
    h2_style.paragraph_format.space_after = Pt(4)
    
    # Heading 3 style
    h3_style = document.styles['Heading 3']
    h3_style.font.name = 'Calibri'
    h3_style.font.size = Pt(12)
    h3_style.font.color.rgb = RGBColor(100, 100, 100)
    h3_style.font.bold = True
    h3_style.paragraph_format.space_before = Pt(10)
    h3_style.paragraph_format.space_after = Pt(4)
    
    # Create custom styles
    _create_custom_styles(document)
    
    return document


def _create_custom_styles(document):
    """Create additional custom styles"""
    
    # Caption style for figures/tables
    try:
        caption_style = document.styles.add_style('Figure Caption', WD_STYLE_TYPE.PARAGRAPH)
        caption_style.font.name = 'Calibri'
        caption_style.font.size = Pt(10)
        caption_style.font.italic = True
        caption_style.font.color.rgb = RGBColor(100, 100, 100)
        caption_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption_style.paragraph_format.space_before = Pt(6)
        caption_style.paragraph_format.space_after = Pt(12)
    except:
        pass  # Style already exists
    
    # Code block style
    try:
        code_style = document.styles.add_style('Code Block', WD_STYLE_TYPE.PARAGRAPH)
        code_style.font.name = 'Consolas'
        code_style.font.size = Pt(9)
        code_style.font.color.rgb = RGBColor(51, 51, 51)
        code_style.paragraph_format.left_indent = Inches(0.5)
    except:
        pass
    
    # List item style
    try:
        list_style = document.styles.add_style('Custom List', WD_STYLE_TYPE.PARAGRAPH)
        list_style.font.name = 'Calibri'
        list_style.font.size = Pt(11)
        list_style.paragraph_format.left_indent = Inches(0.25)
        list_style.paragraph_format.space_after = Pt(4)
    except:
        pass


def set_cell_shading(cell, color_hex):
    """Set cell background color"""
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), color_hex)
    cell._tc.get_or_add_tcPr().append(shading_elm)


def set_table_borders(table):
    """Set table borders"""
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement('w:tblPr')
    
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:color'), 'CCCCCC')
        tblBorders.append(border)
    
    tblPr.append(tblBorders)
    if tbl.tblPr is None:
        tbl.insert(0, tblPr)
