# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\demon\Desktop\terver_lab2_task4_v1\LR2_task4\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.formulaLabel = QtWidgets.QLabel(self.centralwidget)
        self.formulaLabel.setText("")
        self.formulaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.formulaLabel.setObjectName("formulaLabel")
        self.verticalLayout.addWidget(self.formulaLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.neededHypotises = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.neededHypotises.setFont(font)
        self.neededHypotises.setObjectName("neededHypotises")
        self.neededHypotises.setColumnCount(1)
        self.neededHypotises.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.neededHypotises.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.neededHypotises, 0, 0, 1, 2)
        self.probability = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.probability.setFont(font)
        self.probability.setObjectName("probability")
        self.probability.setColumnCount(1)
        self.probability.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.probability.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.probability, 0, 2, 1, 1)
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numberLabel.setFont(font)
        self.numberLabel.setObjectName("numberLabel")
        self.gridLayout.addWidget(self.numberLabel, 1, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName("resultLabel")
        self.gridLayout.addWidget(self.resultLabel, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solveButton.setFont(font)
        self.solveButton.setObjectName("solveButton")
        self.verticalLayout.addWidget(self.solveButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Full Prabability & Bayes Formula"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Формула полной верятности"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Формула Бейеса"))
        item = self.neededHypotises.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hypotises"))
        item = self.probability.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Probabilities"))
        self.numberLabel.setText(_translate("MainWindow", "Количество гипотез"))
        self.resultLabel.setText(_translate("MainWindow", "Результат"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.solveButton.setText(_translate("MainWindow", "Решить"))
