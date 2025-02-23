import os


class FileHandler:
    def __init__(self, folderPath):
        self.folderPath = folderPath
        self.outputFolder = "outputFiles"

    def getAvailableFiles(self):
        for filename in os.listdir(self.folderPath):
            print(os.path.join(self.folderPath, filename))

    def loadFile(self, filename):
        f = open(self.folderPath + "\\" + filename, "r")
        fileContent = f.read()
        f.close()
        return fileContent

    def writeFile(self, filename, data):
        f = open(self.outputFolder + "\\" + filename, "a")
        f.write(data)
        f.close()
