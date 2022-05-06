from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="pdfmerge",
    version="1.0.0",
    description="Small Package for merging PDF files.",
    packages=find_packages(),
    entry_points={"console_scripts": ["pdfmerge = pdfmerge.pdfmerge:main"]},
    install_requires=requirements,
    zip_safe=False,
)
