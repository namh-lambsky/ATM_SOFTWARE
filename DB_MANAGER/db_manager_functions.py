import os
import sys
import re
import datetime
import qrcode
script_dir = os.path.dirname( __file__ )
model_dir = os.path.join( script_dir, 'model')
sys.path.append( model_dir )

from customer import Customer
from account import Account
from card import Card

qr=qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)
#--------------------------------------Funciones Cliente
def showTableCustomers(customers):
    print("==============Tabla Clientes==============\n")
    for customer in customers:
        datos="Id: {0} | Nombre: {1}  (Direccion: {2} | E-mail: {3})"
        print(datos.format(customer[0],customer[1],customer[2],customer[3]))

def newCustomerData():
    emailConfirmPattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    correctID=False
    correctName=False
    correctAddress=False
    correctEmail=False
    while(not correctID):
        idCustomer=input("Ingrese el codigo del cliente: ")
        if len(idCustomer)>=7 and len(idCustomer)<=10:
            correctID=True
        else:
            print("Codigo incorrecto: Debe tener entre 7 y 10 digitos")
    while(not correctName):
        customerName=input("Ingrese el nombre completo del cliente: ")
        if len(customerName)<=255:
            correctName=True
        else:
            print("Nombre incorrecto: Debe ser menor a 255")

    while(not correctAddress):
        customerAddress=input("Ingrese la direccion del cliente: ")
        if len(customerAddress)<=70:
            correctAddress=True
        else:
            print("Direccion incorrecta: Debe ser menor a 255")

    while(not correctEmail):
        customerEmail=input("Ingrese el e-mail del cliente: ")
        if re.fullmatch(emailConfirmPattern,customerEmail):
            correctEmail=True
        else:
            print("E-mail incorrecto: no coincide")
    customer=Customer(int(idCustomer),customerName,customerAddress,customerEmail)
    return customer

def getUpdateData(customers):
    emailConfirmPattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    correctIDtoUpdate=False
    codeExists=False
    correctName=False
    correctAddress=False
    correctEmail=False
    showTableCustomers(customers)
    while(not correctIDtoUpdate):
        idCustomerUpdate=input("Ingrese el codigo del cliente a actualizar: ")
        if len(idCustomerUpdate)>=7 and len(idCustomerUpdate)<=10:
            correctIDtoUpdate=True
        else:
            print("Codigo incorrecto: Debe tener entre 7 y 10 digitos")
    for customer in customers:
        if customer[0]==int(idCustomerUpdate):
            codeExists=True
            break
    if codeExists:
        while(not correctName):
            customerName=input("Ingrese el nombre completo del cliente a actualizar: ")
            if len(customerName)<=255:
                correctName=True
            else:
                print("Nombre incorrecto: Debe ser menor a 255")

        while(not correctAddress):
            customerAddress=input("Ingrese la direccion del cliente a actualizar: ")
            if len(customerAddress)<=70:
                correctAddress=True
            else:
                print("Direccion incorrecta: Debe ser menor a 255")

        while(not correctEmail):
            customerEmail=input("Ingrese el e-mail del cliente a actualizar: ")
            if re.fullmatch(emailConfirmPattern,customerEmail):
                correctEmail=True
            else:
                print("E-mail incorrecto: no coincide")
        customerU=Customer(int(idCustomerUpdate),customerName,customerAddress,customerEmail)

    else:
        customerU=None

    return customerU

def getIDtoDelete(customers):
    correctIDtoDelete=False
    codeExists=False
    showTableCustomers(customers)

    while(not correctIDtoDelete):
        idCustomerDelete=input("Ingrese el codigo del cliente a eliminar: ")
        if len(idCustomerDelete)>=7 and len(idCustomerDelete)<=10:
            correctIDtoDelete=True
        else:
            print("Codigo incorrecto: Debe tener entre 7 y 10 digitos")

    for customer in customers:
        if customer[0]==int(idCustomerDelete):
            codeExists=True
            break

    if not codeExists:
        idCustomerDelete=""

    return idCustomerDelete
#--------------------------------------Funciones Cuenta

def isDate(date):
    format='%d/%m/%Y %I:%M%p'
    confirmDate=False
    try:
        confirmDate=datetime.datetime.strptime(date,format)
    except ValueError:
        confirmDate=False
    return confirmDate

