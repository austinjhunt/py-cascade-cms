import pathlib
from setuptools import setup
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py-cascade-cms-api",
    version="1.1.3",
    description="Simplify interaction with Hannon Hill's Cascade CMS 8 REST API",
    long_description=README,
    keywords='cascade, cms, rest, api, hannon hill, driver',
    long_description_content_type="text/markdown",
    url="https://github.com/austinjhunt/CascadeCMS",
    project_urls={
        'Documentation': 'https://github.com/austinjhunt/CascadeCMS',
        'Bug Reports': 'https://github.com/austinjhunt/CascadeCMS/issues',
        'Source Code': 'https://github.com/austinjhunt/CascadeCMS',
        'Cascade CMS REST API Docs': 'https://www.hannonhill.com/cascadecms/latest/developing-in-cascade/rest-api/index.html'
    },
    author="Austin Hunt",
    author_email="austin353@gmail.com",
    license="MIT",
    classifiers=[
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    include_package_data=True,
    install_requires=["requests", "uplink"],
)
