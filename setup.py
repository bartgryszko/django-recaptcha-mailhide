#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages

with open('README.rst') as fd:
    README = fd.read()

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Bartosz Gryszko",
    author_email="b@gryszko.com",
    name="django-recaptcha-mailhide",
    packages=find_packages(exclude=['docs']),
    version='1.2',
    description="ReCAPTCHA Mailhide is an app for hiding mails from spammers. To use with Django templates.",
    long_description=README,
    url='https://github.com/bgryszko/django-recaptcha-mailhide',
    license='MIT',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    keywords= ['Django', 'ReCaptcha'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'future>=0.16.0',
        'Django>=1.10.0,<1.11',
        'pycrypto>=2.6.1',
    ],
)
