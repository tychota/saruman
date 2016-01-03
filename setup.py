#!/usr/bin/env python3
from setuptools import setup, find_packages
from setuptools.command.install import install as _install


def read(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            return f.read()
    except NameError:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

long_description = u'\n\n'.join([read('README.rst'),
                                 read('CREDITS.rst'),
                                 read('CHANGES.rst')])


class Install(_install):
    def run(self):
        _install.run(self)
        print("Post Install")

setup(
        name='saruman',
        version='0.1.3.dev0',
        packages=find_packages(),
        url='https://github.com/tychota/saruman',
        license='MIT',
        author='tychota',
        author_email='tycho.tatitscheff+saruman@gadz.org',
        description='A firewall that leverage AMQP workqueue ! Build by iresam for iresam !',
        long_description=long_description,
        install_requires=[
            'celery',
            'plumbum',
            'click',
            'colorlog',
            'yaml'
        ],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        test_suite="tests",
        entry_points='''
            [console_scripts]
            saruman=saruman.__main__:cli
        ''',
        cmdclass={'install': Install},
        zip_safe=False,
        keywords=['firewall', 'amqp', 'nftables', 'dhcp, reverse-proxy'],
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
