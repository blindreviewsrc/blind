from distutils.core import setup

setup(
    name='ColabPlugin',
    version='blind',
    author='blind',
    author_email='blind',
    py_modules=['nvcc_plugin', 'v2.v2', 'v1.v1', 'c.c', 'cpp.cpp', 'verilog.verilog', 'java.java', 'gem5.gem5', 'valgrind.valgrind', 'common.helper'],
    url='htpps://github.com/canesche/nvcc4jupyter',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++, GCC code',
    # long_description=open('README.md').read(),
)
