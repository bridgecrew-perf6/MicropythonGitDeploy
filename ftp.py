from ftplib import FTP
from os import walk



class FTPPusher:
    def __init__(self, clientIP, username, password):
        self.clientID = clientIP
        self.username = username
        self.password = password

    def _pushAllPyFiles(self, ftp, dirpath, filenames):
        for fileName in filenames:
            if ".py" in fileName:
                completePath = dirpath + "\\" + fileName
                with open(completePath, "rb") as fp:
                    ftp.storbinary("STOR " + fileName, fp)
                print("Wrote: " + completePath + " to device ")

    def push(self):
        with FTP(self.clientID, timeout=10) as ftp:
            mypath = "."
            ftp.login(user=self.username, passwd=self.password)
            ftp.cwd('flash')
            for (dirpath, dirnames, filenames) in walk(mypath):
                if not ".\.git" in dirpath:
                    print("Dirpath:" + dirpath)
                    if "." == dirpath:
                        self._pushAllPyFiles(ftp, dirpath, filenames)

                        #ftp.dir()
                    elif ".\\" in dirpath: #dont push .git
                        
                        dirName = dirpath[2:]
                        onDeviceDirName = 'flash' + "/" + dirName
                        print("path: " + onDeviceDirName)

                        ftp.cwd("..") # step out of flash
                        try:
                            ftp.mkd(onDeviceDirName)
                            print("mkdir " + onDeviceDirName)
                        except:
                            print("dir exists")

                        print("cd " + onDeviceDirName)
                        ftp.cwd(onDeviceDirName)
                        self._pushAllPyFiles(ftp, dirpath, filenames)
                        ftp.cwd("..") #step out to flash
            ftp.close()
            return True


clients = ["192.168.1.138"]
userName = 'micro'
passwd = 'python'


for client in clients:
    f = FTPPusher(client, userName, passwd)
    f.push()