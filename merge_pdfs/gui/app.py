import sys

import qdarkstyle
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QGridLayout,
    QListWidget,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QWidget,
)

from merge_pdfs.backend.app_data import AppData

from .actions import (
    getActionAdd,
    getActionDarkMode,
    getActionLightMode,
    getActionRemove,
    getActionSave,
)


APP_DATA = AppData()


class Window(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._lightStyleSheet = self.styleSheet()
        self._darkStyleSheet = qdarkstyle.load_stylesheet_pyqt5()

        self._defineWindow()
        self._defineActions()
        self._defineMenuBar()
        self._defineLayout()

    def _defineLayout(self) -> None:
        # setup layout
        layout = QGridLayout()

        # define listView widget
        self.listViewWidget = QListWidget()
        self.listViewWidget.setObjectName(u"listViewWidget")
        self.listViewWidget.setDragEnabled(True)
        self.listViewWidget.setDragDropOverwriteMode(False)
        self.listViewWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listViewWidget.addItem("Item1")
        self.listViewWidget.addItem("Item2")

        # define save button
        self.buttonSave = QPushButton(text="Save")
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.pressed.connect(self.saveFiles)

        # define widgets
        widgets = [
            (self.listViewWidget, 1, 0, 1, 2, Qt.AlignHCenter),
            (self.buttonSave, 2, 1, 1, 1),
        ]

        # add all widgets to the layout
        for w in widgets:
            layout.addWidget(w[0], *w[1:])

        # create central widget
        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        # set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(centralWidget)

    def _defineMenuBar(self) -> None:
        menuBar = QMenuBar(self)
        menuBar.setGeometry(QRect(0, 0, 240, 21))

        # File menu
        fileMenu = QMenu("&File", self)
        fileMenu.addAction(self.actionAdd)
        fileMenu.addAction(self.actionRemove)
        fileMenu.addSeparator()
        fileMenu.addAction(self.actionSave)
        # add File menu to menu bar
        menuBar.addMenu(fileMenu)

        # Settings menu
        settingsMenu = QMenu("&Settings", self)
        modeMenu = QMenu("&Mode", self)
        modeMenu.addAction(self.actionLightMode)
        modeMenu.addAction(self.actionDarkMode)
        settingsMenu.addMenu(modeMenu)
        # add Settings menu to menu bar
        menuBar.addMenu(settingsMenu)

        # set menu bar for window
        self.setMenuBar(menuBar)

    def _defineWindow(self) -> None:
        self.setObjectName(u"MainWindow")
        self.setWindowTitle(u"MergePDFs")
        self.resize(240, 320)
        self.setMinimumSize(QSize(240, 320))
        self.setMaximumSize(QSize(240, 320))
        self.setAutoFillBackground(True)

    def _defineActions(self) -> None:
        self.actionAdd = getActionAdd(self)
        self.actionAdd.triggered.connect(self.addFile)

        self.actionRemove = getActionRemove(self)
        self.actionRemove.triggered.connect(self.removeFile)

        self.actionSave = getActionSave(self)
        self.actionSave.triggered.connect(self.saveFiles)

        self.actionLightMode = getActionLightMode(self)
        self.actionLightMode.triggered.connect(lambda: self.setMode("light"))

        self.actionDarkMode = getActionDarkMode(self)
        self.actionDarkMode.triggered.connect(lambda: self.setMode("dark"))

        # read mode from APP_DATA
        mode = APP_DATA.mode
        if not mode or mode == "light":
            self.setMode(mode="light")
        else:
            self.setMode(mode="dark")

    def setMode(self, mode: str) -> None:
        if mode == "dark":
            self.setStyleSheet(self._darkStyleSheet)
            self.actionLightMode.setChecked(False)
            self.actionDarkMode.setChecked(True)
        else:
            self.setStyleSheet(self._lightStyleSheet)
            self.actionLightMode.setChecked(True)
            self.actionDarkMode.setChecked(False)

        APP_DATA.save_setting("mode", mode)

    def saveFiles(self) -> None:
        print("Save is not implemented yet!")

    def removeFile(self) -> None:
        print("Remove is not implemented yet!")

    def addFile(self) -> None:
        print("Add is not implemented yet!")
        # self.listViewWidget.addItem(item)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
