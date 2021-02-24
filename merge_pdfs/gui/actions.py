from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QAction


class ActionDarkMode(QAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.objectName = u"actionDarkMode"
        self.isCheckable = True
        self.isChecked = False
        self.shortcut = "Ctrl+D"


def getAddAction(window: QWindow) -> QAction:
    addAction = QAction("Add", window)
    addAction.setShortcut("Ctrl+A")
    return addAction


def getRemoveAction(window: QWindow) -> QAction:
    removeAction = QAction("Remove", window)
    removeAction.setShortcut("Del")
    return removeAction


def getSaveAction(window: QWindow) -> QAction:
    saveAction = QAction("Save", window)
    saveAction.setShortcut("Ctrl+S")
    return saveAction


def getLightModeAction(window: QWindow) -> QAction:
    lightModeAction = QAction("Light", window)
    lightModeAction.setShortcut("Ctrl+L")
    lightModeAction.setCheckable(True)
    lightModeAction.setChecked(True)
    return lightModeAction


def getDarkModeAction(window: QWindow) -> QAction:
    darkModeAction = QAction("Dark", window)
    darkModeAction.setShortcut("Ctrl+L")
    darkModeAction.setCheckable(True)
    darkModeAction.setChecked(False)
    return darkModeAction