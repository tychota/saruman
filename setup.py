#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
        name='Firewall',
        version='2',
        packages=find_packages(),
        url='',
        license='MIT',
        author='salas',
        author_email='',
        description='',
        install_requires=['celery', 'python-iptables', 'plumbum', 'click', 'colorlog'],
        entry_points='''
            [console_scripts]
            firewall-cli=firewall:cli
        ''',
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ],
)
