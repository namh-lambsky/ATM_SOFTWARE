from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import time
from pyzbar.pyzbar import decode
from tkinter.font import Font
from atm_functions import controller

ventana=Tk()
ventana.iconbitmap('IMAGES/LogoBancolombia.ico')
ventana.title('')
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)
ventana.geometry("1250x580")
ventana.resizable (0,0)
c=controller()

#Numero de paginas

menuPrincipal= Frame(ventana)
ingresarTarjeta= Frame(ventana)
menuTransaccion= Frame(ventana)
ingresoTarjetaContraseña= Frame(ventana)
retirarDinero= Frame(ventana)
transferenciasOp= Frame(ventana)
transferenciaNumeroDeCuenta= Frame(ventana)
confirmacionCuenta= Frame(ventana)
nuevoSaldo= Frame(ventana)
cambioContraseña=Frame(ventana)
otroMonto=Frame(ventana)
cambioContraseñaR= Frame(ventana)
ingresarMontoTransferencia= Frame(ventana)

#fuente de letra

fuenteLetra= Font(
    family="Helvetica",
    size=20,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0
)

framesList=[menuPrincipal, ingresarTarjeta, ingresoTarjetaContraseña,menuTransaccion, retirarDinero, transferenciasOp, transferenciaNumeroDeCuenta, confirmacionCuenta, nuevoSaldo, otroMonto, cambioContraseña, cambioContraseñaR,ingresarMontoTransferencia]
for frame in framesList:
    frame.grid(row=0,column=0,sticky="nsew")

def framesManager(frame_name):
        frame_name.tkraise()

def clearText(frame_name,entry):
    entry.delete("0","end")
    framesManager(frame_name)

framesManager(menuPrincipal)

#imagenes
bgMainMenu= Image.open("IMAGES/Pantallaprincipal.png")
resizeImagef=bgMainMenu.resize((1250,580))
bgMainMenu= ImageTk.PhotoImage(resizeImagef)

bgIngresarTarjeta= Image.open("IMAGES/IngreseCodigoTarjeta.png")
resizeImagef=bgIngresarTarjeta.resize((1250,580))
bgIngresarTarjeta= ImageTk.PhotoImage(resizeImagef)

bgIngresarSinTarjeta= Image.open("IMAGES/3.png")
resizeImagef=bgIngresarSinTarjeta.resize((1250,580))
bgIngresarSinTarjeta= ImageTk.PhotoImage(resizeImagef)

bgIngresoCorreo= Image.open("IMAGES/IngresoCorreo.png")
resizeImagef=bgIngresoCorreo.resize((1250,580))
bgIngresoCorreo= ImageTk.PhotoImage(resizeImagef)

bgIngresarIdTarjeta= Image.open("IMAGES/IngreseCodigoTarjeta.png")
resizeImagef=bgIngresarIdTarjeta.resize((1250,580))
bgIngresarIdTarjeta= ImageTk.PhotoImage(resizeImagef)

bgMenuTransaccion= Image.open("IMAGES/MenuTransaccion.png")
resizeImagef=bgMenuTransaccion.resize((1250,580))
bgMenuTransaccion= ImageTk.PhotoImage(resizeImagef)

fondoIngresoTarjetaContraseña= Image.open("IMAGES/IngresoTarjetaContraseña.png")
resizeImagef=fondoIngresoTarjetaContraseña.resize((1250,580))
fondoIngresoTarjetaContraseña= ImageTk.PhotoImage(resizeImagef)

bgRetiroDinero= Image.open("IMAGES/MenuRetiro.png")
resized_image=bgRetiroDinero.resize((1250,580))
bgRetiroDinero= ImageTk.PhotoImage(resized_image)

bgConsultarSaldo= Image.open("IMAGES/ConsultarSaldo.png")
resizeImagef=bgConsultarSaldo.resize((1250,580))
bgConsultarSaldo= ImageTk.PhotoImage(resizeImagef)

bgTransferencias= Image.open("IMAGES/Transferencias.png")
resizeImagef=bgTransferencias.resize((1250,580))
bgTransferencias= ImageTk.PhotoImage(resizeImagef)

