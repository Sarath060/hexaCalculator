from UI import *
from hexConverter import *
import datetime
import os

baseIndex = ['B', '9', '9', 'H']
intBase = [2, 8, 10, 16]
baseByte = [[8, 16, 32, 64],  # binary
            [3, 6, 11, 22],  # Octal
            [3, 5, 10, 20],  # Decimal
            [2, 4, 8, 16]]  # Hexdecimal
byteIndex = [1, 2, 4, 8]


def copyoutput():
    try:
        rs = str(ui.Output.toPlainText())
        clipboard.setText(rs)
    except Exception as e:
        messagebox("Error", f"Oops!{e.__class__} Error occurred at Copying.")


def pasteinput():
    try:
        ui.Input.setText(_translate("MainWindow", clipboard.text()))
        convert()
    except Exception as e:
        messagebox("Error", f"Oops!{e.__class__} Error occurred at Pasteing.")


def qexit():
    sys.exit(0)


def messagebox(title, text):
    msgBox = QtWidgets.Qmessagebox()
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QtWidgets.Qmessagebox.Ok)
    returnValue = msgBox.exec()
    return returnValue


def qsave():
    try:
        downloadDir, filename = os.path.split(os.path.abspath(__file__))
        currentBaseText = ui.Base.currentText()
        inputText = ui.Input.text()
        file = str(downloadDir + "\\Result_" + currentBaseText + "_" + inputText +'.txt')
        filepath, result = QtWidgets.QInputDialog.getText(mainWindow , "Input Dialog",
                                                          "Enter File name with Path", QtWidgets.QLineEdit.Normal, file)
        if result:
            file1 = open(filepath, "w")
            file1.write(str(datetime.datetime.now()))
            rs = str(ui.Output.toPlainText())
            file1.writelines(rs)
            file1.close()
        else:
            messagebox("Info", "Incorrect Path")
            return
    except Exception as e:
        messagebox("Error", f"Oops!{e.__class__} Error occurred at Save.")


def inputmask():
    try:
        print("Base Change")
        currentBaseIndex = ui.Base.currentIndex()
        currentByteIndex = ui.Byte.currentIndex()
        inputLen = baseByte[currentBaseIndex][currentByteIndex]
        inputMask = baseIndex[currentBaseIndex] * inputLen
        ui.Input.setInputMask(_translate("MainWindow", inputMask))
        ui.Input.setText(_translate("MainWindow", ""))
        print(currentBaseIndex, currentByteIndex, ui.Input.inputMask())
    except Exception as e:
        messagebox("Error", f"Oops!{e.__class__} Error occurred at Input masking.")


def input2hex():
    try:
        inputText = ui.Input.text()
        base = intBase[ui.Base.currentIndex()]
        inputHex = format(int(inputText, base), 'x')
        print("input", inputHex)
        return inputHex
    except Exception as e:
        messagebox("Error", f"Oops!{e.__class__} Error occurred at Input to Hex Conversion.")


def convert():
    try:
        print("button clicked")
        inputHex = input2hex()
        currentBytes = byteIndex[ui.Byte.currentIndex()]
        rs = conversion(inputHex, currentBytes)
        rs = str('\n'.join(rs))
        # print(rs)
        ui.Output.setPlainText(_translate("MainWindow", rs))
    except Exception as e:
        messagebox("Error", f"Oops!{e.__class__} Error occurred at button Click.")


if __name__ == '__main__':
    import sys

    _translate = QtCore.QCoreApplication.translate
    inNum = ""
    app = QtWidgets.QApplication(sys.argv)
    clipboard = QtWidgets.QApplication.clipboard()
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    # inNum = ui.Input.text()
    # print(inNum)
    ui.Convert.clicked.connect(convert)
    ui.Base.currentTextChanged.connect(inputmask)
    ui.Byte.currentTextChanged.connect(inputmask)
    ui.actionCopy.triggered.connect(copyoutput)
    ui.actionPaste.triggered.connect(pasteinput)
    ui.actionExit.triggered.connect(qexit)
    ui.actionSave.triggered.connect(qsave)
    sys.exit(app.exec_())
