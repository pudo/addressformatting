import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md") as f:
    long_description = f.read()


setup(
    name="addressformatting",
    version="1.0.2",
    description="Formatting utility for international postal addresses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dunkelstern/international_address_formatter",
    author="Johannes Schriewer",
    author_email="hallo@dunkelstern.de",
    license="BSD",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    keywords="address formatting, international",
    packages=["addressformatting"],
    scripts=[],
    install_requires=[
        "PyYAML >= 5.0",
        "pystache >= 0.5",
    ],
    extras_require={
        "dev": [
            "pytest",
            "bump2version",
            "wheel>=0.29.0",
            "twine",
        ],
    },
)
