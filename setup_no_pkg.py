from setuptools import setup
from Cython.Build import cythonize

ext_modules = cythonize(
    [
        "src/package_huxo/alg.py",
        "src/package_huxo/alg2.py",
        "src/package_sxzq/utl.py",
    ]
)

setup(
    name="MyCompiledModule",
    version="0.1.0",
    ext_modules=ext_modules,
    author="huxiaoou",
)
