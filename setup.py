# MC-Formatting Python Module - convert MC (Section Symbol) Formatting Codes to ANSI Escape Codes
# Copyright (C) 2020 SirNapkin1334
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# The author can be contacted via:
#   Email: sirnapkin@protonmail.com
#   Twitter: @SirNapkin1334
#   Discord: @SirNapkin1334#7960
#   Reddit: u/SirNapkin1334
#   IRC: SirNapkin1334; Registered on Freenode, EFNet, possibly others

# Adapted from https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py

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
