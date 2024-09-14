from __future__ import annotations

import logging
from enum import Enum

import qdarkstyle
from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import (QMainWindow, QMenu, QMenuBar, QToolBar,
                               QVBoxLayout, QWidget)

from merge_pdfs.app_data import APP_DATA
from merge_pdfs.gui.actions import (getActionAdd, getActionDarkMode,
                                    getActionLightMode, getActionRemove,
                                    getActionRemoveAll, getActionSave)
from merge_pdfs.gui.widgets import PDFListWidget

logger = logging.getLogger(__name__)


class AppMode(str, Enum):
    LIGHT = "light"
    DARK = "dark"


class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._lightStyleSheet = self.styleSheet()
        self._darkStyleSheet = qdarkstyle.load_stylesheet_pyside6()

        self._pdfListWidget = PDFListWidget()

        # order matters!!
        self._defineWindow()
        self._defineLayout()
        self._define_actions()
        self._defineMenuBar()
        self._defineToolBar()

    def _defineWindow(self) -> None:
        self.setObjectName("MainWindow")
        self.setWindowTitle("MergePDFs")
        self.resize(640, 320)
        self.setMinimumSize(QSize(640, 320))
        self.setMaximumSize(QSize(640, 320))
        self.setAutoFillBackground(True)

    def _defineLayout(self) -> None:
        # setup layout
        layout = QVBoxLayout()
        layout.addWidget(self._pdfListWidget)

        # create central widget
        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        # set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(centralWidget)

    def _define_actions(self) -> None:
        self.actionAdd = getActionAdd(self)
        self.actionAdd.triggered.connect(
            self._pdfListWidget.addItemsFromDialog
        )

        self.actionRemove = getActionRemove(self)
        self.actionRemove.triggered.connect(
            self._pdfListWidget.removeSelectedItems
        )

        self.actionRemoveAll = getActionRemoveAll(self)
        self.actionRemoveAll.triggered.connect(
            self._pdfListWidget.removeAllItems
        )

        self.actionSave = getActionSave(self)
        self.actionSave.triggered.connect(self._pdfListWidget.saveFile)

        self.actionLightMode = getActionLightMode(self)
        self.actionLightMode.triggered.connect(
            lambda: self._setMode(AppMode.LIGHT)
        )

        self.actionDarkMode = getActionDarkMode(self)
        self.actionDarkMode.triggered.connect(
            lambda: self._setMode(AppMode.DARK)
        )

        # read mode from APP_DATA
        mode = APP_DATA.getSetting(setting="mode")
        if not mode or mode == "light":
            self._setMode(mode=AppMode.LIGHT)
        else:
            self._setMode(mode=AppMode.DARK)

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

    def _setMode(self, mode: AppMode) -> None:
        logger.debug("Setting %s mode", mode)
        if mode.value == "dark":
            self.setStyleSheet(self._darkStyleSheet)
            self.actionLightMode.setChecked(False)
            self.actionDarkMode.setChecked(True)
        else:
            self.setStyleSheet(self._lightStyleSheet)
            self.actionLightMode.setChecked(True)
            self.actionDarkMode.setChecked(False)

        APP_DATA.updateSetting("mode", mode.value)
