import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mc-formatting-SirNapkin1334",
    version="1.0",
    author="SirNapkin1334",
    author_email="sirnapkin@protonmail.com",
    description="A package for converting MC (Section-Symbol) Codes to ANSI Escape Codes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SirNapkin1334/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)