# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\vscode\Python\StudentManagement\gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 1000)
        self.infoQuery = QtWidgets.QPushButton(Form)
        self.infoQuery.setGeometry(QtCore.QRect(180, 20, 111, 51))
        self.infoQuery.setObjectName("infoQuery")
        self.scoreQuery = QtWidgets.QPushButton(Form)
        self.scoreQuery.setGeometry(QtCore.QRect(490, 20, 111, 51))
        self.scoreQuery.setObjectName("scoreQuery")
        self.infoEdit = QtWidgets.QTextEdit(Form)
        self.infoEdit.setGeometry(QtCore.QRect(10, 20, 151, 51))
        self.infoEdit.setObjectName("infoEdit")
        self.scoreEdit = QtWidgets.QTextEdit(Form)
        self.scoreEdit.setGeometry(QtCore.QRect(320, 20, 151, 51))
        self.scoreEdit.setObjectName("scoreEdit")
        self.resultCount = QtWidgets.QLabel(Form)
        self.resultCount.setGeometry(QtCore.QRect(10, 80, 591, 31))
        self.resultCount.setObjectName("resultCount")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 120, 1200, 880))
        self.tableView.setObjectName("tableView")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(720, 20, 111, 51))
        self.save.setObjectName("save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学生管理系统"))
        self.infoQuery.setText(_translate("Form", "查询学生"))
        self.scoreQuery.setText(_translate("Form", "查询成绩"))
        self.resultCount.setText(_translate("Form", "TextLabel"))
        self.save.setText(_translate("Form", "保存"))
