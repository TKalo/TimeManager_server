from abc import ABC, abstractmethod

class user_idb(ABC):

    @abstractmethod
    def getUser(user_id):
        pass

    @abstractmethod
    def addUser(email, password):
        pass

    @abstractmethod
    def editUser(email, password):
        pass

    @abstractmethod
    def deleteUser(user_id):
        pass

    

