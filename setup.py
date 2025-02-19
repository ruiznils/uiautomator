#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requires = [
    "urllib3>=1.7.1"
]
test_requires = [
    'nose>=1.0',
    'mock>=1.0.1',
    'coverage>=3.6'
]

version = '1.0.3'

setup(
    name='uiautomator',
    version=version,
    description='Python Wrapper for Android UiAutomator test tool',
    long_description='Python wrapper for Android uiautomator tool.',
    author='Xiaocong He',
    author_email='xiaocong@gmail.com, hongbin.bao@gmail.com',
    url='https://github.com/xiaocong/uiautomator',
    download_url='https://github.com/xiaocong/uiautomator/tarball/%s' % version,
    keywords=[
        'testing', 'android', 'uiautomator', 'uiautomatorpy'
    ],
    install_requires=requires,
    tests_require=test_requires,
    test_suite="nose.collector",
    packages=['uiautomator'],
    package_data={
        'uiautomator': [
            'uiautomator/libs/bundle.jar',
            'uiautomator/libs/uiautomator-stub.jar',
            'uiautomator/libs/app-uiautomator-test.apk',
            'uiautomator/libs/app-uiautomator.apk',
            'uiautomator/libs/app-uiautomator-test-androidx.apk',
            'uiautomator/libs/app-uiautomator-androidx.apk']
    },
    include_package_data=True,
    license='MIT',
    platforms='any',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    )
)
