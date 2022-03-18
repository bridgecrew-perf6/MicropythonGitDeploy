
import os

class LoPyFileSaver:
    def __init__(self, httpClient):
        self.client = httpClient

    def removeOldFiles(self):
        
        for fileOrDir in os.listdir():
            if not fileOrDir == "secrets.py":
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
        oldDir = os.getcwd()
        try:
            os.chdir(localFolder)
        except:
            os.mkdir(localFolder)
            os.chdir(localFolder)

        contents = self.client.get(remoteURL)
        parts = contents.decode("utf-8").split("\r\n\r\n", 1)
        filePart = parts[1]

        with open(fileName, 'w') as datafile:
            datafile.write(filePart)
        datafile.close()
        print(fileName + ' written.')
        
        os.chdir(oldDir)
