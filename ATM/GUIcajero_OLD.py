from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import os
import sys
import cv2
import time
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

MenuPrincipal= Frame(ventana)
ingresarTarjeta= Frame(ventana)
ingresarSinTarjeta= Frame(ventana)
MenuTransaccion= Frame(ventana)
IngresoTarjetaContraseña= Frame(ventana)
retirarDinero= Frame(ventana)
consultarSaldo= Frame(ventana)
transferencias= Frame(ventana)
transferenciasOp= Frame(ventana)
transferenciaNumeroDeCuenta= Frame(ventana)
ConfirmaciónCuenta= Frame(ventana)
CodigoDeBarras= Frame(ventana)
ImprimirRecibo= Frame(ventana)
NuevoSaldo= Frame(ventana)

framesList=[MenuPrincipal, ingresarTarjeta,ingresarSinTarjeta, IngresoTarjetaContraseña,MenuTransaccion, retirarDinero, consultarSaldo, transferencias, transferenciasOp, transferenciaNumeroDeCuenta, ConfirmaciónCuenta, CodigoDeBarras, ImprimirRecibo, NuevoSaldo]

#imagenes
fondo= Image.open("ATM/IMAGES/Pantallaprincipal.png")
resizeImagef=fondo.resize((1250,580))
fondo= ImageTk.PhotoImage(resizeImagef)

fondoingresarTarjeta= Image.open("ATM/IMAGES/IngreseCodigoTarjeta.png")
resizeImagef=fondoingresarTarjeta.resize((1250,580))
fondoingresarTarjeta= ImageTk.PhotoImage(resizeImagef)

fondoIngresarSinTarjeta= Image.open("ATM/IMAGES/3.png")
resizeImagef=fondoIngresarSinTarjeta.resize((1250,580))
fondoIngresarSinTarjeta= ImageTk.PhotoImage(resizeImagef)

fondoIngresarIdTarjeta= Image.open("ATM/IMAGES/IngreseCodigoTarjeta.png")
resizeImagef=fondoIngresarIdTarjeta.resize((1250,580))
fondoIngresarIdTarjeta= ImageTk.PhotoImage(resizeImagef)

fondoMenuTransaccion= Image.open("ATM/IMAGES/MenuTransaccion.png")
resizeImagef=fondoMenuTransaccion.resize((1250,580))
fondoMenuTransaccion= ImageTk.PhotoImage(resizeImagef)

fondoIngresoTarjetaContraseña= Image.open("ATM/IMAGES/IngresoTarjetaContraseña.png")
resizeImagef=fondoIngresoTarjetaContraseña.resize((1250,580))
fondoIngresoTarjetaContraseña= ImageTk.PhotoImage(resizeImagef)

fondoRetirarDinero= Image.open("ATM/IMAGES/RetirarDinero.png")
resizeImagef=fondoRetirarDinero.resize((1250,580))
fondoRetirarDinero= ImageTk.PhotoImage(resizeImagef)

fondoConsultarSaldo= Image.open("ATM/IMAGES/ConsultarSaldo.png")
resizeImagef=fondoConsultarSaldo.resize((1250,580))
fondoConsultarSaldo= ImageTk.PhotoImage(resizeImagef)

fondoTransferencias= Image.open("ATM/IMAGES/Transferencias.png")
resizeImagef=fondoTransferencias.resize((1250,580))
fondoTransferencias= ImageTk.PhotoImage(resizeImagef)

fondoTransferenciasOp= Image.open("ATM/IMAGES/TransferenciasOp.png")
resizeImagef=fondoTransferenciasOp.resize((1250,580))
fondoTransferenciasOp= ImageTk.PhotoImage(resizeImagef)

fondoTransferenciaNumeroDeCuenta= Image.open("ATM/IMAGES/TransferenciaNumeroDeCuenta.png")
resizeImagef=fondoTransferenciaNumeroDeCuenta.resize((1250,580))
fondoTransferenciaNumeroDeCuenta= ImageTk.PhotoImage(resizeImagef)

fondoConfirmacionCuenta= Image.open("ATM/IMAGES/ConfirmacionCuenta.png")
resizeImagef=fondoConfirmacionCuenta.resize((1250,580))
fondoConfirmacionCuenta= ImageTk.PhotoImage(resizeImagef)

fondoCodigoDeBarras= Image.open("ATM/IMAGES/CodigoDeBarras.png")
resizeImagef=fondoCodigoDeBarras.resize((1250,580))
fondoCodigoDeBarras= ImageTk.PhotoImage(resizeImagef)

