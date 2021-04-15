from setuptools import setup
setup(
    name = 'asciy',
    version = '0.1.0',
    packages = ['asciy'],
    entry_points = {
        'console_scripts': [
            'asciy = asciy.__main__:main'
        ]
    })