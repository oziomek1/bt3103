from abc import ABC, abstractmethod

class playGame(ABC):

    @abstractmethod
    def show_menu(self):
        pass 

    @abstractmethod
    def start(self):
        pass 

class detailsOfGame(playGame):
    # START CODE HERE
    def show_menu(self):
        return "Showing menu"
    
    def start(self):
        return "Starting game!"