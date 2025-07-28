from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "package_huxo.alg",  # Name of the so file
        sources=["src/package_huxo/alg.py"],
    ),
    Extension(
        "package_huxo.alg2",
        sources=["src/package_huxo/alg2.py"],
    ),
    Extension(
        "package_sxzq.utl",
        sources=["src/package_sxzq/utl.py"],
    ),
]
ext_modules = cythonize(extensions, compiler_directives={"language_level": "3"})

setup(
    name="MyCompiledModule",
    version="0.1.0",
    ext_modules=ext_modules,
    author="huxiaoou",
)
