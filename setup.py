from setuptools import setup, find_packages

setup(
    name='thanos',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['thanos=thanos.thanos:snap'],
    },
)
