import os
import shutil
import sys


SRC_DIR = "/Debug"
DST_DIR = "/Makefiles"

# List of allowing endings of files
AllowEndOfFilesList = [
    ".mk",
    "objects.list",
    "makefile"
]


# Check end of file
def CheckFile(f):
    Status = True
    for item in AllowEndOfFilesList:
        if f[-len(item):] == str(item):
            Status = False
    return Status


# Get current path
path = os.path.realpath(os.path.dirname(sys.argv[0]))


# Ignore any files but files with extension from list must be pass  
ignore_func = lambda d, files: [
    f for f in files 
        if os.path.isfile(os.path.join(d, f)) 
        and CheckFile(f)
    ]

if (os.path.isdir(path + DST_DIR)):
    shutil.rmtree(path + DST_DIR) 

shutil.copytree(path + SRC_DIR, path + DST_DIR, ignore=ignore_func)

