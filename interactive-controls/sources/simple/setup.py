#!/usr/bin/env python
"""chaostoolkit Simple User Interaction builder and installer"""

import sys
import io

import setuptools

sys.path.insert(0, ".")
from chaossimpleinteract import __version__
sys.path.remove(".")

name = 'chaostoolkit-chaossimpleinteract'
desc = 'Chaos Toolkit Simple Interaction Extension'

with io.open('README.md', encoding='utf-8') as strm:
    long_desc = strm.read()

classifiers = [
    'Intended Audience :: Developers',
    'License :: Freely Distributable',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation',
    'Programming Language :: Python :: Implementation :: CPython'
]
author = 'ChaosIQ Team'
author_email = 'contact@chaosiq.io'
url = 'http://chaosiq.io'
license = 'Apache License Version 2.0'
packages = [
    'chaossimpleinteract'
]

needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []

test_require = []
with io.open('requirements-dev.txt') as f:
    test_require = [l.strip() for l in f if not l.startswith('#')]

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]

extra_requires = {}

setup_params = dict(
    name=name,
    version=__version__,
    description=desc,
    long_description=long_desc,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=packages,
    include_package_data=True,
    install_requires=install_require,
    tests_require=test_require,
    setup_requires=pytest_runner,
    extras_require=extra_requires,
    python_requires='>=3.5.0'
)


def main():
    """Package installation entry point."""
    setuptools.setup(**setup_params)


if __name__ == '__main__':
    main()