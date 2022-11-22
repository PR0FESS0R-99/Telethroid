import setuptools  

setuptools.setup(
      name='PyroPath',
      version='0.0.1',
      author='Muhammed',
      license='MIT License',
      description='Just a simple Python package. Created By @Pr0fess0r_99',                           
      package_data={
        "pyrogram": ["py.typed"],
      },
      zip_safe=False,
      packages=['PyroPath'],
)
