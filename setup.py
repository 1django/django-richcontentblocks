import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='richcontentblocks',
    version='0.3',
    packages=['richcontentblocks'],
    include_package_data=True,
    license='BSD License', 
    description='Simple (rich) content blocks for use on front end templates.',
    long_description=README,
    author='Emerge Interactive',
    author_email='django@emergeinteractive.com',
    install_requires=[
        'django-ckeditor>=4.5.1'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)