fondoImprimirRecibo= Image.open("ATM/IMAGES/ImprimirRecibo.png")
resizeImagef=fondoImprimirRecibo.resize((1250,580))
fondoImprimirRecibo= ImageTk.PhotoImage(resizeImagef)

fondoNuevoSaldo= Image.open("ATM/IMAGES/NuevoSaldo.png")
resizeImagef=fondoNuevoSaldo.resize((1250,580))
fondoNuevoSaldo= ImageTk.PhotoImage(resizeImagef)


#iconos
contraseñaIcon= Image.open("ATM/IMAGES/EntryShape.png")
resizeImageC=contraseñaIcon.resize((300,50))
contraseñaIcon=ImageTk.PhotoImage(resizeImageC)

def framesManager(framesList, frame_name,tx=""):
        for frame in framesList:
            frame.grid(row=0,column=0,sticky="nsew")
        frame_name.tkraise()

framesManager(framesList,MenuPrincipal)

#MenuPrincipal---------------------------------------------------------
#dataList=c.getCardInfo()
#label
MenuPrincipalFondo =Label(MenuPrincipal, image=fondo)
MenuPrincipalFondo.place(x=0,y=0)

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
    framesManager(framesList,IngresoTarjetaContraseña)
#botones
MenuPrincipalBtIngresarTarjeta= Button(MenuPrincipal, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: loadQR())
MenuPrincipalBtIngresarTarjeta.place(x=15,y=435)

MenuPrincipalBtIngresarSinTarjeta= Button(MenuPrincipal, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: framesManager(framesList,ingresarSinTarjeta))
MenuPrincipalBtIngresarSinTarjeta.place(x=1175,y=435)


#Comando para la validación del entry(que sean 4 digitos y que sean numeros)
def validate_entryC(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 10:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()

#MenuingresarTarjeta---------------------------------------------------------
ingresarTarjetafondo=Label(ingresarTarjeta, image=fondoingresarTarjeta)
ingresarTarjetafondo.place(x=0,y=0)

IngresoTarjetaCodigoTx = Entry(ingresarTarjeta, width=6,font=("Helvetica",24),border=0)
IngresoTarjetaCodigoTx.place(x=630,y=204)
IngresoTarjetaCodigoTx.focus_set()
IngresoTarjetaCodigoTx.config(validate='key',validatecommand=(ventana.register(validate_entryC), "%S", "%P"))

#botones ingresarTarjeta
ingresarTarjetaBtIngresar= Button(ingresarTarjeta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: getCardInfo())
ingresarTarjetaBtIngresar.place(x=100,y=345)

ingresarTarjetaBt2Ingresar= Button(ingresarTarjeta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuPrincipal))
ingresarTarjetaBt2Ingresar.place(x=100,y=445)

#IngresoTarjetaContraseña---------------------------------------------------------------------------------

IngresoTarjetaContraseñafondo=Label(IngresoTarjetaContraseña, image=fondoIngresoTarjetaContraseña)
IngresoTarjetaContraseñafondo.place(x=0,y=0)

IngresoTarjetaContraseñaLb=Label(IngresoTarjetaContraseña,image=contraseñaIcon,border=0)
IngresoTarjetaContraseñaLb.place(x=510,y=200)

