

import os

class LoPyFileSaver:
    def __init__(self, httpClient, filesToKeep, ignoreUpload):
        self.client = httpClient
        self.filesToKeep = filesToKeep
        self.ignoreUpload = ignoreUpload


    def removeOldFiles(self):
        
        for fileOrDir in os.listdir():
            if not fileOrDir in self.filesToKeep:
                try:
                    os.remove(fileOrDir)
                except:
                    directory = fileOrDir
                    oldDir = os.getcwd()
                    os.chdir(directory)
                    self.removeOldFiles()
                    os.chdir(oldDir)
                    os.rmdir(directory)

    def downloadAndSave(self, localFolder, fileName, remoteURL):


        if fileName in self.ignoreUpload:
            return

        oldDir = os.getcwd()
        try:
            os.chdir(localFolder)
        except:
            os.mkdir(localFolder)
            os.chdir(localFolder)

        response = self.client.get(remoteURL)

        with open(fileName, 'w') as datafile:
            datafile.write(response.body)
        datafile.close()
        print(fileName + ' written to ' +  localFolder)
        
        os.chdir(oldDir)
