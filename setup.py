from __future__ import print_function
from setuptools import setup, find_packages
from Cython.Build import cythonize
from distutils.core import Extension

module1 = Extension('mpo_lab.MPOtorch',['mpo_lab/MPOtorch.c'])
module2 = Extension('mpo_lab.Matrix2MPO',['mpo_lab/Matrix2MPO.c'])

setup(
    name="mpo_lab",
    version="0.1.0",
    author="Peiyu Liu, Zefeng Gao",
    author_email="liupeiyustu@163.com",
    description="Tools for model compression based on methods from paper, 'Enabling Lightweight Fine-tuning for Pre-trained Language Model Compression based on Matrix Product Operators'",
    license="MIT",
    url="https://arxiv.org/abs/2106.02205", # paper url
    packages=find_packages(),
    ext_modules=[module1,module2],
    include_package_data=True,
    install_requires=[
        'numpy',
        'torch',
        'Cython'
    ],
    zip_safe=True
)