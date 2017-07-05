from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''


install_requires=[
    "configparser",
    'requests',
    'six'
]

testpkgs = [
    "nose==1.3.7",
    "coverage",
    "mock"
]
setup(description='This is the official Python SDK for ContactHub REST API. This SDK easily allows to access your data '
                  'on ContactHub, making the authentication immediate and simplifying read/write operations.',
      author='Axant',
      url='https://github.com/axant/contacthub-sdk-python',
      version='0.1',
      classifiers=['Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.5-dev',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.6-dev',
                   'Programming Language :: Python :: 3.7-dev',
                   'Programming Language :: Python :: nightly',
                   'Topic :: Internet :: WWW/HTTP ',
                   'Topic :: API :: SDK ',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='web skd api',
      author_email='tech@axant.it',
      install_requires=install_requires,
      packages=find_packages(exclude=['tests', 'tests.*']),
      extras_require={
          'testing': testpkgs,
          'documentation': ['Sphinx==1.4.1', 'sphinx_rtd_theme']
      },
      scripts=[],
      name='contacthub-sdk-python',
      long_description=README,
      include_package_data=False,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=testpkgs,
      )
