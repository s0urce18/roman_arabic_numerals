from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='roman_arabic_numerals',
      version='0.7.0',
      description='Roman numerals converting',
      packages=['roman_arabic_numerals'],
      author="s0urce",
      author_email='boyarkin.gleb@gmail.com',
      zip_safe=False,
      long_description=long_description)