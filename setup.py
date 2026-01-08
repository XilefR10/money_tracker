"""Setup configuration for Money Tracker package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="money-tracker",
    version="1.0.0",
    author="XilefR10",
    author_email="xilefr10@gmail.com",
    description="A modern GUI application for personal finance management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XilefR10/money_tracker",
    project_urls={
        "Bug Tracker": "https://github.com/XilefR10/money_tracker/issues",
        "Documentation": "https://github.com/XilefR10/money_tracker/blob/main/README.md",
        "Source Code": "https://github.com/XilefR10/money_tracker",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Financial",
    ],
    python_requires=">=3.8",
    install_requires=[
        "matplotlib>=3.8.0",
        "numpy>=1.24.0",
    ],
    entry_points={
        "console_scripts": [
            "money-tracker=src.main:run",
        ],
    },
)
