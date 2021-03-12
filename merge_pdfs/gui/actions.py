from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QAction, QApplication, QStyle


def getActionAdd(window: QWindow) -> QAction:
    icon = QApplication.style().standardIcon(QStyle.SP_DialogOpenButton)
    addAction = QAction(icon, "Add", window)
    addAction.setShortcut("Ctrl+A")
    return addAction


def getActionRemove(window: QWindow) -> QAction:
    icon = QApplication.style().standardIcon(QStyle.SP_DialogCancelButton)
    removeAction = QAction(icon, "Remove", window)
    removeAction.setShortcut("Del")
    return removeAction


def getActionSave(window: QWindow) -> QAction:
    icon = QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)
    saveAction = QAction(icon, "Save", window)
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
