import mysql.connector
from mysql.connector import Error

#Clase(Data Access Object) que se encarga de conectar la aplicación a la base de datos de MySQL

class DAO():

    #Metodo constructor de la clase que se encarga de conectar a la base de datos

    def __init__(self):
        try:
            self.bankDB = mysql.connector.connect(
                host="bmjk6s1gngsf3waijgnl-mysql.services.clever-cloud.com",
                port="3306",
                user="ujrayhoimysfa94x",
                password="ZtE2N8PEYFLD4jojpFkS",
                database="bmjk6s1gngsf3waijgnl"
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def getTableInfo(self,table):
        if self.bankDB.is_connected():
            if table==1:
                #Metodo para retornar los clientes existentes en la tabla cards
                try:
                    cursor=self.bankDB.cursor()
                    cursor.execute("SELECT * FROM customers ORDER BY idCustomer ASC")
                    result=cursor.fetchall()
                    return result
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
            elif table==2:
                    #Metodo para retornar las cuentas existentes en la tabla accounts
                try:
                    cursor=self.bankDB.cursor()
                    cursor.execute("SELECT * FROM accounts ORDER BY idAccount ASC")
                    result=cursor.fetchall()#crear un array donde se almacenan los datos
                    return result
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
            elif table==3:
                #Metodo para retornar las tarjetas existentes en la tabla cards
                try:
                    cursor=self.bankDB.cursor()
                    cursor.execute("SELECT * FROM cards ORDER BY idCard ASC")
                    result=cursor.fetchall()
                    return result
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))


    def updateAccountBalance(self,idAccount,accountBalance):
        try:
            cursor=self.bankDB.cursor()
            sqlInstruction="UPDATE accounts SET accountBalance='{1}' WHERE idAccount='{0}'"
            cursor.execute(sqlInstruction.format(idAccount, accountBalance))
            self.bankDB.commit()
            print("¡Balance actualizado con exito!")
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

