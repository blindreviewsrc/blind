from distutils.core import setup

setup(
    name='ColabPlugin',
    version='blind',
    author='blind',
    author_email='blind',
    py_modules=['plugin', 'src.v1.v1', 'src.c.c', 'src.cpp.cpp', 'src.verilog.verilog', 'src.java.java', 'src.gem5.gem5', 'src.valgrind.valgrind', 'src.common.helper'],
    url='https://github.com/blindreviewsrc/blind/',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++, GCC code, Verilog, Gem5',
    # long_description=open('README.md').read(),
)
