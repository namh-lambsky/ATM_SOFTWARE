from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import os
import sys
import cv2
import time
from numpy import imag
from pyzbar.pyzbar import decode
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, 'ATM_CONTROLLER')
sys.path.append( controller_dir )
from atm_functions import controller

c=controller()
ventana=Tk()
ventana.geometry("1250x580")
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)
ventana.resizable (0,0)
ventana.iconbitmap('ATM/IMAGES/LogoBancolombia.ico')
ventana.title('Cajero Automatico Bancolombia')
#Numero de paginas

menuPrincipal= Frame(ventana)
ingresarTarjeta= Frame(ventana)
ingresarSinTarjeta= Frame(ventana)
ingresoCorreo= Frame(ventana)
menuTransaccion= Frame(ventana)
ingresoTarjetaContraseña= Frame(ventana)
retirarDinero= Frame(ventana)
consultarSaldo= Frame(ventana)
transferencias= Frame(ventana)
transferenciasOp= Frame(ventana)
transferenciaNumeroDeCuenta= Frame(ventana)
confirmaciónCuenta= Frame(ventana)
codigoDeBarras= Frame(ventana)
imprimirRecibo= Frame(ventana)
nuevoSaldo= Frame(ventana)
cambioContraseña=Frame(ventana)
otroMonto=Frame(ventana)
cambioContraseñaR= Frame(ventana)

framesList=[menuPrincipal, ingresarTarjeta,ingresarSinTarjeta, ingresoTarjetaContraseña,menuTransaccion, retirarDinero, consultarSaldo, transferencias, transferenciasOp, transferenciaNumeroDeCuenta, confirmaciónCuenta, codigoDeBarras, imprimirRecibo, nuevoSaldo, otroMonto, cambioContraseña, cambioContraseñaR]

def framesManager(framesList, frame_name,tx=""):
        for frame in framesList:
            frame.grid(row=0,column=0,sticky="nsew")
        frame_name.tkraise()

framesManager(framesList,menuPrincipal)

#imagenes
bgMainMenu= Image.open("ATM/IMAGES/Pantallaprincipal.png")
resizeImagef=bgMainMenu.resize((1250,580))
bgMainMenu= ImageTk.PhotoImage(resizeImagef)

bgIngresarTarjeta= Image.open("ATM/IMAGES/IngreseCodigoTarjeta.png")
resizeImagef=bgIngresarTarjeta.resize((1250,580))
bgIngresarTarjeta= ImageTk.PhotoImage(resizeImagef)

bgIngresarSinTarjeta= Image.open("ATM/IMAGES/3.png")
resizeImagef=bgIngresarSinTarjeta.resize((1250,580))
bgIngresarSinTarjeta= ImageTk.PhotoImage(resizeImagef)

bgIngresoCorreo= Image.open("ATM/IMAGES/IngresoCorreo.png")
resizeImagef=bgIngresoCorreo.resize((1250,580))
bgIngresoCorreo= ImageTk.PhotoImage(resizeImagef)

bgIngresarIdTarjeta= Image.open("ATM/IMAGES/IngreseCodigoTarjeta.png")
resizeImagef=bgIngresarIdTarjeta.resize((1250,580))
bgIngresarIdTarjeta= ImageTk.PhotoImage(resizeImagef)

bgMenuTransaccion= Image.open("ATM/IMAGES/MenuTransaccion.png")
resizeImagef=bgMenuTransaccion.resize((1250,580))
bgMenuTransaccion= ImageTk.PhotoImage(resizeImagef)

fondoIngresoTarjetaContraseña= Image.open("ATM/IMAGES/IngresoTarjetaContraseña.png")
resizeImagef=fondoIngresoTarjetaContraseña.resize((1250,580))
fondoIngresoTarjetaContraseña= ImageTk.PhotoImage(resizeImagef)

bgRetiroDinero= Image.open("ATM/IMAGES/MenuRetiro.png")
resized_image=bgRetiroDinero.resize((1250,580))
bgRetiroDinero= ImageTk.PhotoImage(resized_image)

bgConsultarSaldo= Image.open("ATM/IMAGES/ConsultarSaldo.png")
resizeImagef=bgConsultarSaldo.resize((1250,580))
bgConsultarSaldo= ImageTk.PhotoImage(resizeImagef)

bgTransferencias= Image.open("ATM/IMAGES/Transferencias.png")
resizeImagef=bgTransferencias.resize((1250,580))
bgTransferencias= ImageTk.PhotoImage(resizeImagef)

