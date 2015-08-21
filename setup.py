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
    description='Simple (rich) content blocks for use on front end templates. With admin tool.',
    long_description=README,
    author='Django Radonich-Camp',
    author_email='django@emergeinteractive.com',
    url = 'https://github.com/django-emerge/django-richcontentblocks',
    install_requires=[
        'django-ckeditor>=4.5.1'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)