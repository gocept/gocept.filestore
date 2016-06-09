import os.path

from setuptools import setup, find_packages


setup(
    name='gocept.filestore',
    version='0.4dev',
    author='gocept gmbh & co. kg',
    author_email='mail@gocept.com',
    url='https://bitbucket.org/gocept/gocept.filestore',
    description="Provides maildir like access to files",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'src', 'gocept', 'filestore',
                                       'README.txt')).read(),
    license="ZPL 2.1",

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
        'test': ['zope.testing'],
    },
)
