from setuptools import find_packages, setup

setup(
    name='emdb_schemas',
    version='3.0.8.0',
    packages=find_packages(),
    package_dir={'emdb_schemas': 'emdb_schemas/current'},
    package_data={'emdb_schemas': ['emdb.xsd', 'emdb_relaxed.xsd']},
    url='',
    license='',
    author='sanja',
    author_email='sanja@ebi.ac.uk',
    description='EMDB schema files',
    install_requires=[
        'lxml>=6.1.1,<7.0.0',
        'six>=1.17.0,<2.0.0',
    ],
    zip_safe=False,
    include_package_data=True
)
