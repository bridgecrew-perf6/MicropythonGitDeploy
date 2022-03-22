import json

class GHFile:
    def __init__(self, clientDirectory, name, url):
        self.name = name
        self.url = url
        self.clientDirectory = clientDirectory
    
    def __str__ (self):
        return self.clientDirectory + " : " + self.name + " -> " + str(self.url)

class GitHubClient:
    def __init__(self, client, userName, repo):
        remoteUrl = '/repos/'+userName+'/'+repo+'/contents'

        self.client = client
        self.files = []
        

        self.parseFolder("/flash", remoteUrl)
    
    def parseFolder(self, clientDirectory, remoteUrl):
        #print("Parse Folder: " + remoteUrl)
        response = self.client.get(remoteUrl)
        
        if response.failed():
            
            if response.needsAuthentication():
                raise Exception("401 Unauthorized, the basicAuthentication in secrets.py needs to be set")
            else:
                print(response.headers)
                raise Exception(response.headers)
            
        jsonObject = json.loads(response.body)

        
        

        for i in jsonObject: 
            name = i["name"]
            type = i["type"]
            if type == "file" and i["download_url"] is not None:
                fileUrl = i["download_url"]
                self.files.append(GHFile(clientDirectory, name, fileUrl))
            elif type == "dir":
                #either a directory in the project or a submodule
                fileUrl = i["url"]
                #print("File URL:" + fileUrl)
                self.parseFolder(clientDirectory + "/"+ name, fileUrl)
            elif type == "file" and i["git_url"] is not None: #Submodule
                git_url = i["git_url"]
                #"git_url": "https://api.github.com/repos/dntoll/ANSIConsole/git/trees/8277ea0646faf079cb3d5b518a57c748dafc178d",
                parts = git_url.split("https://api.github.com")
                repoparts = parts[1].split("/git/trees/")
                #print("parts:")
                #print(repoparts[0])#/repos/dntoll/ANSIConsole
                subModuleRemoteUrl = repoparts[0] + "/contents"
                #either a directory in the project or a submodule
                fileUrl = i["git_url"]
                #print("Submodule URL:" + fileUrl)
                self.parseFolder(clientDirectory + "/"+ name, subModuleRemoteUrl)
