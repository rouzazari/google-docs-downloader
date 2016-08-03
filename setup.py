from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

import googledownload

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
            return sep.join(buf)
        
setup(
    name='googledownload',
    version='0.1.0',
    url='http://github.com/rouzazari/googledownload/',
    license='MIT License',
    author='Rouz Azari',
    install_requires=['beautifulsoup4==4.5.1',
                    'requests==2.10.0',
                    ],
    author_email='rouz@rouzazari.com',
    description='Google Docs public link downloader',
    packages=['googledownload'],
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        ]
)
