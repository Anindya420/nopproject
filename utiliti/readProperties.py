import configparser
config=configparser.RawConfigParser()
config.read("C:\\Users\\hp\\PycharmProjects\\nopproject\\configuration\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("Common info","baseURL")
        return url
    @staticmethod
    def getUsername():
        username = config.get("Common info","username")
        return username
    @staticmethod
    def getPassword():
        password = config.get("Common info","password")
        return password