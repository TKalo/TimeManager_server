from abc import ABC, abstractmethod

class activity_idb(ABC):

    @abstractmethod
    def getActivities():
        pass

    @abstractmethod
    def addActivity():
        pass

    @abstractmethod
    def deleteActivity():
        pass
