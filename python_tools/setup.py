from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "fastmodules",
        ["python_tools/fastmodules.pyx"],
        libraries=["m"],
        extra_compile_args=["-ffast-math"],
        include_dirs=[numpy.get_include()],
        define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]
    )
]

setup(
    name="fastmodules",
    ext_modules=cythonize(
        ext_modules,
        compiler_directives={'language_level': '3'},
        annotate=True  # Generates fastmodules.html for debugging
    )
)