#Comando para la validación del entry(que sean 4 digitos y que sean numeros)
def validate_entry(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 4:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()

#Entry para el ingreso de la contraseña
IngresoTarjetaContraseñaTx = Entry(IngresoTarjetaContraseña, show="*",width=6,font=("Helvetica",24),border=0)
IngresoTarjetaContraseñaTx.place(x=630,y=204)
IngresoTarjetaContraseñaTx.config(validate='key',validatecommand=(ventana.register(validate_entry), "%S", "%P"))
IngresoTarjetaContraseñaTx.focus_set()

def login(ingresoTarjetaContraseñaTx,cardInfoList=None):
    passCount=c.getPasswordTries(cardInfoList)
    if c.cardIsBlocked(cardInfoList):
        messagebox.showerror(message="Tarjeta Bloqueada")
        framesManager(framesList,MenuPrincipal)
    else:
        if passCount==0:
            c.updatePasswordTries(cardInfoList)
            messagebox.showerror(message="Se agotaron sus intentos de inicio de sesion, Tarjeta Bloqueada")
            framesManager(framesList,MenuPrincipal)
        else:
            if c.passwordValidation(cardInfoList,ingresoTarjetaContraseñaTx.get()):
                framesManager(framesList,MenuTransaccion)
            else:
                passCount-=1
                messagebox.showerror(message="contraseña errada le quedan {0} intentos".format(passCount))
                ingresoTarjetaContraseñaTx.delete("0","end")
                c.updatePasswordTries(cardInfoList)

#botones IngresoTarjeta
IngresoTarjetaBtIngresar= Button(IngresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#7ed957",command = lambda:login(IngresoTarjetaContraseñaTx,cardInfoList))
IngresoTarjetaBtIngresar.place(x=100,y=345)

IngresoTarjetaBtFinalizar= Button(IngresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(IngresoTarjetaContraseñaTx,framesList,MenuPrincipal))
IngresoTarjetaBtFinalizar.place(x=100,y=445)

#ingresarSinTarjeta----------------------------------------------------------------

ingresarSinTarjetafondo=Label(ingresarSinTarjeta, image=fondoIngresarSinTarjeta)
ingresarSinTarjetafondo.place(x=0,y=0)

IngresoSinTarjetaContraseñaLb=Label(ingresarSinTarjeta,image=contraseñaIcon,border=0)
IngresoSinTarjetaContraseñaLb.place(x=510,y=210)

IngresoSinTarjetaContraseñaTx= Entry(ingresarSinTarjeta, show="*",width=10,font=("Helvetica",24),border=0)
IngresoSinTarjetaContraseñaTx.place(x=557,y=214)

#BotonesingresarSinTarjeta

ingresarSinTarjetaBtIngresar= Button(ingresarSinTarjeta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.clearTextInput(IngresoSinTarjetaContraseñaTx,framesList,MenuTransaccion))
ingresarSinTarjetaBtIngresar.place(x=100,y=345)

ingresarSinTarjetaBt2Ingresar= Button(ingresarSinTarjeta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(IngresoSinTarjetaContraseñaTx,framesList,MenuPrincipal))
ingresarSinTarjetaBt2Ingresar.place(x=100,y=445)

#MenuTransaccion--------------------------------------------------------------------------

MenuTransaccionfondo=Label(MenuTransaccion, image=fondoMenuTransaccion)
MenuTransaccionfondo.place(x=0,y=0)

#botones MenuTransaccion
MenuTransaccionBtIngresar= Button(MenuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: c.framesManager(framesList,retirarDinero))
MenuTransaccionBtIngresar.place(x=25,y=160)

MenuTransaccion2BtIngresar= Button(MenuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: c.framesManager(framesList,consultarSaldo))
MenuTransaccion2BtIngresar.place(x=25,y=295)

MenuTransaccion3BtIngresar= Button(MenuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: c.framesManager(framesList,transferencias))
MenuTransaccion3BtIngresar.place(x=1170,y=160)

#Retirar Dinero-----------------------------------------------------------------------------------------------
RetirarDinerofondo=Label(retirarDinero, image=fondoRetirarDinero)
RetirarDinerofondo.place(x=0,y=0)

RetirarDineroLb=Label(retirarDinero,image=contraseñaIcon,border=0)
RetirarDineroLb.place(x=510,y=200)

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
#entry

RetirarDineroTx= Entry(retirarDinero,width=10,font=("Helvetica",24),border=0)
RetirarDineroTx.place(x=557,y=204)
RetirarDineroTx.focus_set()
RetirarDineroTx.config(validate='key',validatecommand=(ventana.register(validate_entryR), "%S", "%P"))


#botones RetirarDinero

RetirarDineroBtIngresar= Button(retirarDinero, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.validateR(RetirarDineroTx,RetirarDineroTx.get(),framesList,consultarSaldo))
RetirarDineroBtIngresar.place(x=100,y=345)

RetirarDineroBt2Ingresar= Button(retirarDinero, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(RetirarDineroTx,framesList,MenuTransaccion))
RetirarDineroBt2Ingresar.place(x=100,y=445)

#Consultar saldo-------------------------------------------------------------------------------------------------

#label
ConsultarSaldoFondo =Label(consultarSaldo, image=fondoConsultarSaldo)
ConsultarSaldoFondo.place(x=0,y=0)


#botones
ConsultarSaldoBtImprimir= Button(consultarSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,ImprimirRecibo))
ConsultarSaldoBtImprimir.place(x=15,y=290)

ConsultarSaldoBtVer= Button(consultarSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,NuevoSaldo))
ConsultarSaldoBtVer.place(x=1175,y=290)


