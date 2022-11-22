import setuptools  

setuptools.setup(
    name='PyroPath',
    version='0.0.1',
    author='Muhammed',
    license='MIT License',
    description='Just a simple Python package. Created By @Pr0fess0r_99',                           
    package_data={
      "PyroPath",
    },
    url="https://github.com/PR0FESS0R-99/PyroPath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='~=3.7',
    py_modules=["PyroPath"],
)
