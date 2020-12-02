# CREATE A NESTED DICTIONARY FROM OS.WALK
# Link : https://code.activestate.com/recipes/577879-create-a-nested-dictionary-from-oswalk/
# Example:
"""
{
    "root": {
        "folder2": {
            "item2": None, 
            "item1": None
        }, 
        "folder1": {
            "subfolder1": {
                "item2": None, 
                "item1": None
            }, 
            "subfolder2": {
                "item3": None
            }
        }
    }
}
"""

import os

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir
