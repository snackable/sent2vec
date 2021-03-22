import sys
from setuptools import setup, dist, Extension
from distutils.command.build import build as build_orig

class build(build_orig):

    def finalize_options(self):
        super().finalize_options()
        import numpy
        for extension in self.distribution.ext_modules:
            extension.include_dirs.append(numpy.get_include())
        from Cython.Build import cythonize
        self.distribution.ext_modules = cythonize(self.distribution.ext_modules,
                                                  language_level=3)




#dist.Distribution().fetch_build_eggs(['cython>=0.29.13', 'numpy>=1.19.5'])


sourcefiles  = ['src/sent2vec.pyx',
                'src/fasttext.cc',
                'src/args.cc',
                'src/dictionary.cc',
                'src/matrix.cc',
                'src/shmem_matrix.cc',
                'src/qmatrix.cc',
                'src/model.cc',
                'src/real.cc',
                'src/utils.cc',
                'src/vector.cc',
                'src/real.cc',
                'src/productquantizer.cc']
compile_opts = ['-std=c++0x', '-Wno-cpp', '-pthread', '-Wno-sign-compare']
libraries = ['rt']
if sys.platform == 'darwin':
    libraries = []
ext=[Extension('*',
            sourcefiles,
            extra_compile_args=compile_opts,
            language='c++',
            libraries=libraries)]

setup(
  name='sent2vec',
  setup_requires=['cython>=0.29.13', 'numpy>=1.19.5'],
  install_requires=['numpy>=1.19.5'],
  cmdclass={"build": build},
  ext_modules=ext
)
