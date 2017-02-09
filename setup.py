from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize

extensions = [
    Extension(
        'hello',
        ['hello.pyx'],
    )
]

extensions = cythonize(extensions)

setup(
    name='hello',
    packages=['_hello'],  # required
    include_package_data=True,  # required
    version='1.0.0',
    license='MIT',
    ext_modules=extensions,
)
