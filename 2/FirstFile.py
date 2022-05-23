import glob
import subprocess
import os

"""Maximum possible file size."""
MAX_FILE_SIZE = 14*(2**20)

def firstCompliantFile(fileSystemPath):
    """This function returns the first file allocated on the input path that meets the
        expected requirements:
        1- The file owner is admin
        2- The file is executable
        3- The file has a size lower than 14*2^20

    Parameters:
    fileSystemPath (string): Global/local path for the search.

    Returns:
    string: First found file's name.

   """

    listExeFiles = glob.glob(fileSystemPath + "/*.exe")
    isAdminOwner = False
 
    for file in listExeFiles:
        isAdminOwner = False
        output = subprocess.check_output(["powershell.exe", "Get-Acl " + file + " | Format-List"],
                        universal_newlines=True).splitlines()
        for line in output:
            if (line.find("Owner  :") != -1):
                if ((line.find("Admin") != -1) or (line.find("admin") != -1)):
                    isAdminOwner = True
                break
        if ((os.path.getsize(file) < MAX_FILE_SIZE) and isAdminOwner):
            print("The first file that follows the expected requirements is " + file)
            return file
    raise Exception("There isn't any file that follows the expected requirements")
