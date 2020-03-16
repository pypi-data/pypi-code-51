import setuptools

with open("README.md") as f:
    long_description = f.read()

with open("version.txt", "r", encoding="utf8") as f:
    v_num = f.read().strip()

setuptools.setup(
    name="emeki",
    version=v_num,
    description="Test",
    packages=setuptools.find_packages(exclude=["docs", "tests"]),
    url="https://github.com/chbauman/emeki",
    author="Christian Baumann",
    author_email="chris.python.notifyer@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["emeki=emeki.util:emeki_main"],},
)
