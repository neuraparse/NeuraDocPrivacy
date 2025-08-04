#!/usr/bin/env python3
"""
Setup script for NeuraDocPrivacy
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="neura-doc-privacy",
    version="1.2.0",
    author="NeuraDocPrivacy Team",
    author_email="contact@neura-doc-privacy.com",
    description="A sophisticated PDF document privacy masking tool using NLP",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/neuraparse/NeuraDocPrivacy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: Text Processing :: Filters",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "gui": [
            "PyQt5>=5.15.0",
            "PyQt5-sip>=12.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "neura-doc-privacy=main:main",
            "pdf-masker=pdf_masker:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.spec"],
    },
    keywords="pdf, privacy, masking, nlp, spacy, document-processing, security",
    project_urls={
        "Bug Reports": "https://github.com/neuraparse/NeuraDocPrivacy/issues",
        "Source": "https://github.com/neuraparse/NeuraDocPrivacy",
        "Documentation": "https://github.com/neuraparse/NeuraDocPrivacy#readme",
    },
) 