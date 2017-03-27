from setuptools import setup, find_packages

from codecs import open
from os import path

BASE_DIR = path.abspath(path.dirname(__file__))
README_FILE = 'readme.rst'

with open(path.join(BASE_DIR, README_FILE), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bandeco',
    version='0.1',
    description='Fetches the menu from Unicamp\'s restaurantes',
    url='https://github.com/drakenation/bandeco',
    author='drakenation',
    author_email='draken.emb@gmail.com',
    license='MIT',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
    keywords='restaurant menu scrapper',
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'bandeco=bandeco:main',
            ],
    },
)


