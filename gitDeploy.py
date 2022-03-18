from HTTPClient import HTTPClient
from GitHubClient import GitHubClient
from LoPyFileSaver import LoPyFileSaver
import secrets
import machine

class gitDeploy:

    def __init__(self, username, repoName, filesToKeep, ignoreTheseFiles):
        self.username = username
        self.repoName = repoName
        self.filesToKeep = filesToKeep
        self.ignoreTheseFiles = ignoreTheseFiles

    def deploy(self):
        c = HTTPClient('api.github.com', secrets.basicAuthentication)
        client = GitHubClient(c, self.username, self.repoName)
        
        fs = LoPyFileSaver(HTTPClient('raw.githubusercontent.com', secrets.basicAuthentication), self.filesToKeep, self.ignoreTheseFiles)
        fs.removeOldFiles()

        for f in client.files:
            fs.downloadAndSave(f.clientDirectory, f.name, f.url)

        machine.reset()