bgTransferenciasOp= Image.open("IMAGES/TransferenciasOp.png")
resizeImagef=bgTransferenciasOp.resize((1250,580))
bgTransferenciasOp= ImageTk.PhotoImage(resizeImagef)

bgTransferenciaNumeroDeCuenta= Image.open("IMAGES/TransferenciaNumeroDeCuenta.png")
resizeImagef=bgTransferenciaNumeroDeCuenta.resize((1250,580))
bgTransferenciaNumeroDeCuenta= ImageTk.PhotoImage(resizeImagef)

bgConfirmacionCuenta= Image.open("IMAGES/ConfirmacionCuenta.png")
resizeImagef=bgConfirmacionCuenta.resize((1250,580))
bgConfirmacionCuenta= ImageTk.PhotoImage(resizeImagef)

bgCodigoDeBarras= Image.open("IMAGES/CodigoDeBarras.png")
resizeImagef=bgCodigoDeBarras.resize((1250,580))
bgCodigoDeBarras= ImageTk.PhotoImage(resizeImagef)

bgImprimirRecibo= Image.open("IMAGES/ImprimirRecibo.png")
resizeImagef=bgImprimirRecibo.resize((1250,580))
bgImprimirRecibo= ImageTk.PhotoImage(resizeImagef)

bgNuevoSaldo= Image.open("IMAGES/MenuSaldoPantalla.png")
resizeImagef=bgNuevoSaldo.resize((1250,580))
bgNuevoSaldo= ImageTk.PhotoImage(resizeImagef)

bgOtroMonto=Image.open("IMAGES/OtroMonto.png")
resizeImagef=bgOtroMonto.resize((1250,580))
bgOtroMonto=ImageTk.PhotoImage(resizeImagef)

bgCambioConstraseña=Image.open("IMAGES/CambioContraseña.png")
resizeImagef=bgCambioConstraseña.resize((1250,580))
bgCambioConstraseña=ImageTk.PhotoImage(resizeImagef)

bgCambioConstraseñaR=Image.open("IMAGES/CambioContraseñaR.png")
resizeImagef=bgCambioConstraseñaR.resize((1250,580))
bgCambioConstraseñaR=ImageTk.PhotoImage(resizeImagef)

bgRetiroConfirmacion=Image.open("IMAGES/RetiroConfirmacion.png")
resizeImagef=bgRetiroConfirmacion.resize((1250,580))
bgRetiroConfirmacion=ImageTk.PhotoImage(resizeImagef)

bgTranseferenciaMonto=Image.open("IMAGES/TransferenciaEntry.png")
resizeImagef=bgTranseferenciaMonto.resize((1250,580))
bgTranseferenciaMonto=ImageTk.PhotoImage(resizeImagef)

#iconos
contraseñaIcon= Image.open("IMAGES/EntryShape.png")
resizeImageC=contraseñaIcon.resize((300,50))
contraseñaIcon=ImageTk.PhotoImage(resizeImageC)

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
                    sucess,frame=cap.read()
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
    framesManager(ingresoTarjetaContraseña)
    ingresoTarjetaContraseñaTx.focus_set()
#botones
menuPrincipalBtIngresarTarjeta= Button(menuPrincipal, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: loadQR())
menuPrincipalBtIngresarTarjeta.place(x=15,y=435)

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

ingresarTarjetaBtFinalizar= Button(ingresarTarjeta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: framesManager(menuPrincipal))
ingresarTarjetaBtFinalizar.place(x=100,y=445)

#IngresoTarjetaContraseña---------------------------------------------------------------------------------

ingresoTarjetaContraseñafondo=Label(ingresoTarjetaContraseña, image=fondoIngresoTarjetaContraseña)
ingresoTarjetaContraseñafondo.place(x=0,y=0)

ingresoTarjetaContraseñaLb=Label(ingresoTarjetaContraseña,image=contraseñaIcon,border=0)
ingresoTarjetaContraseñaLb.place(x=510,y=200)

ingresoContraseñaErrorLb1=Label(ingresoTarjetaContraseña,text="",width=50,font=fuenteLetra,border=0, foreground="red", background="white")
ingresoContraseñaErrorLb1.place(x=320,y=100)