bgTransferenciasOp= Image.open("ATM/IMAGES/TransferenciasOp.png")
resizeImagef=bgTransferenciasOp.resize((1250,580))
bgTransferenciasOp= ImageTk.PhotoImage(resizeImagef)

bgTransferenciaNumeroDeCuenta= Image.open("ATM/IMAGES/TransferenciaNumeroDeCuenta.png")
resizeImagef=bgTransferenciaNumeroDeCuenta.resize((1250,580))
bgTransferenciaNumeroDeCuenta= ImageTk.PhotoImage(resizeImagef)

bgConfirmacionCuenta= Image.open("ATM/IMAGES/ConfirmacionCuenta.png")
resizeImagef=bgConfirmacionCuenta.resize((1250,580))
bgConfirmacionCuenta= ImageTk.PhotoImage(resizeImagef)

bgCodigoDeBarras= Image.open("ATM/IMAGES/CodigoDeBarras.png")
resizeImagef=bgCodigoDeBarras.resize((1250,580))
bgCodigoDeBarras= ImageTk.PhotoImage(resizeImagef)

bgImprimirRecibo= Image.open("ATM/IMAGES/ImprimirRecibo.png")
resizeImagef=bgImprimirRecibo.resize((1250,580))
bgImprimirRecibo= ImageTk.PhotoImage(resizeImagef)

bgNuevoSaldo= Image.open("ATM/IMAGES/MenuSaldoPantalla.png")
resizeImagef=bgNuevoSaldo.resize((1250,580))
bgNuevoSaldo= ImageTk.PhotoImage(resizeImagef)

bgOtroMonto=Image.open("ATM/IMAGES/OtroMonto.png")
resizeImagef=bgOtroMonto.resize((1250,580))
bgOtroMonto=ImageTk.PhotoImage(resizeImagef)

bgCambioConstraseña=Image.open("ATM/IMAGES/CambioContraseña.png")
resizeImagef=bgCambioConstraseña.resize((1250,580))
bgCambioConstraseña=ImageTk.PhotoImage(resizeImagef)

bgCambioConstraseñaR=Image.open("ATM/IMAGES/CambioContraseñaR.png")
resizeImagef=bgCambioConstraseñaR.resize((1250,580))
bgCambioConstraseñaR=ImageTk.PhotoImage(resizeImagef)

#iconos
contraseñaIcon= Image.open("ATM/IMAGES/EntryShape.png")
resizeImageC=contraseñaIcon.resize((300,50))
contraseñaIcon=ImageTk.PhotoImage(resizeImageC)

entryHiddenIcon=Image.open("ATM/IMAGES/EntryHidden.png")
resizeImageE=entryHiddenIcon.resize((506,226))
entryHiddenIcon=ImageTk.PhotoImage(resizeImageE)

#menuPrincipal---------------------------------------------------------

#label
menuPrincipalFondo =Label(menuPrincipal, image=bgMainMenu)
menuPrincipalFondo.place(x=0,y=0)

#Funcion para registrar los datos recibidos por la camara
def getCardInfo():
            cap=cv2.VideoCapture(0)
            cap.set(3,640)
            cap.set(4,480)
            used_codes=[]
            camera=True
            while camera:
                    success,frame=cap.read()
                    for code in decode(frame):
                        if code.data.decode('utf-8') not in used_codes:
                            cardInfo=code.data.decode('utf-8')
                            global cardInfoList
                            cardInfoList=cardInfo.split()
                            used_codes.append(code.data.decode('utf-8'))
                            time.sleep(5)
                            camera=False
                        elif code.data.decode('utf-8') in used_codes:
                            messagebox.showerror(message="La camara ya esta activada",title="Error!")
                            time.sleep(5)
                        else:
                            pass
                    cv2.imshow("IngresoTarjeta",frame)
                    cv2.waitKey(1)
            cap.release()
            cv2.destroyWindow("IngresoTarjeta")

def loadQR():
    getCardInfo()
    framesManager(framesList,ingresoTarjetaContraseña)
    ingresoTarjetaContraseñaTx.focus_set()
#botones
menuPrincipalBtIngresarTarjeta= Button(menuPrincipal, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: loadQR())
menuPrincipalBtIngresarTarjeta.place(x=15,y=435)

