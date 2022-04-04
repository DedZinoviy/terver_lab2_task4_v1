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
        pixmap = QPixmap("img/0.png")
        self.ui.formulaLabel.setPixmap(pixmap)

        # Устанавливаем коннекты
        self.ui.neededHypotises.currentCellChanged.connect(self.setCell_n_table)
        self.ui.probability.currentCellChanged.connect(self.setCell_k_table)
        self.ui.spinBox.editingFinished.connect(self.setTableRowCount)
        self.ui.solveButton.clicked.connect(self.solve)
        self.ui.comboBox.currentIndexChanged.connect(self.changeFormulaImg)


    def changeFormulaImg(self):
        solveType = self.ui.comboBox.currentIndex()
        self.ui.formulaLabel.setPixmap(QPixmap("img/" + str(solveType) + ".png"))
        

    '''Изменить текущую строку таблицы k элементов, при изменении строки n элементов'''
    def setCell_k_table(self):
        curCell = self.ui.probability.currentRow()
        self.ui.neededHypotises.setCurrentCell(curCell, 0)


    '''Изменить текущую строку таблицы n элементов, при изменении строки k элементов'''
    def setCell_n_table(self):
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


    '''Вычислить результирующее значение'''
    def solve(self):
        k = self.ui.spinBox.value()
        hypotiseSum = 0
        hypotisesList = []
        probabilityList = []

        try:
            for i in range(0, k):
                hypotise = float(self.ui.neededHypotises.item(i, 0).text())
                probability = float(self.ui.probability.item(i, 0).text())
                if hypotise < 0 or hypotise > 1 or probability < 0 or probability > 1:
                    QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректное значение вероятности в строке " + str(i + 1)
                    + "\nЗначение вероятности должно лежать в интервале [0; 1]")
                    return
                else:
                    hypotisesList.append(hypotise)
                    probabilityList.append(probability)
                    hypotiseSum += hypotise
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректный формат ввода в строке " + str(i + 1)
            + "\nВероятность задается десятичной дробью, целая часть от дробной должна отделяться точкой \".\"")
            return
             
        if round(hypotiseSum, 12) != 1:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Сумма вероятностей гипотез должна равняться 1")
            return
        
        # Полученный числитель разделить на число сочетаний n по k
        if (self.ui.comboBox.currentIndex() == 0) :
            result = Probability.fullProbability(hypotisesList, probabilityList)
            str_result = "{:01.12f}".format(result)
            self.ui.textEdit.setText("P(A) = " + str_result)
        elif (self.ui.comboBox.currentIndex() == 1) :
            strResult = ""
            for i in range(0, k):
                if self.ui.neededHypotises.item(i, 0).checkState() == QtCore.Qt.CheckState.Checked:
                    tmp = "{:01.12f}".format(Probability.bayesFormula(i, hypotisesList, probabilityList), 12)
                    strResult = strResult + "P_A_(H_" + str(i + 1) + ") = " + tmp + "\n"
            if strResult == "":
                QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Не выбрана ни одна гипотеза\nОтметьте галочкой в таблице гипотезы для которых проиводить вычисления")
                return
            self.ui.textEdit.setText(strResult)
        



# Запуск главного окна 
if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())