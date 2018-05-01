from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='assess',
    version='1.0',
    url='https://github.com/nasa-jpl/ASSESS',
    license='Apache License 2.0',
    maintainer='JPL',
    maintainer_email='assess@jpl.nasa.gov',
    description='Automatic Semantic Search Engine for Suitable Standards',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
