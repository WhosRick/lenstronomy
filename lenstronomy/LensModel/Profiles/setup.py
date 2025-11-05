from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
import sys

openmp_flag = ["-fopenmp"]
if sys.platform.startswith("darwin"):
    openmp_flag = ["-fopenmp"]  # 需要本机有 libomp

exts = [
    Extension(
        name="bpl_fast",
        sources=["bpl_fast.pyx"],
        include_dirs=[np.get_include()],
        extra_compile_args=["-O3", "-ffast-math", "-march=native"] + openmp_flag,
        extra_link_args=openmp_flag,
    )
]

setup(
    name="bpl-fast",
    version="0.6.0",
    ext_modules=cythonize(
        exts,
        language_level="3",
        annotate=False,
        compiler_directives=dict(
            boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, infer_types=True
        ),
    ),
)

