from setuptools import setup


setup(
    name='laserEmb',
    version='0.0.1',
    author='cympfh',
    author_email='cympfh@gmail.com',
    install_requires=[
        'mecab-python3==0.7'
    ],
    packages=['laserEmb'],
    package_data={
        '': ['*.py', '*.fcodes', '*.fvocab', '*.pt']
    }
)
