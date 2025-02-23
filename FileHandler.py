import os


class FileHandler:
    def __init__(self, folderPath):
        self.folderPath = folderPath
        self.outputFolder = "outputFiles"

    def getAvailableFiles(self):
        for filename in os.listdir(self.folderPath):
            print(os.path.join(self.folderPath, filename))

    def loadFile(self, filename):
        f = open(self.folderPath + "/" + filename, "rb")
        fileSize = os.path.getsize(self.folderPath + "/" + filename)
        fileContent = f.read()
        f.close()
        return fileContent, fileSize

    def writeFile(self, filename, data):
        f = open(self.outputFolder + "/" + filename, "ab")
        f.write(data)
        f.close()
