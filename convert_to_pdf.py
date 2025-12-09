from fpdf import FPDF
import re

# Read the markdown file
with open(r'C:\Users\HP\Downloads\new process\stat.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Replace special characters that may cause issues
md_content = md_content.replace('χ²', '(Chi-Square)')
md_content = md_content.replace('χ', 'Chi')
md_content = md_content.replace('μ', 'mu')

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_left_margin(15)
pdf.set_right_margin(15)

# Process markdown line by line
lines = md_content.split('\n')
in_table = False
table_data = []

for line in lines:
    stripped = line.strip()
    
    # Skip empty lines
    if not stripped:
        pdf.ln(3)
        continue
    
    # Horizontal rule
    if stripped == '---':
        pdf.ln(3)
        pdf.set_draw_color(200, 200, 200)
        pdf.line(15, pdf.get_y(), 195, pdf.get_y())
        pdf.ln(3)
        continue
    
    # Headers
    if stripped.startswith('# '):
        pdf.set_font('Helvetica', 'B', 16)
        pdf.set_text_color(44, 62, 80)
        pdf.multi_cell(0, 10, stripped[2:])
        pdf.ln(2)
        continue
    elif stripped.startswith('## '):
        pdf.set_font('Helvetica', 'B', 13)
        pdf.set_text_color(52, 73, 94)
        pdf.multi_cell(0, 8, stripped[3:])
        pdf.ln(2)
        continue
    elif stripped.startswith('### '):
        pdf.set_font('Helvetica', 'B', 11)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(0, 7, stripped[4:])
        pdf.ln(2)
        continue
    
    # Table detection
    if '|' in stripped:
        # Skip separator line
        if re.match(r'^[\|\s\-:]+$', stripped):
            continue
        # Parse table row
        cells = [cell.strip() for cell in stripped.split('|')]
        cells = [c for c in cells if c]  # Remove empty strings
        if cells:
            table_data.append(cells)
        continue
    
    # If we have accumulated table data and hit a non-table line, render table
    if table_data:
        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(0, 0, 0)
        num_cols = len(table_data[0]) if table_data else 1
        col_width = 180 / num_cols
        
        for i, row in enumerate(table_data):
            if i == 0:  # Header row
                pdf.set_font('Helvetica', 'B', 8)
                pdf.set_fill_color(240, 240, 240)
                for cell in row:
                    pdf.cell(col_width, 7, cell[:35], border=1, fill=True)
                pdf.ln()
                pdf.set_font('Helvetica', '', 8)
            else:
                for cell in row:
                    pdf.cell(col_width, 7, cell[:35], border=1)
                pdf.ln()
        table_data = []
        pdf.ln(3)
    
    # List items
    if stripped.startswith('-   ') or stripped.startswith('- ') or stripped.startswith('* '):
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(51, 51, 51)
        # Clean up markdown formatting
        text = re.sub(r'^[-*]\s+', '', stripped)
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold markers
        text = re.sub(r'\*(.*?)\*', r'\1', text)  # Remove italic markers
        text = re.sub(r'`(.*?)`', r'\1', text)  # Remove code markers
        if text:
            pdf.multi_cell(0, 6, "    - " + text)
        continue
    
    # Regular paragraph
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(51, 51, 51)
    # Clean up markdown formatting
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', stripped)  # Remove bold markers
    text = re.sub(r'\*(.*?)\*', r'\1', text)  # Remove italic markers
    text = re.sub(r'`(.*?)`', r'\1', text)  # Remove code markers
    if text:
        pdf.multi_cell(0, 6, text)

# Render any remaining table data
if table_data:
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    num_cols = len(table_data[0]) if table_data else 1
    col_width = 180 / num_cols
    
    for i, row in enumerate(table_data):
        if i == 0:
            pdf.set_font('Helvetica', 'B', 8)
            pdf.set_fill_color(240, 240, 240)
            for cell in row:
                pdf.cell(col_width, 7, cell[:35], border=1, fill=True)
            pdf.ln()
            pdf.set_font('Helvetica', '', 8)
        else:
            for cell in row:
                pdf.cell(col_width, 7, cell[:35], border=1)
            pdf.ln()

# Save PDF
pdf.output(r'C:\Users\HP\Downloads\new process\stat.pdf')

print('PDF created successfully: stat.pdf')
