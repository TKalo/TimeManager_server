from abc import ABC, abstractmethod

class category_idb(ABC):

    @abstractmethod
    def getCategories(userId):
        pass

    @abstractmethod
    def addCategory(userId, name, color):
        pass

    @abstractmethod
    def deleteCategory(userId, name):
        pass

    

