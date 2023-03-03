import os
import shutil
import re
import zipfile

# Change this to the path your web browser defaults downloaded files to
DOWNLOADS_PATH = "/Users/lucas.vasconcelos/Downloads"
DUP_RGXR = re.compile("^.[(\\[0-9\\]\\+).zip]")
# '(<X number of 0-9 digits>).zip)'
VERSION_RGXR = re.compile("\\[\\[0-9\\]\\+).zip]")
NAME_RGXR = re.compile(").zip")


def main():
    fnMap = {}
    # reverse the list so that earlier versions of packages come first
    downloads.reverse()
    # get most recent versions of all Appian package files
    for filename in downloads:
        processDuplicate(filename, DUP_RGXR, VERSION_RGXR, NAME_RGXR, dupVersionsMap)
    

def getUniqueDownloadedFilenames(filenames, fnMap):
    for fnName in filenames:
        fs = zipfile.PyZipFile.
        if fnName not in fnMap:
            fnMap[fnName] = 0
    
def processDuplicate(filename, dupRgxr, versionRgxr, nameRgxr, dupVersionsMap):
    matched = dupRgxr.fullmatch(filename)

    for match in matched:
         rawVersionString = versionRgxr.search(match)
         version = rawVersionString.replace(").zip", "")[len(rawVersionString)]
         versionKey = nameRgxr.sub("", match)
         if versionKey not in dupVersionsMap:
             dupVersionsMap[versionKey] = 0
         else:
             if version < dupVersionsMap[versionKey]:
                 os.remove("./${match}",)
             else:
                dupVersionsMap[versionKey] = version

def 
    

