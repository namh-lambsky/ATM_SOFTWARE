
import account

#Creacion de la clase Card
class Card():
    def __init__(self, idCard, idAccount):
        #definir atributos de la clase Card
        self.idCard=idCard
        self.idAccount=idAccount

    def getIdCard(self):
        return self.idCard

    def getIdAccount(self):
        return self.idAccount

    def setIdCard(self,idCard):
        self.idCard=idCard

    def setIdAccount(self,idAccount):
        self.idAccount=idAccount