ingresoContraseñaErrorLb2=Label(ingresoTarjetaContraseña,text="",width=70,font=fuenteLetra,border=0, foreground="red", background="white")
ingresoContraseñaErrorLb2.place(x=200,y=100)

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
        retrieveErrorMessage(ingresoContraseñaErrorLb1,"TARJETA BLOQUEADA")
        #messagebox.showerror(message="Tarjeta Bloqueada")
        ingresoTarjetaContraseñaTx.delete("0","end")
        framesManager(menuPrincipal)
    else:
        if passCount==0:
            c.updatePasswordTries(cardInfoList)
            retrieveErrorMessage(ingresoContraseñaErrorLb2,"SE AGOTARON SUS INTENTOS DE INICIO DE SESION, TARJETA BLOQUEADA")
            #messagebox.showerror(message="Se agotaron sus intentos de inicio de sesion, Tarjeta Bloqueada")
            ingresoTarjetaContraseñaTx.delete("0","end")
            framesManager(menuPrincipal)
        else:
            if c.passwordValidation(cardInfoList,ingresoTarjetaContraseñaTx.get()):
                ingresoTarjetaContraseñaTx.delete("0","end")
                framesManager(menuTransaccion)
            else:
                passCount-=1
                retrieveErrorMessage(ingresoContraseñaErrorLb2,"CONTRASEÑA ERRADA LE QUEDAN {0} INTENTOS".format(passCount))
                #messagebox.showerror(message="contraseña errada le quedan {0} intentos".format(passCount))
                ingresoTarjetaContraseñaTx.delete("0","end")
                c.updatePasswordTries(cardInfoList)

#botones IngresoTarjeta
IngresoTarjetaBtIngresar= Button(ingresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#7ed957",command = lambda:login(ingresoTarjetaContraseñaTx,cardInfoList))
IngresoTarjetaBtIngresar.place(x=100,y=345)

IngresoTarjetaBtFinalizar= Button(ingresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#e61717",command = lambda: clearText(menuPrincipal,ingresoTarjetaContraseñaTx))
IngresoTarjetaBtFinalizar.place(x=100,y=445)

#CambioContraseña

cambioContraseñafondo= Label(cambioContraseña, image=bgCambioConstraseña)
cambioContraseñafondo.place(x=0,y=0)
cambioContraseñafondoErrorLb=Label(cambioContraseña,text="",width=50,font=fuenteLetra,border=0, foreground="red", background="white")
cambioContraseñafondoErrorLb.place(x=410,y=100)

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
    framesManager(cambioContraseñaR)
    cambioContraseñaRTx.focus_set()
    cambioContraseñaTx.delete("0","end")

#Entry para el cambio de la contraseña
cambioContraseñaTx = Entry(cambioContraseña, show="*",width=6,font=("Helvetica",24),border=0)
cambioContraseñaTx.place(x=590,y=220)
cambioContraseñaTx.config(validate='key',validatecommand=(ventana.register(validate_entryCambio), "%S", "%P"))

#botones CambioContraseña
cambioContraseñaBtIngresar= Button(cambioContraseña, padx=25,border=0, pady=15, bg="#7ed957",command=lambda: loadCambioContraseñaR())
cambioContraseñaBtIngresar.place(x=100,y=345)

cambioContraseñaBtFinalizar= Button(cambioContraseña, padx=25,border=0, pady=15, bg="#e61717",command=lambda: clearText(menuPrincipal,cambioContraseñaTx))
cambioContraseñaBtFinalizar.place(x=100,y=445)

#CambioContraseñaR

cambioContraseñaRfondo= Label(cambioContraseñaR, image=bgCambioConstraseñaR)
cambioContraseñaRfondo.place(x=0,y=0)
cambioContraseñaRfondoErrorLb=Label(cambioContraseñaR,text="",width=100,font=fuenteLetra,border=0, foreground="red", background="white")
cambioContraseñaRfondoErrorLb.place(x=410,y=100)

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
            retrieveErrorMessage(cambioContraseñaRfondoErrorLb,"LA CONSTRASEÑA FUE ACTUALIZADA EXITOSAMENTE")
            #messagebox.showinfo(message="La contraseña fue actualizada exitosamente")
            cambioContraseñaTx.delete("0","end")
            cambioContraseñaRTx.delete("0","end")
            framesManager(menuTransaccion)
    else:
        retrieveErrorMessage(cambioContraseñaRfondoErrorLb,"LAS CONSTRASEÑAS NO COINCIDEN, INGRESELA DE NUEVO")
        #messagebox.showerror(message="Las contraseñas no coinciden, ingresela de nuevo")
        cambioContraseñaTx.delete("0","end")
        cambioContraseñaRTx.delete("0","end")
        framesManager(cambioContraseña)

#Entry para el cambio de la contraseña
cambioContraseñaRTx = Entry(cambioContraseñaR, show="*",width=6,font=("Helvetica",24),border=0)
cambioContraseñaRTx.place(x=590,y=220)
cambioContraseñaRTx.config(validate='key',validatecommand=(ventana.register(validate_entryCambio), "%S", "%P"))

#botones CambioContraseña
cambioContraseñaRBtIngresar= Button(cambioContraseñaR, padx=25,border=0, pady=15, bg="#7ed957",command=lambda: changePassword(password,cambioContraseñaRTx.get(),cardInfoList))
cambioContraseñaRBtIngresar.place(x=100,y=345)

cambioContraseñaRBtFinalizar= Button(cambioContraseñaR, padx=25,border=0, pady=15, bg="#e61717",command=lambda: clearText(menuPrincipal,cambioContraseñaRTx))
cambioContraseñaRBtFinalizar.place(x=100,y=445)

#MenuTransaccion--------------------------------------------------------------------------

menuTransaccionfondo=Label(menuTransaccion, image=bgMenuTransaccion)
menuTransaccionfondo.place(x=0,y=0)

def loadBalance(cardInfoList):
    retrieveAccountBalance(cardInfoList,nuevoSaldoLbSaldo)
    framesManager(nuevoSaldo)

def retrieveAccountBalance(cardInfoList,labelText):
    currentBalance=str(c.getAccountBalance(cardInfoList))
    labelText.config(text=currentBalance)

def retrieveErrorMessage(labelText,message):
    labelText.config(text=message)
    time.sleep(5)

def loadCambioContraseña():
    framesManager(cambioContraseña)
    cambioContraseñaTx.focus_set()

#botones MenuTransaccion
menuTransaccionBtRetirarDinero= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: framesManager(retirarDinero))
menuTransaccionBtRetirarDinero.place(x=25,y=150)

menuTransaccionBtConsultaSaldo= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: loadBalance(cardInfoList))
menuTransaccionBtConsultaSaldo.place(x=25,y=285)

