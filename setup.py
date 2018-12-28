from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="algorithms-toolbox",
    version="0.0.1",
    author="Quan Hua",
    author_email="quanhua92@gmail.com",
    description="A small collection of algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quanhua92/algorithms-toolbox",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
