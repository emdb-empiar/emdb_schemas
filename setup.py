from pathlib import Path

from setuptools import setup


ROOT = Path(__file__).parent

setup(
    name='emdb_schemas',
    version='3.0.11.13',
    packages=['emdb_schemas'],
    package_dir={'emdb_schemas': 'emdb_schemas/current'},
    package_data={'emdb_schemas': ['emdb.xsd', 'emdb_relaxed.xsd']},
    url='https://github.com/emdb-empiar/emdb_schemas',
    license='Apache-2.0',
    license_files=['LICENSE'],
    author='sanja',
    author_email='sanja@ebi.ac.uk',
    description='EMDB schema files',
    long_description=(ROOT / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'lxml>=6.1.1,<7.0.0',
        'six>=1.17.0,<2.0.0',
    ],
    zip_safe=False,
    include_package_data=True
)
