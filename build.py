from py_compile import compile
from os import mkdir
from os.path import join, exists

import utils

builddir = './build'
mode = 0o777
if not exists(builddir):
    mkdir(builddir, mode)
srcs = list(filter(lambda file: file.endswith('.py'), utils.files('.')))
bytecodes = [join(builddir, src.replace('.py', '.pyc')) for src in srcs]
for i in range(len(srcs)):
    compile(srcs[i], cfile=bytecodes[i])
print(srcs)
