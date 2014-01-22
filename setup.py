import sys
import os
import subprocess

from setuptools import setup

PUBLISH_CMD = "python setup.py register sdist upload"
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist upload -r test'
TEST_CMD = 'nosetests'

if 'publish' in sys.argv:
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit()

if 'run_tests' in sys.argv:
    try:
        __import__('nose')
    except ImportError:
        print('nose required. Run `pip install nose`.')
        sys.exit(1)
    status = subprocess.call(TEST_CMD, shell=True)
    sys.exit(status)

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='wgetdb',
    version="0.1.3",
    description='Download and store webpages in a sqlite database',
    long_description=read("README.md"),
    author='Akira Kozakai',
    author_email='akiraak@gmail.com',
    url='https://github.com/akiraak/wgetdb',
    install_requires=['docopt'],
    license=read("LICENSE"),
    zip_safe=False,
    keywords='wgetdb',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    py_modules=["wgetdb"],
    entry_points={
        'console_scripts': [
            "wgetdb = wgetdb:main"
        ]
    },
    tests_require=['nose'],
)