menuTransaccionBtSalir= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: framesManager(menuPrincipal))
menuTransaccionBtSalir.place(x=25,y=420)

menuTransaccionBtTransferencias= Button(menuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: framesManager(transferenciasOp))
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
    if amount < 10000:
        retrieveErrorMessage(otroMontoErrorLb,"EL NUMERO NO ES VALIDO INTENTE DE NUEVO")
        #messagebox.showerror(message="Error: El numero no es valido intente de nuevo")
        otroMontoTx.delete("0","end")
    else:
        if c.accountIsBlocked(cardInfoList):
            messagebox.showerror(message="Error: Ya supero el maximo de retiros diarios, retornado al menu transacciones")
            otroMontoTx.delete("0","end")
            framesManager(menuTransaccion)
        else:
            if withdrawalCount==0:
                c.updateWithdrawalCount(cardInfoList)
                otroMontoTx.delete("0","end")
            else:
                if c.withdrawal(amount,cardInfoList):
                    messagebox.showinfo(message="¡Transaccion Exitosa! no olvide retirar su dinero")
                    c.updateWithdrawalCount(cardInfoList)
                    otroMontoTx.delete("0","end")
                    framesManager(menuTransaccion)
                else:
                    messagebox.showerror(message="Error: Saldo Insuficiente, retornado al menu transacciones")
                    otroMontoTx.delete("0","end")
                    framesManager(menuTransaccion)

def loadOtroMonto():
    framesManager(otroMonto)
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

bt_Pagina_Retiros_Finalizar= Button(retirarDinero, padx=25, pady=15,border=0, bg="#DD5222",command= lambda: framesManager(menuTransaccion))
bt_Pagina_Retiros_Finalizar.place(x=25,y=430)

