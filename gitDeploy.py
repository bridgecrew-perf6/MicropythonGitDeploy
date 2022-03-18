from HTTPClient import HTTPClient
from GitHubClient import GitHubClient
from LoPyFileSaver import LoPyFileSaver
import secrets
import machine

class gitDeploy:

    def __init__(self, username, repoName):
        self.username = username
        self.repoName = repoName

    def deploy(self):
        c = HTTPClient('api.github.com', secrets.basicAuthentication)
        client = GitHubClient(c, self.username, self.repoName)
        filesToKeep=["secrets.py"]
        ignoreUpload=[".gitmodules", 'pymakr.conf']
        fs = LoPyFileSaver(HTTPClient('raw.githubusercontent.com', secrets.basicAuthentication), filesToKeep, ignoreUpload)
        fs.removeOldFiles()

        for f in client.files:
            fs.downloadAndSave(f.clientDirectory, f.name, f.url)

        machine.reset()