#menuPrincipalBtIngresarSinTarjeta= Button(menuPrincipal, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: framesManager(framesList,ingresarSinTarjeta))
#menuPrincipalBtIngresarSinTarjeta.place(x=1175,y=435)

#Comando para la validación del entry(que sean 4 digitos y que sean numeros)
def validate_entryC(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 10:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()

#MenuingresarTarjeta---------------------------------------------------------
ingresarTarjetafondo=Label(ingresarTarjeta, image=bgIngresarTarjeta)
ingresarTarjetafondo.place(x=0,y=0)

IngresoTarjetaCodigoTx = Entry(ingresarTarjeta, width=6,font=("Helvetica",24),border=0)
IngresoTarjetaCodigoTx.place(x=630,y=204)
IngresoTarjetaCodigoTx.focus_set()
IngresoTarjetaCodigoTx.config(validate='key',validatecommand=(ventana.register(validate_entryC), "%S", "%P"))

#botones ingresarTarjeta
ingresarTarjetaBtIngresar= Button(ingresarTarjeta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: getCardInfo())
ingresarTarjetaBtIngresar.place(x=100,y=345)

ingresarTarjetaBt2Ingresar= Button(ingresarTarjeta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,menuPrincipal))
ingresarTarjetaBt2Ingresar.place(x=100,y=445)

#IngresoTarjetaContraseña---------------------------------------------------------------------------------

ingresoTarjetaContraseñafondo=Label(ingresoTarjetaContraseña, image=fondoIngresoTarjetaContraseña)
ingresoTarjetaContraseñafondo.place(x=0,y=0)

ingresoTarjetaContraseñaLb=Label(ingresoTarjetaContraseña,image=contraseñaIcon,border=0)
ingresoTarjetaContraseñaLb.place(x=510,y=200)

