# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableUi.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 326)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 318))
        # 通过设置水平方向的滚动条和设置大小，消除了最后一行遮挡的情况
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.addaction = QtWidgets.QAction(MainWindow)
        self.addaction.setObjectName("addaction")
        self.deleteaction = QtWidgets.QAction(MainWindow)
        self.deleteaction.setObjectName("deleteaction")
        self.additemaction = QtWidgets.QAction(MainWindow)
        self.additemaction.setObjectName("additemaction")
        self.updateitemaction = QtWidgets.QAction(MainWindow)
        self.updateitemaction.setObjectName("updateitemaction")
        self.deleteitemaction = QtWidgets.QAction(MainWindow)
        self.deleteitemaction.setObjectName("deleteitemaction")
        self.savetodbaction = QtWidgets.QAction(MainWindow)
        self.savetodbaction.setObjectName("savetodbaction")
        self.importfromexcelaction = QtWidgets.QAction(MainWindow)
        self.importfromexcelaction.setObjectName("importfromexcelaction")
        self.exporttoexcelaction = QtWidgets.QAction(MainWindow)
        self.exporttoexcelaction.setObjectName("exporttoexcelaction")
        self.helpaction = QtWidgets.QAction(MainWindow)
        self.helpaction.setObjectName("helpaction")
        self.declareaction = QtWidgets.QAction(MainWindow)
        self.declareaction.setObjectName("declareaction")
        self.qtaction = QtWidgets.QAction(MainWindow)
        self.qtaction.setObjectName("qtaction")
        self.menu.addAction(self.addaction)
        self.menu.addAction(self.deleteaction)
        self.menu_2.addAction(self.additemaction)
        self.menu_2.addAction(self.updateitemaction)
        self.menu_2.addAction(self.deleteitemaction)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.savetodbaction)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.exporttoexcelaction)
        self.menu_3.addAction(self.helpaction)
        self.menu_3.addAction(self.declareaction)
        self.menu_3.addAction(self.qtaction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Table的操作"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "内容"))
        self.menu_3.setTitle(_translate("MainWindow", "说明"))
        self.addaction.setText(_translate("MainWindow", "添加行"))
        self.deleteaction.setText(_translate("MainWindow", "删除行"))
        self.additemaction.setText(_translate("MainWindow", "添加一行"))
        self.updateitemaction.setText(_translate("MainWindow", "修改一行"))
        self.deleteitemaction.setText(_translate("MainWindow", "删除一行"))
        self.savetodbaction.setText(_translate("MainWindow", "保存到数据库"))
        self.importfromexcelaction.setText(_translate("MainWindow", "从excel导入"))
        self.exporttoexcelaction.setText(_translate("MainWindow", "导出到excel"))
        self.helpaction.setText(_translate("MainWindow", "帮助"))
        self.declareaction.setText(_translate("MainWindow", "说明"))
        self.qtaction.setText(_translate("MainWindow", "关于Qt"))

