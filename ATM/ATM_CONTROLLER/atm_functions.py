from tkinter import *
import os
import sys
from tkinter import messagebox
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

    def getAccountBalance(self,cardInfoList):
        idAccount=int(cardInfoList[1])
        accounts=dao.getTableInfo(2)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            currentBalance=dao.getAccountBalance(idAccount)
            currentBalance=float(currentBalance[0])
        else:
            currentBalance=0.0
        return currentBalance

    def getPasswordTries(self,cardInfoList):
        codeExists=False
        cardId=int(cardInfoList[0])
        cards=dao.getTableInfo(3)
        for card in cards:
            if card[0]==cardId:
                codeExists=True
                break
        if codeExists:
            passwordTries=dao.getPasswordTries(cardId)
            passwordTries=passwordTries[0]

        return passwordTries

    def getCardState(self,cardInfoList):
        codeExists=False
        cardId=int(cardInfoList[0])
        cards=dao.getTableInfo(3)
        for card in cards:
            if card[0]==cardId:
                codeExists=True
                break
        if codeExists:
            cardState=dao.getCardState(cardId)
        return cardState

    def updatePasswordTries(self,cardInfoList):
        codeExists=False
        cardId=int(cardInfoList[0])
        cards=dao.getTableInfo(3)
        for card in cards:
            if card[0]==cardId:
                codeExists=True
                break
        if codeExists:
            currentTries=self.getPasswordTries(cardInfoList)
            if currentTries==0:
                dao.updateCardState(cardId,state=1)
            else:
                currentTries-=1
                dao.updatePasswordTries(cardId,currentTries)

    def cardIsBlocked(self,cardInfoList):
        codeExists=False
        cardId=int(cardInfoList[0])
        cards=dao.getTableInfo(3)
        for card in cards:
            if card[0]==cardId:
                codeExists=True
                break
        if codeExists:
            state=self.getCardState(cardInfoList)
            state=int(state[0])
            if state==1:
                cardState=True
            else:
                cardState=False
        return cardState

    def passwordValidation(self,cardInfoList,passwordGUI):
        codeExists=False
        userCanEnter=False
        accountId=int(cardInfoList[1])
        cards=dao.getTableInfo(3)
        for card in cards:
            if card[1]==accountId:
                codeExists=True
                break
        if codeExists:
            passwordScheme=dao.getAccountPassword(accountId)
            passwordScheme=int(passwordScheme[0])
            if passwordScheme==int(passwordGUI):
                userCanEnter=True
            else:
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