#Comando para la validación del entry(que sean 4 digitos y que sean numeros)
def validate_entry(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 4:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()

#Entry para el ingreso de la contraseña
ingresoTarjetaContraseñaTx = Entry(ingresoTarjetaContraseña, show="*",width=6,font=("Helvetica",24),border=0)
ingresoTarjetaContraseñaTx.place(x=630,y=204)
ingresoTarjetaContraseñaTx.config(validate='key',validatecommand=(ventana.register(validate_entry), "%S", "%P"))

def login(ingresoTarjetaContraseñaTx,cardInfoList=None):
    passCount=c.getPasswordTries(cardInfoList)
    if c.cardIsBlocked(cardInfoList):
        messagebox.showerror(message="Tarjeta Bloqueada")
        framesManager(framesList,menuPrincipal)
    else:
        if passCount==0:
            c.updatePasswordTries(cardInfoList)
            messagebox.showerror(message="Se agotaron sus intentos de inicio de sesion, Tarjeta Bloqueada")
            framesManager(framesList,menuPrincipal)
        else:
            if c.passwordValidation(cardInfoList,ingresoTarjetaContraseñaTx.get()):
                ingresoTarjetaContraseñaTx.delete("0","end")
                framesManager(framesList,menuTransaccion)
            else:
                passCount-=1
                messagebox.showerror(message="contraseña errada le quedan {0} intentos".format(passCount))
                ingresoTarjetaContraseñaTx.delete("0","end")
                c.updatePasswordTries(cardInfoList)

#botones IngresoTarjeta
IngresoTarjetaBtIngresar= Button(ingresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#7ed957",command = lambda:login(ingresoTarjetaContraseñaTx,cardInfoList))
IngresoTarjetaBtIngresar.place(x=100,y=345)

IngresoTarjetaBtFinalizar= Button(ingresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(ingresoTarjetaContraseñaTx,framesList,menuPrincipal))
IngresoTarjetaBtFinalizar.place(x=100,y=445)

#CambioContraseña

cambioContraseñafondo= Label(cambioContraseña, image=bgCambioConstraseña)
cambioContraseñafondo.place(x=0,y=0)

#Comando para la validación del entry(que sean 4 digitos y que sean numeros)
def validate_entryCambio(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 4:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()

def loadCambioContraseñaR():
    global password
    password=cambioContraseñaTx.get()
    framesManager(framesList,cambioContraseñaR)
    cambioContraseñaRTx.focus_set()

#Entry para el cambio de la contraseña
cambioContraseñaTx = Entry(cambioContraseña, show="*",width=6,font=("Helvetica",24),border=0)
cambioContraseñaTx.place(x=590,y=220)
cambioContraseñaTx.config(validate='key',validatecommand=(ventana.register(validate_entryCambio), "%S", "%P"))

#botones CambioContraseña
cambioContraseñaBtIngresar= Button(cambioContraseña, padx=25,border=0, pady=15, bg="#7ed957",command=lambda: loadCambioContraseñaR())
cambioContraseñaBtIngresar.place(x=100,y=345)

cambioContraseñaBtFinalizar= Button(cambioContraseña, padx=25,border=0, pady=15, bg="#e61717",command=lambda: framesManager(framesList, menuTransaccion))
cambioContraseñaBtFinalizar.place(x=100,y=445)


#CambioContraseñaR

cambioContraseñaRfondo= Label(cambioContraseñaR, image=bgCambioConstraseñaR)
cambioContraseñaRfondo.place(x=0,y=0)

#Comando para la validación del entry(que sean 4 digitos y que sean numeros)
def validate_entryCambio(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 4:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()


def changePassword(cambioContraseñaTx,cambioContraseñaRTx,cardInfoList):
    if cambioContraseñaTx==cambioContraseñaRTx:
        if c.updatePassword(cardInfoList,cambioContraseñaRTx):
            messagebox.showinfo(message="La contraseña fue actualizada exitosamente")
            framesManager(framesList,menuTransaccion)
    else:
        messagebox.showerror(message="Las contraseñas no coinciden, ingresela de nuevo")
        framesManager(framesList,cambioContraseña)

#Entry para el cambio de la contraseña
cambioContraseñaRTx = Entry(cambioContraseñaR, show="*",width=6,font=("Helvetica",24),border=0)
cambioContraseñaRTx.place(x=590,y=220)
cambioContraseñaRTx.config(validate='key',validatecommand=(ventana.register(validate_entryCambio), "%S", "%P"))

#botones CambioContraseña
cambioContraseñaRBtIngresar= Button(cambioContraseñaR, padx=25,border=0, pady=15, bg="#7ed957",command=lambda: changePassword(password,cambioContraseñaRTx.get(),cardInfoList))
cambioContraseñaRBtIngresar.place(x=100,y=345)

cambioContraseñaRBtFinalizar= Button(cambioContraseñaR, padx=25,border=0, pady=15, bg="#e61717",command=lambda: framesManager(framesList, menuTransaccion))
cambioContraseñaRBtFinalizar.place(x=100,y=445)

#MenuTransaccion--------------------------------------------------------------------------

menuTransaccionfondo=Label(menuTransaccion, image=bgMenuTransaccion)
menuTransaccionfondo.place(x=0,y=0)

def loadBalance(cardInfoList):
    retrieveAccountBalance(cardInfoList,nuevoSaldoLbSaldo)
    framesManager(framesList,nuevoSaldo)

def retrieveAccountBalance(cardInfoList,labelText):
    currentBalance=str(c.getAccountBalance(cardInfoList))
    labelText.config(text=currentBalance)
    return currentBalance

def loadCambioContraseña():
    framesManager(framesList,cambioContraseña)
    cambioContraseñaTx.focus_set()

#botones MenuTransaccion
menuTransaccionBtRetirarDinero= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: framesManager(framesList,retirarDinero))
menuTransaccionBtRetirarDinero.place(x=25,y=150)

menuTransaccionBtConsultaSaldo= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: loadBalance(cardInfoList))
menuTransaccionBtConsultaSaldo.place(x=25,y=285)

menuTransaccionBtSalir= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: framesManager(framesList,menuPrincipal))
menuTransaccionBtSalir.place(x=25,y=420)

menuTransaccionBtTransferencias= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: framesManager(framesList,transferenciasOp))
menuTransaccionBtTransferencias.place(x=1170,y=150)

menuTransaccionBtCambioContraseña= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: loadCambioContraseña())
menuTransaccionBtCambioContraseña.place(x=1170,y=285)

#Retirar Dinero-----------------------------------------------------------------------------------------------
retirarDinerofondo=Label(retirarDinero, image=bgRetiroDinero)
retirarDinerofondo.place(x=0,y=0)

#Comando de validacion

