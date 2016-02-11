#!/usr/bin/env python

from setuptools import setup

setup(
    name='wfppresence',
    version='1.0.0',
    install_requires=[],
    author='Patrick Dufour',
    author_email='pjdufour.dev@gmail.com',
    license='BSD License',
    url='https://github.com/wfp-ose/wfp-presence-django',
    keywords='python gis wfp',
    description='WFP Presence Django, Version 1.x',
    long_description=open('README.rst').read(),
    download_url="https://github.com/wfp-ose/wfp-presence-django/zipball/master",
    packages=[
        "wfppresencedjango",
        "wfppresencedjango.tests"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
