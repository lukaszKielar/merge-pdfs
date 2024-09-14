from __future__ import annotations

from PySide6.QtCore import QObject
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QStyle


def getActionAdd(qObject: QObject) -> QAction:
    icon = QApplication.style().standardIcon(
        QStyle.StandardPixmap.SP_DialogOpenButton
    )
    qAction = QAction(icon, "Add", qObject)
    qAction.setShortcut("Ctrl++")
    return qAction


def getActionRemove(qObject: QObject) -> QAction:
    icon = QApplication.style().standardIcon(
        QStyle.StandardPixmap.SP_DialogCancelButton
    )
    qAction = QAction(icon, "Remove", qObject)
    qAction.setShortcut("Del")
    return qAction


def getActionRemoveAll(qObject: QObject) -> QAction:
    icon = QApplication.style().standardIcon(
        QStyle.StandardPixmap.SP_DialogResetButton
    )
    qAction = QAction(icon, "Remove all", qObject)
    return qAction


def getActionSave(qObject: QObject) -> QAction:
    icon = QApplication.style().standardIcon(
        QStyle.StandardPixmap.SP_DialogSaveButton
    )
    qAction = QAction(icon, "Save", qObject)
    qAction.setShortcut("Ctrl+S")
    return qAction


def getActionLightMode(qObject: QObject) -> QAction:
    qAction = QAction("Light", qObject)
    qAction.setShortcut("Ctrl+L")
    qAction.setCheckable(True)
    qAction.setChecked(True)
    return qAction


def getActionDarkMode(qObject: QObject) -> QAction:
    qAction = QAction("Dark", qObject)
    qAction.setShortcut("Ctrl+D")
    qAction.setCheckable(True)
    qAction.setChecked(False)
    return qAction