#----------------------------------------------Funciones Cliente
    def newCustomer(self,customer):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="INSERT INTO customers(idCustomer, customerName, customerAddress, customerEmail) VALUES ('{0}','{1}','{2}','{3}')"
                cursor.execute(sqlInstruction.format(customer.getIdCustomer(),customer.getCustomerName(),customer.getCustomerAddress(),customer.getCustomerEmail()))
                self.bankDB.commit()
                print("¡Nuevo Cliente ingresado con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def updateCustomer(self,customer):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE customers SET idCustomer='{0}', customerName='{1}', customerAddress='{2}', customerEmail='{3}' WHERE idCustomer='{0}'"
                cursor.execute(sqlInstruction.format(customer.getIdCustomer(),customer.getCustomerName(),customer.getCustomerAddress(),customer.getCustomerEmail()))
                self.bankDB.commit()
                print("¡Cliente actualizado con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def deleteCustomer(self,idCustomerDelete):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="DELETE FROM customers WHERE idCustomer = '{0}' "
                cursor.execute(sqlInstruction.format(idCustomerDelete))
                self.bankDB.commit()
                print("¡Cliente eliminado con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def selectEmailCustomer(self,email):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursos()
                sqlInstruction="SELECT idCustomer FROM customers WHERE email = '{0}' "
                cursor.execute(sqlInstruction.format(email))
                result=cursor.fetchone()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

#----------------------------------------------Funciones Cuenta
    def newAccount(self,account):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="INSERT INTO accounts(idAccount, accountType, dateCreated, accountPassword, accountBalance, idCustomer) VALUES ('{0}','{1}','{2}',aes_encrypt('{3}','cypherDB'), {4}, {5})"
                cursor.execute(sqlInstruction.format(account.getIdAccount(),account.getAccountType(),account.getDateCreated(), account.getAccountPassword(), account.getAccountBalance(), account.getIdCustomer()))
                self.bankDB.commit()
                print("¡Nueva Cuenta ingresado con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def updateAccount(self,account):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE accounts SET idAccount='{0}', accountType='{1}', dateCreated='{2}', accountPassword=aes_encrypt('{3}','cypherDB'), accountBalance='{4}', idCustomer='{5}' WHERE idAccount='{0}'"
                cursor.execute(sqlInstruction.format(account.getIdAccount(),account.getAccountType(),account.getDateCreated(), account.getAccountPassword(), account.getAccountBalance(), account.getIdCustomer()))
                self.bankDB.commit()
                print("¡Cuenta actualizado con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def deleteAccount(self,idAccountDelete):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="DELETE FROM accounts WHERE idAccount = '{0}' "
                cursor.execute(sqlInstruction.format(idAccountDelete))
                self.bankDB.commit()
                print("¡Cuenta eliminada con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def getAccountPassword(self,id):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                cursor.execute("SELECT cast(aes_decrypt(accountPassword,'cypherDB') as int) FROM accounts WHERE idAccount='{0}'".format(id))
                result=cursor.fetchone()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def updateAccountPassword(self,idAccount,newPassword):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE accounts SET accountPassword=aes_encrypt('{3}','cypherDB') WHERE idAccount='{0}'"
                cursor.execute(sqlInstruction.format(idAccount,newPassword))
                self.bankDB.commit()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def getAccountBalance(self,id):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                cursor.execute("SELECT accountBalance FROM accounts WHERE idAccount='{0}'".format(id))
                result=cursor.fetchone()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def updateAccountBalance(self,idAccount,newBalance):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE accounts SET accountBalance='{1}' WHERE idAccount='{0}'"
                cursor.execute(sqlInstruction.format(idAccount,newBalance))
                self.bankDB.commit()
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def getWithdrawalCount(self,id):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                cursor.execute("SELECT withdrawalCount FROM accounts WHERE idAccount='{0}'".format(id))
                result=cursor.fetchone()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def updateWithdrawalCount(self,idAccount,withdrawalCount):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE accounts SET withdrawalCount='{1}' WHERE idAccount='{0}'"
                cursor.execute(sqlInstruction.format(idAccount,withdrawalCount))
                self.bankDB.commit()
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def getWithdrawalState(self,idAccount):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                cursor.execute("SELECT withdrawalState FROM accounts WHERE idAccount='{0}'".format(idAccount))
                result=cursor.fetchone()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def updateWithdrawalState(self,idAccount,withdrawalState):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE accounts SET withdrawalState='{1}' WHERE idAccount='{0}'"
                cursor.execute(sqlInstruction.format(idAccount,withdrawalState))
                self.bankDB.commit()
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

#----------------------------------------------Funciones Tarjeta
    def newCard(self,card):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="INSERT INTO cards( idCard, idAccount) VALUES ('{0}','{1}')"
                cursor.execute(sqlInstruction.format(card.getIdCard(),card.getIdAccount()))
                self.bankDB.commit()
                print("¡Nueva Tarjeta ingresada con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def updateCard(self,card):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE cards SET idCard='{0}', idAccount='{1}' WHERE idCard='{0}'"
                cursor.execute(sqlInstruction.format(card.getIdCard(),card.getIdAccount()))
                self.bankDB.commit()
                print("¡Tarjeta actualizada con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def deleteCard(self,idCardDelete):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="DELETE FROM cards WHERE idCard = '{0}' "
                cursor.execute(sqlInstruction.format(idCardDelete))
                self.bankDB.commit()
                print("¡Cuenta eliminada con exito!")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def getCardState(self,idCard):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                cursor.execute("SELECT cardState FROM cards WHERE idCard='{0}'".format(idCard))
                result=cursor.fetchone()
                return result
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def getPasswordTries(self,idCard):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                cursor.execute("SELECT passwordTries FROM cards WHERE idCard='{0}'".format(idCard))
                result=cursor.fetchone()
                return result
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))


    def updatePasswordTries(self,idCard,tries):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE cards SET passwordTries='{1}' WHERE idCard='{0}'"
                cursor.execute(sqlInstruction.format(idCard,tries))
                self.bankDB.commit()
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def updateCardState(self,idCard,state):
        if self.bankDB.is_connected():
            try:
                cursor=self.bankDB.cursor()
                sqlInstruction="UPDATE cards SET cardState='{1}' WHERE idCard='{0}'"
                cursor.execute(sqlInstruction.format(idCard,state))
                self.bankDB.commit()
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
