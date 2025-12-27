"""
DataLib - A utility library for data processing and analysis
"""

__version__ = "1.0.0"
__author__ = "Interview Team"

from .processor import DataProcessor
from .validator import DataValidator
from .formatter import DataFormatter

__all__ = ["DataProcessor", "DataValidator", "DataFormatter"]