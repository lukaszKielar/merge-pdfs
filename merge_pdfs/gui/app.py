import sys

import qdarkstyle
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMenuBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from merge_pdfs.backend.app_data import APP_DATA
from merge_pdfs.backend.logger import AppLogger
from merge_pdfs.gui.actions import (
    getActionAdd,
    getActionDarkMode,
    getActionLightMode,
    getActionRemove,
    getActionRemoveAll,
    getActionSave,
)
from merge_pdfs.gui.widgets import PDFListWidget

logger = AppLogger.default()


class Window(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._lightStyleSheet = self.styleSheet()
        self._darkStyleSheet = qdarkstyle.load_stylesheet_pyqt5()

        self._defineWindow()
        self._defineLayout()
        self._defineActions()
        self._defineMenuBar()
        self._defineToolBar()

    def _defineLayout(self) -> None:
        # setup layout
        layout = QVBoxLayout()

        # define listView widget
        self.listViewWidget = PDFListWidget()
        layout.addWidget(self.listViewWidget)

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
        fileMenu.addAction(self.actionRemoveAll)
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
        self.setObjectName("MainWindow")
        self.setWindowTitle("MergePDFs")
        self.resize(640, 320)
        self.setMinimumSize(QSize(640, 320))
        self.setMaximumSize(QSize(640, 320))
        self.setAutoFillBackground(True)

    def _defineActions(self) -> None:
        self.actionAdd = getActionAdd(self)
        self.actionAdd.triggered.connect(self.listViewWidget.addItemsFromDialog)

        self.actionRemove = getActionRemove(self)
        self.actionRemove.triggered.connect(self.listViewWidget.removeSelectedItems)

        self.actionRemoveAll = getActionRemoveAll(self)
        self.actionRemoveAll.triggered.connect(self.listViewWidget.removeAllItems)

        self.actionSave = getActionSave(self)
        self.actionSave.triggered.connect(self.listViewWidget.saveFile)

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
        logger.debug("Setting %s mode", mode)
        if mode == "dark":
            self.setStyleSheet(self._darkStyleSheet)
            self.actionLightMode.setChecked(False)
            self.actionDarkMode.setChecked(True)
        else:
            self.setStyleSheet(self._lightStyleSheet)
            self.actionLightMode.setChecked(True)
            self.actionDarkMode.setChecked(False)

        APP_DATA.save_setting("mode", mode)

    def _defineToolBar(self) -> None:
        toolBar = QToolBar(self)
        toolBar.setMovable(False)

        # add actions
        toolBar.addAction(self.actionAdd)
        toolBar.addAction(self.actionRemove)
        toolBar.addSeparator()
        toolBar.addAction(self.actionRemoveAll)
        toolBar.addSeparator()
        toolBar.addAction(self.actionSave)

        self.addToolBar(toolBar)


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = Window()
        window.show()
        sys.exit(app.exec())
    except Exception:
        # TODO print message box with exception and
        #  button that allows to copy the content of the message
        logger.exception("Application failed")
        sys.exit(1)
