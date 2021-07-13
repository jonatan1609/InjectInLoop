from setuptools import setup, find_packages

__version__ = "1.0.1"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="InjectInLoop",
    version=__version__,
    author="Jonathan",
    author_email="pybots.il@gmail.com",
    description="This module lets you inject a function call between every iteration without doing it manually."
                " Created mainly for fun :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonatan1609/InjectInLoop",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",

    ],
    python_requires=">=3"
)