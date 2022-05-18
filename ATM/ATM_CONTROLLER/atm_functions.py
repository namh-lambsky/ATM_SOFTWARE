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
        else:
            print("Su numero ingresado no es correcto intente de nuevo")

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

    def getWithdrawalCount(self,cardInfoList):
        idAccount=int(cardInfoList[1])
        accounts=dao.getTableInfo(2)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            withdrawalCount=dao.getWithdrawalCount(idAccount)
            withdrawalCount=int(withdrawalCount[0])

        return withdrawalCount

    def getWithdrawalState(self,cardInfoList):
        idAccount=int(cardInfoList[1])
        accounts=dao.getTableInfo(2)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            withdrawalState=dao.getWithdrawalState(idAccount)
            withdrawalState=int(withdrawalState[0])

        return withdrawalState

    def accountIsBlocked(self,cardInfoList):
        idAccount=int(cardInfoList[1])
        accounts=dao.getTableInfo(2)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            state=self.getWithdrawalState(cardInfoList)
            if state==1:
                accountBlocked=True
            else:
                accountBlocked=False
        return accountBlocked

    def updateWithdrawalCount(self,cardInfoList):
        idAccount=int(cardInfoList[1])
        accounts=dao.getTableInfo(2)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            currentCount=self.getWithdrawalCount(cardInfoList)
            if currentCount==0:
                dao.updateWithdrawalState(idAccount,state=1)
            else:
                currentCount-=1
                dao.updateWithdrawalCount(idAccount,currentCount)



    def updatePassword(self,cardInfoList,newPassword):
        idAccount=int(cardInfoList[1])
        accounts=dao.getTableInfo(2)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            dao.updateAccountPassword(idAccount,newPassword)
            updateSuccess=True
        else:
            updateSuccess=False

        return updateSuccess



    def withdrawal(self,amount,cardInfoList):
        idAccount=int(cardInfoList[1])
        accounts=dao.getTableInfo(2)
        currentBalance=self.getAccountBalance(cardInfoList)
        for account in accounts:
            if account[0]==int(idAccount):
                codeExists=True
                break
        if codeExists:
            if currentBalance>amount:
                newBalance=currentBalance-amount
                dao.updateAccountBalance(idAccount,newBalance)
                withdrawalSuccess=True
            else:
                withdrawalSuccess=False
        return withdrawalSuccess


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
