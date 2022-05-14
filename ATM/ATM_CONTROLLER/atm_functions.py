from tkinter import *
import os
import sys
from tkinter import messagebox
import cv2
import time
from pyzbar.pyzbar import decode
script_dir = os.path.dirname( __file__ )
connector_dir = os.path.join( script_dir,'..','..', 'DB_CONNECTOR')
sys.path.append( connector_dir )
from db_connector import DAO

dao=DAO()
class controller():

    def validateR(self,entry,text):
        if int(text) < 2700000 and int(text) %5==0:
            amount=int(text)
            entry.delete("0","end")
            self.withdrawal(amount,)
        else:
            print("Su numero ingresado no es correcto intente de nuevo")

    def getCardList(self):
        cardInfo=self.getCardInfo()
        return cardInfo

    def getCardInfo(self):
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
        cv2.destroyAllWindows()
        return cardInfoList

    def getAccountBalance(self,idAccount):
        accounts=dao.getTableInfo(2)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            currentBalance=dao.getAccountBalance(idAccount)
        else:
            currentBalance=None
        return currentBalance

    def passwordValidation(self,cardInfoList,passwordGUI):
        userCanEnter=False
        accountId=int(cardInfoList[1])
        cards=dao.getTableInfo(3)
        for card in cards:
            if card[1]==accountId:
                codeExists=True
                break
        if passEntryTries==3:
            if codeExists:
                passwordScheme=dao.getAccountPassword(accountId)
                passwordScheme=int(passwordScheme[0])
                if passwordScheme==int(passwordGUI):
                    passEntryTries=0
                    userCanEnter=True
                else:
                    messagebox.showerror(message="contraseña errada")
                    passEntryTries+=1
        else:
            messagebox.showerror(message="Tarjeta Bloqueada")
            userCanEnter=False
        return userCanEnter

    def entryPasswordValidation(self,entry,framesList,frametoShow):
        try:
            passwordEntry=entry.get()
            passwordIsCorrect=True
            print(passwordEntry)
            pass
            if passwordIsCorrect:
                self.framesManager(framesList,frametoShow)
                entry.delete("0","end")
        except Exception as e:
            print ("error: "+str(e))

    def clearTextInput(self,entry,framesList,frametoShow):
        entry.delete("0","end")
        self.framesManager(framesList,frametoShow)