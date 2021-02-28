from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QListWidget


class PDFListWidget(QListWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setObjectName(u"listViewWidget")
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setAlternatingRowColors(True)

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

                files = []

                for url in mimeData.urls():
                    if url.isLocalFile():
                        files.append(str(url.toLocalFile()))

                self.addItems(files)
            else:
                event.ignore()

        # otherwise ignore action
        else:
            event.ignore()