def isNumber(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def showTableAccounts(accounts):
    print("==============Tabla Cuentas==============\n")
    for account in accounts:
        datos="Id de Cuenta: {0} | Id del titular de la cuenta:{5} | Tipo de cuenta: {1}  fecha creada: {2}  contraseña: {3} | balance:{4})"
        print(datos.format(account[0],account[1],account[2],account[3],account[4],account[5]))

def newAccountData():
    passwordConfirmPattern='^\d+$'
    correctIDAcc=False
    correctIDCus=False
    correctAccType=False
    correctDate=False
    correctPassword=False
    correctBalance=False

    while(not correctIDAcc):
        idAccount=input("Ingrese el codigo de la cuenta: ")
        if len(idAccount)>=7 and len(idAccount)<=10:
            correctIDAcc=True
        else:
            print("Codigo de cuenta incorrecto: Debe tener entre 7 y 10 digitos")

    while(not correctIDCus):
        idCustomer=input("Ingrese el codigo del cliente: ")
        if len(idCustomer)>=7 and len(idCustomer)<=10:
            correctIDCus=True
        else:
            print("Codigo de cliente incorrecto: Debe tener entre 7 y 10 digitos")

    while(not correctAccType):
        accountType=input("Ingrese el tipo de cuenta: ").upper()
        if len(accountType)<=50:
            if accountType=="CREDITO" or accountType=="AHORROS" or accountType=="CORRIENTE":
                correctAccType=True
            else:
                print("Tipo de cuenta incorrecto: Tipo de cuenta no existe en el Banco")
        else:
            print("Tipo de cuenta incorrecto: Debe ser menor a 50")

    while(not correctDate):
        dateCreated=input("Ingrese la fecha de creación (Formato: dd/mm/YY Horas:MinutosAM(PM)): ")
        if isDate(dateCreated):
            correctDate=True
        else:
            print("Tipo de fecha de creación errado: no coincide con el formato dd/mm/YY Horas:MinutosAM(PM)")

    while(not correctPassword):
        accountPassword=input("Ingrese la contraseña de la cuenta (Recuerde que deben ser 4 digitos): ")
        if len(accountPassword)==4:
            if re.fullmatch(passwordConfirmPattern,accountPassword):
                correctPassword=True
            else:
                print("Contraseña incorrecta: los digitos de la contraseña no son numeros")
        else:
            print("Contraseña incorrecta: los digitos de la contraseña deben ser 4")

    while(not correctBalance):
        accountBalance=input("Ingrese el balance de la cuenta: ")
        if isNumber(accountBalance):
            correctBalance=True
        else:
            print("Balance incorrecto: no es un valor aceptado")
    dateCreated=datetime.datetime.strptime(dateCreated,'%d/%m/%Y %I:%M%p')
    account=Account(int(idAccount),accountType,dateCreated,int(accountPassword),round(float(accountBalance),2),int(idCustomer))
    return account

def getUpdateDataAccount(accounts):
    passwordConfirmPattern='^\d+$'
    correctIDAcc=False
    correctIDCus=False
    correctAccType=False
    correctDate=False
    correctPassword=False
    correctBalance=False

    while(not correctIDAcc):
        idAccountUpdate=input("Ingrese el codigo de la cuenta: ")
        if len(idAccountUpdate)>=7 and len(idAccountUpdate)<=10:
            correctIDAcc=True
        else:
            print("Codigo de cuenta incorrecto: Debe tener entre 7 y 10 digitos")
    for account in accounts:
        if account[0]==int(idAccountUpdate):
            codeExists=True
            break
    if codeExists:
        while(not correctIDCus):
            idCustomer=input("Ingrese el codigo del cliente: ")
            if len(idCustomer)>=7 and len(idCustomer)<=10:
                correctIDCus=True
            else:
                print("Codigo de cliente incorrecto: Debe tener entre 7 y 10 digitos")

        while(not correctAccType):
            accountType=input("Ingrese el tipo de cuenta: ").upper()
            if len(accountType)<=50:
                if accountType=="CREDITO" or accountType=="AHORROS" or accountType=="CORRIENTE":
                    correctAccType=True
                else:
                    print("Tipo de cuenta incorrecto: Tipo de cuenta no existe en el Banco")
            else:
                print("Tipo de cuenta incorrecto: Debe ser menor a 50")

        while(not correctDate):
            dateCreated=input("Ingrese la fecha de creación (Formato: dd/mm/YY Horas:MinutosAM(PM)): ")
            if isDate(dateCreated):
                correctDate=True
            else:
                print("Tipo de fecha de creación errado: no coincide con el formato dd/mm/YY Horas:MinutosAM(PM)")

        while(not correctPassword):
            accountPassword=input("Ingrese la contraseña de la cuenta (Recuerde que deben ser 4 digitos): ")
            if len(accountPassword)==4:
                if re.fullmatch(passwordConfirmPattern,accountPassword):
                    correctPassword=True
                else:
                    print("Contraseña incorrecta: los digitos de la contraseña no son numeros")
            else:
                print("Contraseña incorrecta: los digitos de la contraseña deben ser 4")

        while(not correctBalance):
            accountBalance=input("Ingrese el balance de la cuenta: ")
            if isNumber(accountBalance):
                correctBalance=True
            else:
                print("Balance incorrecto: no es un valor aceptado")
        dateCreated=datetime.datetime.strptime(dateCreated,'%d/%m/%Y %I:%M%p')
        accountU=Account(int(idAccountUpdate),accountType,dateCreated,int(accountPassword),round(float(accountBalance),2),int(idCustomer))
    else:
        accountU=None
    return accountU

def getIDAccountDelete(accounts):
    correctIDtoDelete=False
    codeExists=False
    showTableAccounts(accounts)
    while(not correctIDtoDelete):
        idAccountDelete=input("Ingrese el codigo del cliente a eliminar: ")
        if len(idAccountDelete)>=7 and len(idAccountDelete)<=10:
            correctIDtoDelete=True
        else:
            print("Codigo incorrecto: Debe tener entre 7 y 10 digitos")

    for account in accounts:
        if account[0]==int(idAccountDelete):
            codeExists=True
            break

    if not codeExists:
        idAccountDelete=""

    return idAccountDelete

#--------------------------------------Funciones Tarjeta

def showTableCards(cards):
    print("==============Tabla Tarjetas==============\n")
    for card in cards:
        datos="Id de la tarjeta: {0} | Id de la cuenta asociada:{1}"
        print(datos.format(card[0],card[1]))

def newCardData():
    correctIDCard=False
    correctIDAcc=False

    while(not correctIDCard):
        idCard=input("Ingrese el codigo de la tarjeta: ")
        if len(idCard)>=7 and len(idCard)<=10:
            correctIDCard=True
        else:
            print("Codigo de la tarjeta incorrecto: Debe tener entre 7 y 10 digitos")

    while(not correctIDAcc):
        idAccount=input("Ingrese el codigo de la cuenta asociada: ")
        if len(idAccount)>=7 and len(idAccount)<=10:
            correctIDAcc=True
        else:
            print("Codigo de cliente incorrecto: Debe tener entre 7 y 10 digitos")

    card=Card(int(idCard),int(idAccount))
    data="{0} {1}".format(int(idCard),int(idAccount))
    qrimg=qrcode.make(data)
    pathQR="DB_MANAGER/QR_CODES/qr{0}.png"
    qrimg.save(pathQR.format(idCard))
    return card

def getUpdateDataCard(cards):
    correctIDCard=False
    correctIDAcc=False
    showTableCards(cards)
    while(not correctIDCard):
        idCard=input("Ingrese el codigo de la tarjeta: ")
        if len(idCard)>=7 and len(idCard)<=10:
            correctIDCard=True
        else:
            print("Codigo de la tarjeta incorrecto: Debe tener entre 7 y 10 digitos")
    for card in cards:
        if card[0]==int(idCard):
            codeExists=True
            break
    if codeExists:
        while(not correctIDAcc):
            idAccount=input("Ingrese el codigo de la cuenta asociada: ")
            if len(idAccount)>=7 and len(idAccount)<=10:
                correctIDAcc=True
            else:
                print("Codigo de la cuenta asociada incorrecto: Debe tener entre 7 y 10 digitos")

        cardU=Card(int(idCard),int(idAccount))
    else:
        cardU=None
    return cardU

def getIDCardDelete(cards):
    correctIDCardDelete=False
    codeExists=False
    showTableCards(cards)
    while(not correctIDCardDelete):
        idCard=input("Ingrese el codigo de la tarjeta: ")
        if len(idCard)>=7 and len(idCard)<=10:
            correctIDCardDelete=True
        else:
            print("Codigo de la tarjeta incorrecto: Debe tener entre 7 y 10 digitos")

    for card in cards:
        if card[0]==int(idCard):
            codeExists=True
            break

    if not codeExists:
        idCard=""

    return idCard