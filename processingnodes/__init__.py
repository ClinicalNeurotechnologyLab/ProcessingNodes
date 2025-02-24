"""
This is a package to test python packaging
"""

__version__ = "0.1.0"
__author__ = "Niels Peekhaus"
__credits__ = ""

from .DataProcessor import DataProcessor
from .ProcessingNode import ProcessingNode
from .ProcessingPipeline import ProcessingPipeline

__all__ = ['DataProcessor', 'ProcessingNode', 'ProcessingPipeline']

