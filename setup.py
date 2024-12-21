from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='rotate_ocr',
    version='0.1.0',
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    author='Yutaka Nishizaki',
)
