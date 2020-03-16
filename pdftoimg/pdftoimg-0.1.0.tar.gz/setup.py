import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdftoimg",
    version="0.1.0",
    author="starkblaze01",
    author_email="mp.pathela@gmail.com",
    description="Easily convert PDF to Image from command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/starkblaze01/Pdf-To-Image",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    keywords="pdf-to-image convert",

    entry_points={
        "console_scripts": ['pdftoimg = pdftoimg.pdftoimg:main'],
    },
    python_requires='>=3.6',
    install_requires=[
        'pdf2image>=1.11.0',
    ],
)
