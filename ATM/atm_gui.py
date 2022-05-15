import os
import sys
import tkinter as tk
from tkinter import messagebox
import cv2
import time
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, 'ATM_CONTROLLER')
sys.path.append( controller_dir )
from atm_functions import controller


current_accountId=0
current_balance=0.00
cardInfo=[]
c=controller()

#Clase que contendrá los diferentes menus del software
class SampleApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.shared_data={
            'accountId':tk.IntVar(),
            'balance':tk.IntVar()
            }
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        #Iniciar paginas dentro del container
        for F in (MenuInicioSesion,MenuIngresoTarjeta,MenuTransacciones,PaginaRetiros):
            page_name=F.__name__
            frame=F(parent=container, controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame("MenuInicioSesion")

    def show_frame(self,page_name):
        #Funcion que muestra un frame dado el nombre del mismo
        frame=self.frames[page_name]
        frame.tkraise()

#Creacion de los frames
#MenuInicioSesion
class MenuInicioSesion(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#090909')
        self.controller=controller
        self.controller.title('Cajero Automatico Bancolombia')
        self.controller.state('zoomed')
        self.controller.iconbitmap('ATM/IMAGES/LogoBancolombia.ico')

        #abrir la imagen para el fondo de pantalla
        bg_image= Image.open("ATM/IMAGES/Pantallaprincipal.png")
        resized_image=bg_image.resize((1920,1080))
        bg_image= ImageTk.PhotoImage(resized_image)

        #label para el fondo
        background_label_inicio_sesion=tk.Label(self,image=bg_image)
        background_label_inicio_sesion.image=bg_image
        background_label_inicio_sesion.place(x=0,y=0)

        def go_to_MenuIngresoTarjeta():
            controller.show_frame('MenuIngresoTarjeta')

        def go_to_MenuIngresoSinTarjeta():
            controller.show_frame('MenuIngresoSinTarjeta')

        bt_ingreso_tarjeta=tk.Button(self , padx=25,border=0, pady=15, bg="#DD5222", command=go_to_MenuIngresoTarjeta)
        bt_ingreso_sin_tarjeta=tk.Button(self , padx=25,border=0, pady=15, bg="#DD5222", command=go_to_MenuIngresoSinTarjeta)

        bt_ingreso_tarjeta.place(x=15,y=435)
        bt_ingreso_sin_tarjeta.place(x=1175,y=435)

class MenuIngresoTarjeta(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#090909')
        self.controller=controller
        self.controller.title('Cajero Automatico Bancolombia')


        bg_image_ingreso_tarjeta= Image.open("ATM/IMAGES/IngresoTarjetaContraseña.png")
        resized_image_ingreso_tarjeta=bg_image_ingreso_tarjeta.resize((1920,1080))
        bg_image_ingreso_tarjeta= ImageTk.PhotoImage(resized_image_ingreso_tarjeta)

        contraseñaIcon= Image.open("ATM/IMAGES/EntryShape.png")
        resizeImageC=contraseñaIcon.resize((300,50))
        contraseñaIcon=ImageTk.PhotoImage(resizeImageC)

        #label para el fondo
        background_label_ingreso_tarjeta=tk.Label(self,image=bg_image_ingreso_tarjeta)
        background_label_ingreso_tarjeta.image=bg_image_ingreso_tarjeta
        background_label_ingreso_tarjeta.place(x=0,y=0)

        label_shape_ingreso_tarjeta=tk.Label(self,image=contraseñaIcon)
        label_shape_ingreso_tarjeta.image=contraseñaIcon
        label_shape_ingreso_tarjeta.place(x=510,y=200)

        #Comando para la validación del entry(que sean 4 digitos y que sean numeros)
        def validate_entry(text, new_text):
        # Primero chequear que el contenido total no exceda los diez caracteres.
            if len(new_text) > 10:
                return False
        # Luego, si la validación anterior no falló, chequear que el texto solo
        # contenga números.
            return text.isdecimal()

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
            return cardInfoList

        def login(cardInfoList,ingresoTarjetaContraseñaTx):
                if c.passwordValidation(cardInfoList,ingresoTarjetaContraseñaTx.get()):
                    go_to_MenuTransacciones()

        def go_to_MenuTransacciones():
            controller.show_frame('MenuTransacciones')

        def go_to_MenuInicioSesion():
            controller.show_frame('MenuInicioSesion')

        global cardInfo
        cardInfo=getCardInfo()
        if cardInfo!=None:
            controller.shared_data['accountId'].set(cardInfo[1])
            controller.shared_data['balance'].set(float(c.getAccountBalance(controller.shared_data['accountId'].get())))

        entry_ingreso_tarjeta= tk.Entry(self,show="*",width=6,font=("Helvetica",24),border=0)
        entry_ingreso_tarjeta.place(x=630,y=204)
        entry_ingreso_tarjeta.focus_set()
        entry_ingreso_tarjeta.config(validate='key',validatecommand=(controller.register(validate_entry), "%S", "%P"))

        bt_ingresar_contraseña=tk.Button(self,padx=25,border=0, pady=15, bg="#7ed957", command=lambda:login(cardInfo,entry_ingreso_tarjeta))
        bt_menuInicioSesion=tk.Button(self,padx=25,border=0, pady=15, bg="#7ed957", command=go_to_MenuInicioSesion)

        bt_ingresar_contraseña.place(x=100,y=345)
        bt_menuInicioSesion.place(x=100,y=445)


class MenuTransacciones(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#090909')
        self.controller=controller
        self.controller.title('Cajero Automatico Bancolombia')
        #abrir la imagen para el fondo de pantalla
        bg_image_Menu_Transacciones= Image.open("ATM/IMAGES/MenuTransaccion.png")
        resized_image=bg_image_Menu_Transacciones.resize((1920,1080))
        bg_image_Menu_Transacciones= ImageTk.PhotoImage(resized_image)

        #label para el fondo
        background_label_menu_transacciones=tk.Label(self,image=bg_image_Menu_Transacciones)
        background_label_menu_transacciones.image=bg_image_Menu_Transacciones
        background_label_menu_transacciones.place(x=0,y=0)

        #botones MenuTransaccion
        bt_retirar_dinero=tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_retirar_dinero.place(x=25,y=147)
        bt_consultar_saldo=tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_consultar_saldo.place(x=25,y=282)
        bt_transferencias=tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_transferencias.place(x=1170,y=147)
        bt_finalizar=tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_finalizar.place(x=25,y=417)

class PaginaRetiros(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#090909')
        self.controller=controller
        self.controller.title('Cajero Automatico Bancolombia')


        bg_image_Pagina_Retiros= Image.open("ATM/IMAGES/RetirarDinero.png")
        resized_image=bg_image_Pagina_Retiros.resize((1920,1080))
        bg_image_Pagina_Retiros= ImageTk.PhotoImage(resized_image)

        background_label_Pagina_Retiros=tk.Label(self, image=bg_image_Pagina_Retiros)
        background_label_Pagina_Retiros.image=bg_image_Pagina_Retiros
        background_label_Pagina_Retiros.place(x=0,y=0)

        bt_Pagina_Retiros_10000= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_Pagina_Retiros_10000.place(x=25,y=10)

        bt_Pagina_Retiros_20000= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_Pagina_Retiros_20000.place(x=25,y=145)

        bt_Pagina_Retiros_50000= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_Pagina_Retiros_50000.place(x=25,y=280)

        bt_Pagina_Retiros_Finalizar= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_Pagina_Retiros_Finalizar.place(x=25,y=415)

        bt_Pagina_Retiros_150000= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_Pagina_Retiros_150000.place(x=1170,y=10)

        bt_Pagina_Retiros_250000= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_Pagina_Retiros_250000.place(x=1170,y=145)

        bt_Pagina_Retiros_350000= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        bt_Pagina_Retiros_350000.place(x=1170,y=280)

        menuTransaccionBtRetirarDineroOtroValor= tk.Button(self, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDineroOtroValor.place(x=1170,y=415)

class ConsultarSaldo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#090909')
        self.controller=controller
        self.controller.title('Cajero Automatico Bancolombia')
        self.controller.state('zoomed')
        self.controller.iconbitmap('ATM/IMAGES/LogoBancolombia.ico')
        #ConsultarSaldoFondo
        bg_image_consultar_saldo= Image.open("ATM/IMAGES/ConsultarSaldo.png")
        resizeImagef=bg_image_consultar_saldo.resize((1250,580))
        bg_image_consultar_saldo= ImageTk.PhotoImage(resizeImagef)
        #label
        background_label_consultar_saldo =tk.Label(self, image=bg_image_consultar_saldo)
        background_label_consultar_saldo.image=bg_image_consultar_saldo
        background_label_consultar_saldo.place(x=0,y=0)

        #botones
        bt_saldo_imprimir= tk.Button(self, padx=25,border=0, pady=15, bg="#DD5222")
        bt_saldo_imprimir.place(x=15,y=290)

        bt_saldo_ver= tk.Button(self, padx=25,border=0, pady=15, bg="#DD5222")
        bt_saldo_ver.place(x=1175,y=290)
        
def mainP():

    app=SampleApp()
    app.mainloop

mainP()