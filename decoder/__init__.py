"""
HID (Hierarchical Interchange Data) Format Decoder
Open-source decoder for the HID music format

Patent Notice: The encoding algorithm is patent-protected (CN202410xxxxx).
This decoder is released under MIT License for academic and commercial use.
"""

from .core import HIDDecoder
from .events import HIDEvent, EventType
from .utils import read_hid_file, validate_hid

__version__ = "1.0.0"
__author__ = "Freening Lu"
__license__ = "MIT"

__all__ = [
    "HIDDecoder",
    "HIDEvent",
    "EventType",
    "read_hid_file",
    "validate_hid"
]