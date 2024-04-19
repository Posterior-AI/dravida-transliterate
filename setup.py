from setuptools import setup, find_packages

from translit import __version__

setup(
    name='translit',
    version=__version__,

    url='https://github.com/Posterior-AI/dravida-transliterate',
    author='PosteriorAI',
    author_email='jas@posterior.xyz',

    py_modules=find_packages(),
)