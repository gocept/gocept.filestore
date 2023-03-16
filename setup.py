from setuptools import find_packages
from setuptools import setup
import os.path


def read(*path):
    with open(os.path.join(*path)) as f:
        return f.read()


setup(
    name='gocept.filestore',
    version='0.5',
    author='gocept gmbh & co. kg',
    author_email='mail@gocept.com',
    url='https://github.com/gocept/gocept.filestore',
    description="Provides maildir like access to files",
    long_description='.. contents::\n\n'
        + read(os.path.dirname(__file__), 'src', 'gocept', 'filestore',
               'README.txt')
        + '\n\n'
        + read('CHANGES.txt'),
    license="ZPL 2.1",
    classifiers=[
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
            ],
    keywords='filesystem consistency',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['gocept'],
    install_requires=[
        'setuptools',
        'zope.deferredimport',
        'zope.interface',
            ],
    extras_require={
        'test': [
            'zope.testing',
            'zope.testrunner'],
            },
)