def validate_entryR(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 7:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()


#Comando para la validación del entry(que sean >10000 digitos y que sean numeros)
def validate_entryRetiro(text):
    if int(text) < 2700000 and int(text) %5==0:
        return True
    else:
        print("Su numero ingresado no es correcto intente de nuevo")
#Funcion para realizar el retiro del dinero dada el id de la cuenta y la cantidad a retirar

def loadWithdrawalMessage(amount,cardInfoList):
    withdrawalCount=c.getWithdrawalCount(cardInfoList)
    if c.accountIsBlocked(cardInfoList):
        messagebox.showerror(message="Error: Ya supero el maximo de retiros diarios, retornado al menu transacciones")
        framesManager(framesList,menuTransaccion)
    else:
        if withdrawalCount==0:
            c.updateWithdrawalCount(cardInfoList)
        else:
            if c.withdrawal(amount,cardInfoList):
                messagebox.showinfo(message="¡Transaccion Exitosa! no olvide retirar su dinero")
                framesManager(framesList,menuTransaccion)
                c.updateWithdrawalCount(cardInfoList)
            else:
                messagebox.showerror(message="Error: Saldo Insuficiente, retornado al menu transacciones")
                framesManager(framesList,menuTransaccion)

def loadOtroMonto():
    framesManager(framesList,otroMonto)
    otroMontoTx.focus_set()

#botones RetirarDinero
bt_Pagina_Retiros_10000= Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222", command=lambda:loadWithdrawalMessage(10000,cardInfoList))
bt_Pagina_Retiros_10000.place(x=25,y=75)

bt_Pagina_Retiros_150000=Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222", command=lambda:loadWithdrawalMessage(150000,cardInfoList))
bt_Pagina_Retiros_150000.place(x=1170,y=75)

bt_Pagina_Retiros_20000=Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222", command=lambda:loadWithdrawalMessage(20000,cardInfoList))
bt_Pagina_Retiros_20000.place(x=25,y=185)

bt_Pagina_Retiros_250000=Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222", command=lambda:loadWithdrawalMessage(250000,cardInfoList))
bt_Pagina_Retiros_250000.place(x=1170,y=185)

bt_Pagina_Retiros_50000=Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222", command=lambda:loadWithdrawalMessage(50000,cardInfoList))
bt_Pagina_Retiros_50000.place(x=25,y=300)

bt_Pagina_Retiros_350000= Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222", command=lambda:loadWithdrawalMessage(350000,cardInfoList))
bt_Pagina_Retiros_350000.place(x=1170,y=300)

menuTransaccionBtRetirarDineroOtroValor= Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222", command= loadOtroMonto)
menuTransaccionBtRetirarDineroOtroValor.place(x=1170,y=430)

bt_Pagina_Retiros_Finalizar= Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222",command= lambda: framesManager(framesList,menuTransaccion))
bt_Pagina_Retiros_Finalizar.place(x=25,y=430)
#Otro Monto-------------------------------------------------------------------------------------------------

bgOtroMontoLabel= Label(otroMonto, image=bgOtroMonto)
bgOtroMontoLabel.place(x=0,y=0)

otroMontoTx= Entry(otroMonto,width=10,font=("Helvetica",24),border=0)
otroMontoTx.config(validate='key',validatecommand=(ventana.register(validate_entryR), "%S", "%P"))
otroMontoTx.place(x=557,y=225)

#botones
otroMontoBtIngresar= Button(otroMonto, padx=25,border=0, pady=15, bg="#7ed957", command= lambda: loadWithdrawalMessage(float(otroMontoTx.get())))
otroMontoBtIngresar.place(x=100,y=345)

otroMontoBtMenuT= Button(otroMonto, padx=25,border=0, pady=15, bg="#e61717",command = lambda: framesManager(framesList,retirarDinero))
otroMontoBtMenuT.place(x=100,y=445)

#Consultar saldo-------------------------------------------------------------------------------------------------

#label
consultarSaldoFondo =Label(consultarSaldo, image=bgConsultarSaldo)
consultarSaldoFondo.place(x=0,y=0)

#botones
consultarSaldoBtImprimir= Button(consultarSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,imprimirRecibo))
consultarSaldoBtImprimir.place(x=15,y=290)

consultarSaldoBtVer= Button(consultarSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,nuevoSaldo))
consultarSaldoBtVer.place(x=1175,y=290)

#TransferenciasOp----------------------------------------------------------------------------------------------------

#label
transferenciasOpFondo =Label(transferenciasOp, image=bgTransferenciasOp)
transferenciasOpFondo.place(x=0,y=0)

def loadNumeroDeCuenta():
    framesManager(framesList,transferenciaNumeroDeCuenta)
    transferenciaNumeroDeCuentaTx.focus_set()

