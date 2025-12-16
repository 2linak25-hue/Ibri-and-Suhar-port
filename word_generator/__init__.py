# Word Document Generator Package
# Generates professional Word documents for EMF ML Analysis

from .document_builder import DocumentBuilder
from .styles import apply_styles
from .tables import create_table, create_results_table
from .content import get_methodology_content, get_results_content, get_discussion_content

__all__ = [
    'DocumentBuilder',
    'apply_styles',
    'create_table',
    'create_results_table',
    'get_methodology_content',
    'get_results_content',
    'get_discussion_content'
]
