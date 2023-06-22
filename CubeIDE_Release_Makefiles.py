import os
import shutil
import sys


SRC_DIR = "/Release"
DST_DIR = "/Makefiles"



path = os.path.realpath(os.path.dirname(sys.argv[0]))


# ignore any files but files with '.mk, .list' extension and makefiles
ignore_func = lambda d, files: [
    f for f in files 
        if os.path.isfile(os.path.join(d, f)) 
        and f[-3:] != '.mk' 
        and f[-12:] != 'objects.list' 
        and f[-8:] != 'makefile'
    ]

if (os.path.isdir(path + DST_DIR)):
    shutil.rmtree(path + DST_DIR) 

shutil.copytree(path + SRC_DIR, path + DST_DIR, ignore=ignore_func)

