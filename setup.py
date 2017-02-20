from setuptools import setup

setup(
    name='greenhousemonitor'
    packages=['greenhousemonitor']
    include_package_data=True,
    install_requires=[
        'flask',
        'serial',
        'pygal',
    ],
)
