from fpdf import FPDF
import re

# Read the markdown file
with open(r'C:\Users\ahmed\Desktop\vr\Ibri-and-Suhar-port\outputs\METHODOLOGY_RESULTS_DISCUSSION.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Replace special characters that may cause issues
md_content = md_content.replace('χ²', '(Chi-Square)')
md_content = md_content.replace('χ', 'Chi')
md_content = md_content.replace('μ', 'mu')
md_content = md_content.replace('α', 'alpha')
md_content = md_content.replace('β', 'beta')
md_content = md_content.replace('γ', 'gamma')
md_content = md_content.replace('ε', 'epsilon')
md_content = md_content.replace('η', 'eta')
md_content = md_content.replace('∞', 'inf')
md_content = md_content.replace('√', 'sqrt')
md_content = md_content.replace('∑', 'sum')
md_content = md_content.replace('≤', '<=')
md_content = md_content.replace('≥', '>=')
md_content = md_content.replace('±', '+/-')
md_content = md_content.replace('→', '->')
md_content = md_content.replace('─', '-')
md_content = md_content.replace('│', '|')
md_content = md_content.replace('┌', '+')
md_content = md_content.replace('┐', '+')
md_content = md_content.replace('└', '+')
md_content = md_content.replace('┘', '+')
md_content = md_content.replace('├', '+')
md_content = md_content.replace('┤', '+')
md_content = md_content.replace('┬', '+')
md_content = md_content.replace('┴', '+')
md_content = md_content.replace('┼', '+')
md_content = md_content.replace('▼', 'v')
md_content = md_content.replace('✅', '[OK]')
md_content = md_content.replace('❌', '[X]')
md_content = md_content.replace('⚠️', '[!]')
md_content = md_content.replace('⛔', '[STOP]')
md_content = md_content.replace('📊', '[TABLE]')
# Subscript and superscript numbers
md_content = md_content.replace('₀', '0')
md_content = md_content.replace('₁', '1')
md_content = md_content.replace('₂', '2')
md_content = md_content.replace('₃', '3')
md_content = md_content.replace('₄', '4')
md_content = md_content.replace('₅', '5')
md_content = md_content.replace('₆', '6')
md_content = md_content.replace('₇', '7')
md_content = md_content.replace('₈', '8')
md_content = md_content.replace('₉', '9')
md_content = md_content.replace('⁰', '0')
md_content = md_content.replace('¹', '1')
md_content = md_content.replace('²', '2')
md_content = md_content.replace('³', '3')
md_content = md_content.replace('⁴', '4')
md_content = md_content.replace('⁵', '5')
md_content = md_content.replace('⁶', '6')
md_content = md_content.replace('⁷', '7')
md_content = md_content.replace('⁸', '8')
md_content = md_content.replace('⁹', '9')
# Other special chars
md_content = md_content.replace('λ', 'lambda')
md_content = md_content.replace('σ', 'sigma')
md_content = md_content.replace('Σ', 'Sigma')
md_content = md_content.replace('π', 'pi')
md_content = md_content.replace('θ', 'theta')
md_content = md_content.replace('φ', 'phi')
md_content = md_content.replace('ω', 'omega')
md_content = md_content.replace('Ω', 'Omega')
md_content = md_content.replace('∈', 'in')
md_content = md_content.replace('∉', 'not in')
md_content = md_content.replace('∀', 'for all')
md_content = md_content.replace('∃', 'exists')
md_content = md_content.replace('∫', 'integral')
md_content = md_content.replace('∂', 'd')
md_content = md_content.replace('∇', 'nabla')
md_content = md_content.replace('•', '-')
md_content = md_content.replace('·', '.')
md_content = md_content.replace('×', 'x')
md_content = md_content.replace('÷', '/')
md_content = md_content.replace('≠', '!=')
md_content = md_content.replace('≈', '~')
md_content = md_content.replace('∝', 'proportional to')
md_content = md_content.replace('∆', 'Delta')
md_content = md_content.replace('′', "'")
md_content = md_content.replace('″', '"')
md_content = md_content.replace(''', "'")
md_content = md_content.replace(''', "'")
md_content = md_content.replace('"', '"')
md_content = md_content.replace('"', '"')
md_content = md_content.replace('—', '-')
md_content = md_content.replace('–', '-')
md_content = md_content.replace('…', '...')
# Remove any remaining non-latin1 characters
md_content = md_content.encode('latin-1', errors='replace').decode('latin-1')
# Remove LaTeX/KaTeX equations
md_content = re.sub(r'\$\$.*?\$\$', '[EQUATION]', md_content, flags=re.DOTALL)
md_content = re.sub(r'\$[^$]+\$', '[eq]', md_content)
# Skip image references
md_content = re.sub(r'!\[.*?\]\(.*?\)', '[IMAGE]', md_content)

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
pdf.output(r'C:\Users\ahmed\Desktop\vr\Ibri-and-Suhar-port\outputs\METHODOLOGY_RESULTS_DISCUSSION.pdf')

print('PDF created successfully: METHODOLOGY_RESULTS_DISCUSSION.pdf')
