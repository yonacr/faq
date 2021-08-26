import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='faq',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description=(
        "A small Django FAQ app for demonstration purposes."
    ),
    url='https://github.com/yonacr/faq',
    author='Yona Rasolonjatovo',
    author_email='yonaclementie@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved ::  MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
