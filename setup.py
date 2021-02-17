import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fintopy", # Replace with your own username
    version="0.0.1",
    author="Marco Bonifacio",
    author_email="bonifacio.marco@gmail.com",
    description="Pandas extensions for financial markets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mbonix/fintopy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)