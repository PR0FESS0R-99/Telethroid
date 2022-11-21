import re
import setuptools

with open('requirements.txt') as fp:
    requirements = [line.strip() for line in fp]

with open('PyroPath/__init__.py') as fp:
    version = re.search('__version__ = "(.+?)"', fp.read())[1]

setuptools.setup(
    name="PyroPath",
    version=version,
    author="Muhammed RK",
    author_email="muhammedmotech@gmail.com",
    license="MLT",
    description="Symbol Programming Language",
    long_description_content_type="text/markdown",
    url="https://github.com/PR0FESS0R-99/PyroPath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='~=3.7',
    py_modules=["PyroPath"],
    install_requires=requirements,
)
