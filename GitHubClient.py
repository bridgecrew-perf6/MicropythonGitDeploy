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
        

        folder = self.parseFolder("/flash", remoteUrl)
    
    def parseFolder(self, clientDirectory, remoteUrl):
        print(remoteUrl)
        contents = self.client.get(remoteUrl)
        parts = contents.decode("utf-8").split("\r\n\r\n", 1)
        
        jsonObject = json.loads(parts[1])

        for i in jsonObject: 
            name = i["name"];
            type = i["type"]
            if type == "file":
                fileUrl = i["download_url"]
                self.files.append(GHFile(clientDirectory, name, fileUrl))
            elif type == "dir":
                fileUrl = i["url"]
                print(fileUrl)
                self.parseFolder(clientDirectory + "/"+ name, fileUrl)
        
