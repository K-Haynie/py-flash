# Form implementation generated from reading ui file 'flashcards_modified_again.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 575)
        MainWindow.setMinimumSize(QtCore.QSize(675, 575))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.top = QtWidgets.QHBoxLayout()
        self.top.setObjectName("top")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.top.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(138, 17, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.top.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.top)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.Alignment.AlignLeading|QtCore.Qt.Alignment.AlignLeft|QtCore.Qt.Alignment.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 517, 496))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.bottom = QtWidgets.QHBoxLayout()
        self.bottom.setObjectName("bottom")
        self.verticalLayout_6.addLayout(self.bottom)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_6.addWidget(self.toolButton)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_6.addWidget(self.toolButton_2)
        self.verticalLayout.addWidget(self.groupBox_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(90, 0))
        self.comboBox.setCurrentText("")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_10.addWidget(self.comboBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_10.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.buttonAdd = QtWidgets.QPushButton(self.groupBox)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout_7.addWidget(self.buttonAdd)
        self.buttonRem = QtWidgets.QPushButton(self.groupBox)
        self.buttonRem.setObjectName("buttonRem")
        self.verticalLayout_7.addWidget(self.buttonRem)
        self.buttonDel = QtWidgets.QPushButton(self.groupBox)
        self.buttonDel.setObjectName("buttonDel")
        self.verticalLayout_7.addWidget(self.buttonDel)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.selectAll = QtWidgets.QPushButton(self.groupBox_8)
        self.selectAll.setObjectName("selectAll")
        self.verticalLayout_13.addWidget(self.selectAll)
        self.DeleteSelection = QtWidgets.QPushButton(self.groupBox_8)
        self.DeleteSelection.setObjectName("DeleteSelection")
        self.verticalLayout_13.addWidget(self.DeleteSelection)
        self.verticalLayout.addWidget(self.groupBox_8)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.timedPractice = QtWidgets.QCheckBox(self.groupBox_2)
        self.timedPractice.setObjectName("timedPractice")
        self.verticalLayout_8.addWidget(self.timedPractice)
        self.revPractice = QtWidgets.QCheckBox(self.groupBox_2)
        self.revPractice.setObjectName("revPractice")
        self.verticalLayout_8.addWidget(self.revPractice)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.numRight = QtWidgets.QLabel(self.tab_2)
        self.numRight.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.numRight.setObjectName("numRight")
        self.horizontalLayout_5.addWidget(self.numRight)
        self.numWrong = QtWidgets.QLabel(self.tab_2)
        self.numWrong.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.numWrong.setObjectName("numWrong")
        self.horizontalLayout_5.addWidget(self.numWrong)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.timerDisplay = QtWidgets.QLCDNumber(self.tab_2)
        self.timerDisplay.setObjectName("timerDisplay")
        self.horizontalLayout_5.addWidget(self.timerDisplay)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 267))
        self.stackedWidget.setMaximumSize(QtCore.QSize(200, 267))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.stackedWidget.addWidget(self.page3)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        self.discardPile = QtWidgets.QStackedWidget(self.tab_2)
        self.discardPile.setMinimumSize(QtCore.QSize(200, 267))
        self.discardPile.setMaximumSize(QtCore.QSize(200, 267))
        self.discardPile.setObjectName("discardPile")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.discardPile.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.discardPile.addWidget(self.page_3)
        self.horizontalLayout_7.addWidget(self.discardPile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit, 0, QtCore.Qt.Alignment.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.practiceCancelBtn = QtWidgets.QPushButton(self.tab_2)
        self.practiceCancelBtn.setObjectName("practiceCancelBtn")
        self.horizontalLayout_2.addWidget(self.practiceCancelBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 546, 501))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.tableView.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_5.addWidget(self.tableView)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.inputName = QtWidgets.QLineEdit(self.tab_3)
        self.inputName.setObjectName("inputName")
        self.horizontalLayout.addWidget(self.inputName)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.importButton = QtWidgets.QPushButton(self.groupBox_4)
        self.importButton.setObjectName("importButton")
        self.verticalLayout_9.addWidget(self.importButton)
        self.editButton = QtWidgets.QPushButton(self.groupBox_4)
        self.editButton.setObjectName("editButton")
        self.verticalLayout_9.addWidget(self.editButton)
        self.deckDelBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.deckDelBtn.setObjectName("deckDelBtn")
        self.verticalLayout_9.addWidget(self.deckDelBtn)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.addButton = QtWidgets.QPushButton(self.groupBox_5)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_11.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(self.groupBox_5)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_11.addWidget(self.removeButton)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_12.addWidget(self.pushButton_2)
        self.createButton = QtWidgets.QPushButton(self.groupBox_6)
        self.createButton.setObjectName("createButton")
        self.verticalLayout_12.addWidget(self.createButton)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flashcard Whiz"))
        self.label.setText(_translate("MainWindow", "Select the decks you want to practice:"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Settings"))
        self.toolButton.setText(_translate("MainWindow", "Info"))
        self.toolButton_2.setText(_translate("MainWindow", "Settings"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Collections"))
        self.pushButton_3.setText(_translate("MainWindow", "Create Collection"))
        self.groupBox.setTitle(_translate("MainWindow", "Edit Collection"))
        self.buttonAdd.setText(_translate("MainWindow", " Add Deck"))
        self.buttonRem.setText(_translate("MainWindow", " Remove Deck"))
        self.buttonDel.setText(_translate("MainWindow", " Delete Collection"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Selection"))
        self.selectAll.setText(_translate("MainWindow", "Select All"))
        self.DeleteSelection.setText(_translate("MainWindow", "Select to Delete"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Practice Options"))
        self.timedPractice.setText(_translate("MainWindow", "Timed Practice"))
        self.revPractice.setText(_translate("MainWindow", "Reverse Practice"))
        self.pushButton.setText(_translate("MainWindow", "Go!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Options"))
        self.numRight.setText(_translate("MainWindow", "Right: "))
        self.numWrong.setText(_translate("MainWindow", "Wrong:"))
        self.practiceCancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Practice"))
        self.label_2.setText(_translate("MainWindow", "Deck Name:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Decks"))
        self.importButton.setText(_translate("MainWindow", "Import Deck"))
        self.editButton.setText(_translate("MainWindow", "Edit Deck"))
        self.deckDelBtn.setText(_translate("MainWindow", "Delete Deck"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Cards"))
        self.addButton.setText(_translate("MainWindow", "Add Card"))
        self.removeButton.setText(_translate("MainWindow", "Delete Card"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Create"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.createButton.setText(_translate("MainWindow", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Create"))
