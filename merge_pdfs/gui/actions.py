from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QAction


class ActionDarkMode(QAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.objectName = u"actionDarkMode"
        self.isCheckable = True
        self.isChecked = False
        self.shortcut = "Ctrl+D"


def getActionAdd(window: QWindow) -> QAction:
    addAction = QAction("Add", window)
    addAction.setShortcut("Ctrl+A")
    return addAction


def getActionRemove(window: QWindow) -> QAction:
    removeAction = QAction("Remove", window)
    removeAction.setShortcut("Del")
    return removeAction


def getActionSave(window: QWindow) -> QAction:
    saveAction = QAction("Save", window)
    saveAction.setShortcut("Ctrl+S")
    return saveAction


def getActionLightMode(window: QWindow) -> QAction:
    lightModeAction = QAction("Light", window)
    lightModeAction.setShortcut("Ctrl+L")
    lightModeAction.setCheckable(True)
    lightModeAction.setChecked(True)
    return lightModeAction


def getActionDarkMode(window: QWindow) -> QAction:
    darkModeAction = QAction("Dark", window)
    darkModeAction.setShortcut("Ctrl+D")
    darkModeAction.setCheckable(True)
    darkModeAction.setChecked(False)
    return darkModeAction