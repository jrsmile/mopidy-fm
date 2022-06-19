import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-FM',
    version=get_version('mopidy_fm/__init__.py'),
    url='https://github.com/jrsmile/mopidy-fm',
    license='Apache License, Version 2.0',
    author='JRSmile',
    author_email='mopidy-fm@behead.de',
    description='Mopidy PiFM bridge with RDS',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 3.00',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'fm = mopidy_fm:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
