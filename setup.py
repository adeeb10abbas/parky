import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='parky',  
     version='0.2',
     scripts=['parky/main.py'] ,
     author="Adeeb Abbas",
     author_email="adeeb.abbas@drexel.edu",
   long_description_content_type="text/markdown",
     url="https://github.com/adeeb10abbas/parky",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent // Linux|MacOS preferred",
     ],
 )