#transferencias-----------------------------------------------------------------------------------------------------

#label
transferenciasFondo =Label(transferencias, image=fondoTransferencias)
transferenciasFondo.place(x=0,y=0)


#botones
transferenciasBtAhorro= Button(transferencias, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,transferenciasOp))
transferenciasBtAhorro.place(x=15,y=270)

transferenciasBtCorriente= Button(transferencias, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,transferenciasOp))
transferenciasBtCorriente.place(x=1175,y=270)

#TransferenciasOp----------------------------------------------------------------------------------------------------

#label
transferenciasOpFondo =Label(transferenciasOp, image=fondoTransferenciasOp)
transferenciasOpFondo.place(x=0,y=0)


#botones
transferenciasOpBtNumero= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,transferenciaNumeroDeCuenta))
transferenciasOpBtNumero.place(x=15,y=270)

transferenciasOpBtCodigo= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,CodigoDeBarras))
transferenciasOpBtCodigo.place(x=1175,y=270)

#transferenciaNumeroDeCuenta--------------------------------------------------------------------------------------------

transferenciaNumeroDeCuentafondo=Label(transferenciaNumeroDeCuenta, image=fondoTransferenciaNumeroDeCuenta)
transferenciaNumeroDeCuentafondo.place(x=0,y=0)

transferenciaNumeroDeCuentafondoLb=Label(transferenciaNumeroDeCuenta,image=contraseñaIcon,border=0)
transferenciaNumeroDeCuentafondoLb.place(x=510,y=200)

#




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
transferenciaNumeroDeCuentaTx.focus_set()
transferenciaNumeroDeCuentaTx.config(validate='key',validatecommand=(ventana.register(validate_entryN), "%S", "%P"))

#botones transferenciaNumeroDeCuenta

transferenciaNumeroDeCuentaBtIngresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.clearTextInput(transferenciaNumeroDeCuentaTx,framesList,ConfirmaciónCuenta))
transferenciaNumeroDeCuentaBtIngresar.place(x=100,y=345)

transferenciaNumeroDeCuentaBt2Ingresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(transferenciaNumeroDeCuentaTx,framesList,MenuTransaccion))
transferenciaNumeroDeCuentaBt2Ingresar.place(x=100,y=445)

#ConfirmaciónCuenta-------------------------------------------------------------------------------------------------------

#label
ConfirmaciónCuentaFondo =Label(ConfirmaciónCuenta, image=fondoConfirmacionCuenta)
ConfirmaciónCuentaFondo.place(x=0,y=0)


#botones
ConfirmaciónCuentaBtIngresar= Button(ConfirmaciónCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.framesManager(framesList,consultarSaldo))
ConfirmaciónCuentaBtIngresar.place(x=100,y=345)

ConfirmaciónCuentaBt2Ingresar= Button(ConfirmaciónCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuTransaccion))
ConfirmaciónCuentaBt2Ingresar.place(x=100,y=445)

#CodigoDeBarras-------------------------------------------------------------------------------------------------------------

CodigoDeBarrasfondo=Label(CodigoDeBarras, image=fondoCodigoDeBarras)
CodigoDeBarrasfondo.place(x=0,y=0)


#Botones

CodigoDeBarrasBtIngresar= Button(CodigoDeBarras, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.framesManager(framesList,ConfirmaciónCuenta))
CodigoDeBarrasBtIngresar.place(x=100,y=345)

CodigoDeBarrasBt2Ingresar= Button(CodigoDeBarras, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuTransaccion))
CodigoDeBarrasBt2Ingresar.place(x=100,y=445)

#ImprimirRecibo------------------------------------------------------------------------------------------------------------------------

ImprimirRecibofondo=Label(ImprimirRecibo, image=fondoImprimirRecibo)
ImprimirRecibofondo.place(x=0,y=0)


#Botones

ImprimirReciboBtIngresar= Button(ImprimirRecibo, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuPrincipal))
ImprimirReciboBtIngresar.place(x=100,y=345)

#NuevoSaldo-----------------------------------------------------------------------------------------------------------------------------

NuevoSaldofondo=Label(NuevoSaldo, image=fondoNuevoSaldo)
NuevoSaldofondo.place(x=0,y=0)

#Botones

NuevoSaldoBtIngresar= Button(NuevoSaldo, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuPrincipal))
NuevoSaldoBtIngresar.place(x=100,y=345)


    





ventana.mainloop()
