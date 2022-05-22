import card

#Creacion de la clase Account
class Account():
    def __init__(self, idAccount, accountType, dateCreated, accountPassword, accountBalance, idCustomer):
        #definir atributos de la clase Account
        self.idAccount=idAccount
        self.accountType=accountType
        self.dateCreated=dateCreated
        self.accountPassword=accountPassword
        self.accountBalance=accountBalance
        self.idCustomer=idCustomer

    #Creacion de los gets
    def getIdAccount(self):
        return self.idAccount

    def getAccountType(self):
        return self.accountType

    def getDateCreated(self):
        return self.dateCreated

    def getAccountPassword(self):
        return self.accountPassword

    def getAccountBalance(self):
        return self.accountBalance

    def getIdCustomer(self):
        return self.idCustomer

    def setIdAccount(self,idAccount):
        self.idAccount=idAccount

    def setAccountType(self,accountType):
        self.accountType=accountType

    def setIdCustomer(self,idCustomer):
        self.idCustomer=idCustomer

    def setDateCreated(self,dateCreated):
        self.dateCreated=dateCreated

    def setAccountPassword(self,accountPassword):
        self.accountPassword=accountPassword

    def setAccountBalance(self,accountBalance):
        self.accountBalance=accountBalance

    def setIdCustomer(self,idCustomer):
        self.idCustomer=idCustomer