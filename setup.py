"""
HID Format Setup Configuration
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hid-music",
    version="1.0.0",
    author="Freening Lu",
    author_email="nl2608@stern.nyu.edu",
    description="HID: Hyper Instrument Data - An AI-Native Music Representation Format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FreeNingLu/HID",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "mido>=1.2.10",
        "tabulate>=0.8.9",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "hid-decode=decoder.cli:main",
            "hid-benchmark=benchmarks.run_all:main",
        ],
    },
    project_urls={
        "Paper": "https://arxiv.org/abs/2025.xxxxx",
        "Documentation": "https://hid-format.readthedocs.io",
        "Source": "https://github.com/FreeNingLu/HID",
        "Issues": "https://github.com/FreeNingLu/HID/issues",
    },
)