#Otro Monto-------------------------------------------------------------------------------------------------

bgOtroMontoLabel= Label(otroMonto, image=bgOtroMonto)
bgOtroMontoLabel.place(x=0,y=0)
otroMontoErrorLb=Label(otroMonto,text="",width=50,font=fuenteLetra,border=0, foreground="red", background="white")
otroMontoErrorLb.place(x=390,y=100)

otroMontoTx= Entry(otroMonto,width=10,font=("Helvetica",24),border=0)
otroMontoTx.config(validate='key',validatecommand=(ventana.register(validate_entryR), "%S", "%P"))
otroMontoTx.place(x=557,y=225)

#botones
otroMontoBtIngresar= Button(otroMonto, padx=25,border=0, pady=15, bg="#7ed957", command= lambda: loadWithdrawalMessage(float(otroMontoTx.get()),cardInfoList))
otroMontoBtIngresar.place(x=100,y=345)

otroMontoBtMenuT= Button(otroMonto, padx=25,border=0, pady=15, bg="#e61717",command = lambda: clearText(menuPrincipal,otroMontoTx))
otroMontoBtMenuT.place(x=100,y=445)

#TransferenciasOp----------------------------------------------------------------------------------------------------

#label
transferenciasOpFondo =Label(transferenciasOp, image=bgTransferenciasOp)
transferenciasOpFondo.place(x=0,y=0)

def loadNumeroDeCuenta():
    framesManager(transferenciaNumeroDeCuenta)
    transferenciaNumeroDeCuentaTx.focus_set()

def getCardToTransfer():
            capT=cv2.VideoCapture(0)
            capT.set(3,640)
            capT.set(4,480)
            used_codes=[]
            camera=True
            while camera:
                    success,frame=capT.read()
                    for code in decode(frame):
                        if code.data.decode('utf-8') not in used_codes:
                            cardInfo=code.data.decode('utf-8')
                            global cardInfoTList
                            cardInfoTList=cardInfo.split()
                            used_codes.append(code.data.decode('utf-8'))
                            time.sleep(5)
                            camera=False
                        elif code.data.decode('utf-8') in used_codes:
                            messagebox.showerror(message="La camara ya esta activada",title="Error!")
                            time.sleep(5)
                        else:
                            pass
                    cv2.imshow("IngresoTarjetaTransaccion",frame)
                    cv2.waitKey(1)
            capT.release()
            cv2.destroyWindow("IngresoTarjetaTransaccion")

def loadQRTransfer():
    getCardToTransfer()
    loadAccIdLbl(1)

def loadAccIdLbl(fromPage):
    framesManager(confirmacionCuenta)
    global idAccountTransfer
    if fromPage==0:
        idAccountTransfer=numeroCuenta
        confirmacionCuentaLabel.config(text="¿EL NUMERO DE CUENTA: {0} ES A QUIEN\n DESEA HACER LA TRANSFERENCIA?".format(numeroCuenta))
    else:
        idAccountTransfer=cardInfoTList[1]
        confirmacionCuentaLabel.config(text="¿EL NUMERO DE CUENTA: {0} ES A QUIEN\n DESEA HACER LA TRANSFERENCIA?".format(cardInfoTList[1]))
#botones
transferenciasOpBtNumero= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: loadNumeroDeCuenta())
transferenciasOpBtNumero.place(x=15,y=270)

transferenciasOpBtCodigo= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda:loadQRTransfer())
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

transferenciaNumeroDeCuentaBtIngresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda:getNumeroCuenta())
transferenciaNumeroDeCuentaBtIngresar.place(x=100,y=345)

transferenciaNumeroDeCuentaBtRegresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: framesManager(menuTransaccion))
transferenciaNumeroDeCuentaBtRegresar.place(x=100,y=445)

#funcion transferencia
def getNumeroCuenta():
    global numeroCuenta
    numeroCuenta=transferenciaNumeroDeCuentaTx.get()
    loadAccIdLbl(0)

#ConfirmaciónCuenta-------------------------------------------------------------------------------------------------------

#label
ConfirmaciónCuentaFondo =Label(confirmacionCuenta, image=bgConfirmacionCuenta)
ConfirmaciónCuentaFondo.place(x=0,y=0)

