import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(240, 320)
        MainWindow.setMinimumSize(QSize(240, 320))
        MainWindow.setMaximumSize(QSize(240, 320))
        MainWindow.setWindowTitle(u"MergePDFs")
        MainWindow.setAutoFillBackground(True)

        # actions
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName(u"actionRemove")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionLight.setCheckable(True)
        self.actionLight.setChecked(True)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionDark.setCheckable(True)
        self.actionDark.setChecked(False)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 2, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 240, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuMode = QMenu(self.menuSettings)
        self.menuMode.setObjectName(u"menuMode")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionRemove)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionAdd)
        self.menuFile.addAction(self.actionRemove)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuSettings.addAction(self.menuMode.menuAction())
        self.menuMode.addAction(self.actionLight)
        self.menuMode.addAction(self.actionDark)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionRemove.setText(
            QCoreApplication.translate("MainWindow", u"Remove", None)
        )
        self.actionLight.setText(
            QCoreApplication.translate("MainWindow", u"Light", None)
        )
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"Item 1", None)
        )
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"Item 2", None)
        )
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(
            QCoreApplication.translate("MainWindow", u"Settings", None)
        )
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"toolBar", None)
        )
        pass

    # retranslateUi


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    main_window = Ui_MainWindow()
    main_window.setupUi(window)

    window.show()
    sys.exit(app.exec())