#botones
transferenciasOpBtNumero= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: loadNumeroDeCuenta)
transferenciasOpBtNumero.place(x=15,y=270)

transferenciasOpBtCodigo= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda:framesManager(framesList,codigoDeBarras))
transferenciasOpBtCodigo.place(x=1175,y=270)

#transferenciaNumeroDeCuenta--------------------------------------------------------------------------------------------

transferenciaNumeroDeCuentafondo=Label(transferenciaNumeroDeCuenta, image=bgTransferenciaNumeroDeCuenta)
transferenciaNumeroDeCuentafondo.place(x=0,y=0)

transferenciaNumeroDeCuentafondoLb=Label(transferenciaNumeroDeCuenta,image=contraseñaIcon,border=0)
transferenciaNumeroDeCuentafondoLb.place(x=510,y=200)

#Verificacion

def validate_entryN(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 10:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()

transferenciaNumeroDeCuentaTx= Entry(transferenciaNumeroDeCuenta,width=10,font=("Helvetica",24),border=0)
transferenciaNumeroDeCuentaTx.place(x=557,y=204)
transferenciaNumeroDeCuentaTx.config(validate='key',validatecommand=(ventana.register(validate_entryN), "%S", "%P"))

#botones transferenciaNumeroDeCuenta

transferenciaNumeroDeCuentaBtIngresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.clearTextInput(transferenciaNumeroDeCuentaTx,framesList,confirmaciónCuenta))
transferenciaNumeroDeCuentaBtIngresar.place(x=100,y=345)

transferenciaNumeroDeCuentaBt2Ingresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(transferenciaNumeroDeCuentaTx,framesList,menuTransaccion))
transferenciaNumeroDeCuentaBt2Ingresar.place(x=100,y=445)

#ConfirmaciónCuenta-------------------------------------------------------------------------------------------------------

#label
ConfirmaciónCuentaFondo =Label(confirmaciónCuenta, image=bgConfirmacionCuenta)
ConfirmaciónCuentaFondo.place(x=0,y=0)

#botones
ConfirmaciónCuentaBtIngresar= Button(confirmaciónCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.framesManager(framesList,consultarSaldo))
ConfirmaciónCuentaBtIngresar.place(x=100,y=345)

ConfirmaciónCuentaBt2Ingresar= Button(confirmaciónCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,menuTransaccion))
ConfirmaciónCuentaBt2Ingresar.place(x=100,y=445)

#CodigoDeBarras-------------------------------------------------------------------------------------------------------------

CodigoDeBarrasfondo=Label(codigoDeBarras, image=bgCodigoDeBarras)
CodigoDeBarrasfondo.place(x=0,y=0)

#Botones

CodigoDeBarrasBtIngresar= Button(codigoDeBarras, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.framesManager(framesList,confirmaciónCuenta))
CodigoDeBarrasBtIngresar.place(x=100,y=345)

CodigoDeBarrasBt2Ingresar= Button(codigoDeBarras, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,menuTransaccion))
CodigoDeBarrasBt2Ingresar.place(x=100,y=445)

#ImprimirRecibo------------------------------------------------------------------------------------------------------------------------

imprimirRecibofondo=Label(imprimirRecibo, image=bgImprimirRecibo)
imprimirRecibofondo.place(x=0,y=0)


#Botones

imprimirReciboBtIngresar= Button(imprimirRecibo, padx=25,border=0, pady=15, bg="#e61717",command = lambda: framesManager(framesList,menuPrincipal))
imprimirReciboBtIngresar.place(x=100,y=345)

#NuevoSaldo-----------------------------------------------------------------------------------------------------------------------------

nuevoSaldofondo=Label(nuevoSaldo, image=bgNuevoSaldo)
nuevoSaldofondo.place(x=0,y=0)

nuevoSaldoLbSaldo=Label(nuevoSaldo,text="",width=10,font=("Helvetica",24),border=0,background="white")
nuevoSaldoLbSaldo.place(x=525,y=250)

#Botones

nuevoSaldoBtMenuT= Button(nuevoSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: framesManager(framesList,menuTransaccion))
nuevoSaldoBtMenuT.place(x=100,y=355)

nuevoSaldoBtCerrarSesion= Button(nuevoSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: framesManager(framesList,menuPrincipal))
nuevoSaldoBtCerrarSesion.place(x=100,y=450)


ventana.mainloop()
