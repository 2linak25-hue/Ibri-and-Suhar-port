"""
Generate EMF ML Analysis Word Document
Main script to generate the Word document from scratch
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from word_generator.document_builder import DocumentBuilder


def main():
    """Main function to generate the Word document"""
    
    # Define paths
    base_dir = r'C:\Users\ahmed\Desktop\vr\Ibri-and-Suhar-port'
    output_dir = os.path.join(base_dir, 'outputs')
    plots_dir = os.path.join(output_dir, 'plots')
    output_file = os.path.join(output_dir, 'EMF_ML_ANALYSIS_REPORT.docx')
    
    print("=" * 60)
    print("EMF ML Analysis - Word Document Generator")
    print("=" * 60)
    print(f"\nOutput Directory: {output_dir}")
    print(f"Plots Directory: {plots_dir}")
    print(f"Output File: {output_file}")
    print()
    
    # Check if plots directory exists
    if os.path.exists(plots_dir):
        plot_files = [f for f in os.listdir(plots_dir) if f.endswith('.png')]
        print(f"Found {len(plot_files)} plot images")
    else:
        print("Warning: Plots directory not found. Images will not be included.")
    
    print("\nGenerating document...")
    print("-" * 40)
    
    # Create document builder
    builder = DocumentBuilder(output_file, plots_dir)
    
    # Build the document
    try:
        output_path = builder.build()
        print("-" * 40)
        print(f"\n✓ Document generated successfully!")
        print(f"  Location: {output_path}")
        
        # Get file size
        file_size = os.path.getsize(output_path) / 1024  # KB
        print(f"  File size: {file_size:.1f} KB")
        
    except Exception as e:
        print(f"\n✗ Error generating document: {e}")
        raise
    
    print("\n" + "=" * 60)
    return output_path


if __name__ == '__main__':
    main()
