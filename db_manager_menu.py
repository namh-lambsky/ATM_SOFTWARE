from db_connector import DAO
import db_manager_functions as functions

dao=DAO()

def showMenu(menu):
    if menu==0:
        print("=============Menu Principal=============")
        print("1.             Clientes                 ")
        print("2.             Cuentas                  ")
        print("3.             Tarjetas                 ")
        print("4.              Salir                   ")
        print("========================================")

    elif menu==1:
        print("=============Menu Clientes==============")
        print("1.          Mostrar Clientes            ")
        print("2.           Nuevo Cliente              ")
        print("3.         Actualizar Cliente           ")
        print("4.           Borrar Cliente             ")
        print("5.    Regresar al Menu Principal        ")
        print("========================================")

    elif menu==2:
        print("=============Menu Cuentas===============")
        print("1.          Mostrar Cuentas             ")
        print("2.           Nueva Cuenta               ")
        print("3.         Actualizar Cuenta            ")
        print("4.           Borrar Cuenta              ")
        print("5.    Regresar al Menu Principal        ")
        print("========================================")

    elif menu==3:
        print("=============Menu Tarjetas==============")
        print("1.          Mostrar Tarjetas            ")
        print("2.           Nueva Tarjeta              ")
        print("3.         Actualizar Tarjeta           ")
        print("4.           Borrar Tarjeta             ")
        print("5.    Regresar al Menu Principal        ")
        print("========================================")

    try:
        option=int(input('Seleccione una opcion: '))
        print("\n")
    except:
        print("Error! el campo debe ser un numero entero!")
        print("\n")
    return(int(option))


#------------------------------------------------Menu Cliente
def menuCustomers():
    while True:
        menuCustomerOption=showMenu(1)
        if menuCustomerOption==1:
            print("=============Mostrar Clientes=============\n")
            try:
                customers=dao.getTableInfo(1)
                if len(customers)>0:
                    functions.showTableCustomers(customers)
                else:
                    print("La tabla clientes se encuentra vacia\n")
            except Exception as e:
                print("Ocurrio un error..."+str(e))
        elif menuCustomerOption==2:
            print("==============Nuevo Cliente===============\n")
            customer = functions.newCustomerData()
            try:
                dao.newCustomer(customer)
            except Exception as e:
                print("Ocurrio un error..."+str(e))
        elif menuCustomerOption==3:
            print("============Actualizar Cliente============\n")
            try:
                customers=dao.getTableInfo(1)
                if len(customers)>0:
                    customer=functions.getUpdateData(customers)
                    if customer:
                        dao.updateCustomer(customer)
                    else:
                        print("Código de Cliente a actualizar no encontrado...\n")
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuCustomerOption==4:
            print("==============Borrar Cliente==============\n")
            try:
                customers=dao.getTableInfo(1)
                if len(customers)>0:
                    idCustomerDelete=functions.getIDtoDelete(customers)
                    if not(idCustomerDelete == ""):
                        dao.deleteCustomer(int(idCustomerDelete))
                    else:
                        print("Código de Cliente a eliminar no encontrado...\n")
            except Exception as e:
                print("Ocurrio un error..."+str(e))
        elif menuCustomerOption==5:
            print("Volviendo al menu principal!\n")
            break
        else:
            print("Error, Opcion no valida! el campo debe ser un numero entero entre 1 y 5!\n")
#------------------------------------------------Menu Cuenta
def menuAccounts():
    while True:
        menuAccountsOption=showMenu(2)
        if menuAccountsOption==1:
            print("=============Mostrar Cuenta=============\n")
            try:
                accounts=dao.getTableInfo(2)
                if len(accounts)>0:
                    functions.showTableAccounts(accounts)
                else:
                    print("La tabla cuentas se encuentra vacia\n")
            except Exception as e:
                print("Ocurrio un error..."+str(e))
        elif menuAccountsOption==2:
            print("==============Nueva Cuenta===============\n")
            account = functions.newAccountData()
            try:
                dao.newAccount(account)
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuAccountsOption==3:
            print("============Actualizar Cuenta============\n")
            try:
                accounts=dao.getTableInfo(2)
                if len(accounts)>0:
                    account=functions.getUpdateDataAccount(accounts)
                    if account:
                        dao.updateAccount(account)
                    else:
                        print("Código de Cliente a actualizar no encontrado...\n")
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuAccountsOption==4:
            print("==============Borrar Cuenta==============\n")
            try:
                accounts=dao.getTableInfo(2)
                if len(accounts)>0:
                    idAccountDelete=functions.getIDAccountDelete(accounts)
                    if not(idAccountDelete == ""):
                        dao.deleteAccount(int(idAccountDelete))
                    else:
                        print("Código de Cliente a eliminar no encontrado...\n")
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuAccountsOption==5:
            print("Volviendo al menu principal!\n")
            break
        else:
            print("Error, Opcion no valida! el campo debe ser un numero entero entre 1 y 5!\n")
#------------------------------------------------Menu Tarjeta
def menuCards():
    while True:
        menuCardsOption=showMenu(3)
        if menuCardsOption==1:
            print("=============Mostrar Tarjetas=============\n")
            try:
                cards=dao.getTableInfo(3)
                if len(cards)>0:
                    functions.showTableCards(cards)
                else:
                    print("La tabla tarjetas se encuentra vacia\n")
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuCardsOption==2:
            print("==============Nueva Tarjeta===============\n")
            card = functions.newCardData()
            try:
                dao.newCard(card)
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuCardsOption==3:
            print("============Actualizar Tarjeta============\n")
            try:
                cards=dao.getTableInfo(3)
                if len(cards)>0:
                    card=functions.getUpdateDataCard(cards)
                    print(card)
                    if card:
                        dao.updateCard(card)
                    else:
                        print("Código de tarjeta a actualizar no encontrado...\n")
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuCardsOption==4:
            print("==============Borrar Tarjeta==============\n")
            try:
                cards=dao.getTableInfo(3)
                if len(cards)>0:
                    idCardDelete=functions.getIDCardDelete(cards)
                    if not(idCardDelete == ""):
                        dao.deleteCard(int(idCardDelete))
                    else:
                        print("Código de tarjeta a eliminar no encontrado...\n")
            except Exception as e:
                print("Ocurrio un error... " + str(e))
        elif menuCardsOption==5:
            print("Volviendo al menu principal!\n")
            break
        else:
            print("Error, Opcion no valida! el campo debe ser un numero entero entre 1 y 5!\n")
#------------------------------------------------Menu Principal
def mainMenu():
    while True:
        mainMenuOption=showMenu(0)
        if mainMenuOption==1:
            menuCustomers()
        elif mainMenuOption==2:
            menuAccounts()
        elif mainMenuOption==3:
            menuCards()
        elif mainMenuOption==4:
            print("Programa Finalizado!\n")
            break
        else:
            print("Error, Opcion no valida! el campo debe ser un numero entero entre 1 y 4!\n")

mainMenu()