confirmacionCuentaLabel=Label(confirmacionCuenta,text="",width=70,font=fuenteLetra,border=0,background="white")
confirmacionCuentaLabel.place(x=90,y=200)


#botones
ConfirmaciónCuentaBtIngresar= Button(confirmacionCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: framesManager(ingresarMontoTransferencia))
ConfirmaciónCuentaBtIngresar.place(x=100,y=345)

ConfirmaciónCuentaBtRegresar= Button(confirmacionCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: framesManager(transferenciasOp))
ConfirmaciónCuentaBtRegresar.place(x=100,y=445)


#NuevoSaldo-----------------------------------------------------------------------------------------------------------------------------

nuevoSaldofondo=Label(nuevoSaldo, image=bgNuevoSaldo)
nuevoSaldofondo.place(x=0,y=0)

nuevoSaldoLbSaldo=Label(nuevoSaldo,text="",width=10,font=("Helvetica",24),border=0,background="white")
nuevoSaldoLbSaldo.place(x=525,y=250)

#Botones

nuevoSaldoBtMenuT= Button(nuevoSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: framesManager(menuTransaccion))
nuevoSaldoBtMenuT.place(x=100,y=355)

nuevoSaldoBtCerrarSesion= Button(nuevoSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: framesManager(menuPrincipal))
nuevoSaldoBtCerrarSesion.place(x=100,y=450)

#Funcion transferencia
def loadTransferMessage(amount,cardInfoList,cardInfoTList):
    withdrawalCount=c.getWithdrawalCount(cardInfoList)
    if amount < 10000:
        retrieveErrorMessage(otroMontoErrorLb,"EL NUMERO NO ES VALIDO INTENTE DE NUEVO")
        #messagebox.showerror(message="Error: El numero no es valido intente de nuevo")
        ingresarMontoTransferenciaTx.delete("0","end")
    else:
        if c.accountIsBlocked(cardInfoList):
            messagebox.showerror(message="Error: Ya supero el maximo de retiros diarios, retornado al menu transacciones")
            ingresarMontoTransferenciaTx.delete("0","end")
            framesManager(menuTransaccion)
        else:
            if withdrawalCount==0:
                c.updateWithdrawalCount(cardInfoList)
                ingresarMontoTransferenciaTx.delete("0","end")
            else:
                if c.transfer(amount,cardInfoList,cardInfoTList):
                    messagebox.showinfo(message="¡Transaccion Exitosa! no olvide retirar su dinero")
                    c.updateWithdrawalCount(cardInfoList)
                    ingresarMontoTransferenciaTx.delete("0","end")
                    framesManager(menuTransaccion)
                else:
                    messagebox.showerror(message="Error: Saldo Insuficiente, retornado al menu transacciones")
                    ingresarMontoTransferenciaTx.delete("0","end")
                    framesManager(menuTransaccion)

#ingresarMontoTransaccion
ingresarMontoTransferenciaLabel= Label(ingresarMontoTransferencia, image=bgOtroMonto)
ingresarMontoTransferenciaLabel.place(x=0,y=0)

ingresarMontoTransferenciaTx= Entry(ingresarMontoTransferencia,width=10,font=("Helvetica",24),border=0)
ingresarMontoTransferenciaTx.config(validate='key',validatecommand=(ventana.register(validate_entryR), "%S", "%P"))
ingresarMontoTransferenciaTx.place(x=557,y=225)

#botones
ingresarMontoTransferenciaBtIngresar= Button(ingresarMontoTransferencia, padx=25,border=0, pady=15, bg="#7ed957", command= lambda: loadTransferMessage(float(ingresarMontoTransferenciaTx.get()),cardInfoList,cardInfoTList))
ingresarMontoTransferenciaBtIngresar.place(x=100,y=345)

ingresarMontoTransferenciaBtMenuT= Button(ingresarMontoTransferencia, padx=25,border=0, pady=15, bg="#e61717",command = lambda: clearText(menuTransaccion,ingresarMontoTransferenciaTx))
ingresarMontoTransferenciaBtMenuT.place(x=100,y=445)

if __name__=="__main__":
    ventana.mainloop()
