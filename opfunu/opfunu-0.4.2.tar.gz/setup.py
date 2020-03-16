from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="opfunu",
    version="0.4.2",
    author="Thieu Nguyen",
    author_email="nguyenthieu2102@gmail.com",
    description="A python (Numpy) package for Un-constrained Optimization Functions",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/thieunguyen5991/opfunu",
    download_url="https://github.com/thieunguyen5991/opfunu/archive/v.0.4.2.zip",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: System :: Benchmark",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Science/Research"
    ],
    install_requires=["numpy"],
    python_requires='>=3.6',
)