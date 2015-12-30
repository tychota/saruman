#!/usr/bin/env python3
from setuptools import setup, find_packages

version = __import__('saruman').__version__

setup(
        name='saruman',
        version=version,
        packages=find_packages(),
        url='',
        license='MIT',
        author='tychota',
        author_email='tycho.tatitscheff+saruman@gadz.org',
        description='A firewall that leverage workqueue ! Build by iresam for iresam !',
        install_requires=['celery', 'python-iptables', 'plumbum', 'click', 'colorlog'],
        entry_points='''
            [console_scripts]
            saruman=saruman.__main__:cli
        ''',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Intended Audience :: System Administrators',
            'Natural Language :: English',
            'Natural Language :: French',
            'Operating System :: POSIX :: Linux',
            'Topic :: Internet :: Name Service (DNS)',
            'Topic :: Internet :: Proxy Servers',
            'Topic :: System :: Networking',
            'Topic :: System :: Networking :: Firewalls',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ],
)
