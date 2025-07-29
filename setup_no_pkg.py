from setuptools import setup
from Cython.Build import cythonize

ext_modules = cythonize(
    [
        # "src/package_huxo/alg.py",
        # "src/package_huxo/alg2.py",
        # "src/package_huxo/alg3.py",
        # "src/package_sxzq/utl.py",
        "src/package_huxo/*",
        "src/package_sxzq/*",
    ],
    compiler_directives={
        "language_level": "3",
        "annotation_typing": False,
    },
)

setup(
    name="MyCompiledModule",
    version="0.1.0",
    ext_modules=ext_modules,
    author="huxiaoou",
)
