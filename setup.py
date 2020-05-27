from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_desc='\n'.join(f.readlines())
desc="Read yaml, use Pygal, return chart"

setup(name='yamgal',
    version='0.3a',
    author='Joshua Patterson',
    author_email='joshua.d.patterson@gmail.com',
    description=desc,
    long_description=long_desc,
    python_requires='>=3.6',
    packages=find_packages(),
)

