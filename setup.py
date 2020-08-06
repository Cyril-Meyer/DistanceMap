import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distance-map",
    version="1.0.1",
    author="Cyril Meyer",
    author_email="contact@cyrilmeyer.eu",
    description="Distance Map library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cyril-Meyer/DistanceMap",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "numba"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
