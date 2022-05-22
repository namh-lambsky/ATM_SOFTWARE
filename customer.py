#Creacion de la clase Customer
class Customer():
    def __init__(self, idCustomer, customerName, customerAddress, customerEmail):
        #definir atributos de la clase Customer
        self.idCustomer=idCustomer
        self.customerName=customerName
        self.customerAddress=customerAddress
        self.customerEmail=customerEmail

    #Creacion de los gets
    def getIdCustomer(self):
        return self.idCustomer

    def getCustomerName(self):
        return self.customerName

    def getCustomerAddress(self):
        return self.customerAddress

    def getCustomerEmail(self):
        return self.customerEmail

    def setIdCustomer(self,idCustomer):
        self.idCustomer=idCustomer

    def setCustomerName(self,customerName):
        self.customerName=customerName

    def setCustomerAddress(self,customerAddress):
        self.customerAddress=customerAddress

    def setCustomerEmail(self,customerEmail):
        self.customerEmail=customerEmail