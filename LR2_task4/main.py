from msilib.schema import ComboBox
from typing import Type
from unittest import result
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from PyQt5 import QtCore
import sys
from combinatoric import Combinatoric
from probablity import Probability

class mywindow(QtWidgets.QMainWindow):

    '''Конструктор главного окна'''
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Устанавливаем изображение формулы
        self.ui.setupUi(self)
        pixmap = QPixmap("img/img.jpg")
        self.ui.formulaLabel.setPixmap(pixmap)

        # Устанавливаем коннекты
        self.ui.neededHypotises.currentCellChanged.connect(self.setCell_n_table)
        self.ui.probability.currentCellChanged.connect(self.setCell_k_table)
        self.ui.spinBox.editingFinished.connect(self.enter)
        self.ui.solveButton.clicked.connect(self.solve)



    '''Изменить текущую строку таблицы k элементов, при изменении строки n элементов'''
    def setCell_k_table(self):
        curCell = self.ui.neededHypotises.currentRow()
        self.ui.probability.setCurrentCell(curCell, 0)


    '''Установить m строк в таблицы'''
    def setTableRowCount(self):
        m = self.ui.spinBox.value()
        rowAmount = self.ui.neededHypotises.rowCount()
        if m < rowAmount:
            for i in range(rowAmount - 1, m - 1, -1):
                self.ui.neededHypotises.setCurrentCell(i, 0)
                self.removeRow()
        elif m > rowAmount:
            for i in range(rowAmount - 1, m - 1, 1):
                self.addRow()


    '''Изменить текущую строку таблицы n элементов, при изменении строки k элементов'''
    def setCell_n_table(self):
        curCell = self.ui.neededHypotises.currentRow()
        self.ui.probability.setCurrentCell(curCell, 0)


    '''Добавить по одной строке в таблицы'''
    def addRow(self):
        lastRow = self.ui.neededHypotises.rowCount()
        self.ui.probability.insertRow(lastRow)
        self.ui.probability.setItem(lastRow, 0, QtWidgets.QTableWidgetItem("1"))
        self.ui.neededHypotises.insertRow(lastRow)
        self.ui.neededHypotises.setItem(lastRow, 0, QtWidgets.QTableWidgetItem("0"))
        self.ui.neededHypotises.item(lastRow, 0).setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.updateHeaders()
        self.ui.spinBox.setValue(self.ui.neededHypotises.rowCount())

        


    '''Удалить по одной строке из таблиц'''
    def removeRow(self):
        curRow = self.ui.neededHypotises.currentRow()
        if self.ui.neededHypotises.rowCount() > 1:
            self.ui.neededHypotises.removeRow(curRow)
            self.ui.probability.removeRow(curRow)
            self.updateHeaders()
            self.ui.spinBox.setValue(self.ui.neededHypotises.rowCount())


    '''Обновить заголовки строк в таблицах'''
    def updateHeaders(self):
        for i in range(self.ui.neededHypotises.rowCount()):
            item = QtWidgets.QTableWidgetItem("H_" + str(i + 1))
            self.ui.neededHypotises.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem("P(A)_" + str(i + 1))
            self.ui.probability.setVerticalHeaderItem(i, item)


    '''Установить m строк в таблицы'''
    def enter(self):
        m = self.ui.spinBox.value()
        rowAmount = self.ui.neededHypotises.rowCount()
        if m < rowAmount:
            for i in range(rowAmount - 1, m - 1, -1):
                self.ui.neededHypotises.setCurrentCell(i, 0)
                self.removeRow()
        elif m > rowAmount:
            for i in range(rowAmount - 1, m - 1, 1):
                self.addRow()


    '''Проверить корректность введенных данных'''
    def isInputCorrect(self, k, n, m):
        if n > k:
            QtWidgets.QMessageBox.information(self, "Ошибка", "n не может быть больше k")
            return False
        elif m > k:
            QtWidgets.QMessageBox.information(self, "Ошибка", "m не может быть больше k")
            return False
        
        k_sum = 0
        n_sum = 0
        for i in range(m):
            k_value = self.ui.neededHypotises(i, 0).text()
            n_value = self.ui.probability.item(i, 0).text()
            
            if not k_value.isnumeric():
                QtWidgets.QMessageBox.information(self, "Ошибка", "недопустимое значение H_" + str(i + 1) + " = " + k_value)
                return False
            elif not n_value.isnumeric():
                QtWidgets.QMessageBox.information(self, "Ошибка", "недопустимое значение P(A)_" + str(i + 1) + " = " + n_value)
                return False
            elif int(n_value) > int(k_value):
                QtWidgets.QMessageBox.information(self, "Ошибка", "P(A)_" + str(i + 1) + " не может быть больше H_" + str(i + 1))
                return False
            
            k_sum += int(k_value)
            n_sum += int(n_value)
        
        if k_sum != k:
            QtWidgets.QMessageBox.information(self, "Ошибка", "сумма k_i должна равняться k")
            return False
        elif n_sum != n:
            QtWidgets.QMessageBox.information(self, "Ошибка", "сумма n_i должна равняться n")
            return False
        return True


    '''Вычислить результирующее значение'''
    def solve(self):
        k = self.ui.spinBox.value()

        hypotisesNumber = self.ui.spinBox.value()

        #if (self.ui.comboBox.currentIndex() == 0):

        # Проверить введенные данные
        #if not self.isInputCorrect(k, n, m):
         #   return
        hypotisesList = []
        probabilityList = []
        # В числителе произведение всех сочетаний n_i по k_i
        for i in range(0, k):
            hypotisesList.append(float(self.ui.neededHypotises.item(i, 0).text()))
            probabilityList.append(float(self.ui.probability.item(i, 0).text()))
                

        
        # Полученный числитель разделить на число сочетаний n по k
        if (self.ui.comboBox.currentIndex() == 0) :
            result = Probability.fullProbability(hypotisesList, probabilityList)
            str_result = "{:01.12f}".format(result)
            self.ui.textEdit.setText("P(A) = " + str_result)
        elif (self.ui.comboBox.currentIndex() == 1) :
            strResult = ""
            for i in range(0, k):
                if self.ui.neededHypotises.item(i, 0).checkState() == QtCore.Qt.CheckState.Checked:
                    tmp = round(Probability.bayesFormula(i, hypotisesList, probabilityList), 8)
                    strResult = strResult + "P_A_(H_" + str(i + 1) + ") = " + str(tmp) + "\n"
            self.ui.textEdit.setText(strResult)
             

        # Вывести результат в поле ответа
        



# Запуск главного окна 
if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())