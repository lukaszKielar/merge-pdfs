from pathlib import Path
from typing import Dict, List

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QListWidget, QListWidgetItem


class PDFListWidget(QListWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setObjectName(u"listViewWidget")
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.ContiguousSelection)

        self._addedFiles: Dict[str, Path] = {}

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        # check drop action
        dropAction = event.dropAction()

        # if action is MoveAction use parent behavior
        # it basically means we want to change order of existing items
        if dropAction == Qt.MoveAction:
            super().dropEvent(event)

        # if action is CopyAction we are dropping local files to QListWidget
        elif dropAction == Qt.CopyAction:
            mimeData = event.mimeData()
            if mimeData.hasUrls:
                event.accept()

                newFiles = []

                for url in mimeData.urls():
                    if url.isLocalFile():
                        # convert url to Path
                        _newFilePath = Path(url.toLocalFile())
                        # check if path is present in already existed files
                        if _newFilePath.name not in self._addedFiles:
                            self._addedFiles[_newFilePath.name] = _newFilePath
                            newFiles.append(_newFilePath.name)

                self.addItems(newFiles)
            else:
                event.ignore()

        # otherwise ignore action
        else:
            event.ignore()

    def _removeItem(self, item: QListWidgetItem):
        itemText = item.text()
        # not really needed, because we took it from the QWidgetList,
        # but who cares (we want to be safe as almighty Java people)
        if itemText in self._addedFiles:
            del self._addedFiles[itemText]
            self.takeItem(self.row(item))

    def removeItems(self):
        selectedItems = self.selectedItems()
        for item in selectedItems:
            self._removeItem(item)
