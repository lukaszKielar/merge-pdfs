import logging
from pathlib import Path
from typing import Dict

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QFileDialog,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
)

from merge_pdfs.backend.app_data import APP_DATA
from merge_pdfs.backend.pdf_writer import PDFWriter

logger = logging.getLogger(__name__)


class PDFListWidget(QListWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setObjectName("listViewWidget")
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # dict that maps item label with its paths
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

                for url in mimeData.urls():
                    if url.isLocalFile():
                        self._addItem(url.toLocalFile())

            else:
                event.ignore()

        # otherwise ignore action
        else:
            event.ignore()

    def _removeItem(self, item: QListWidgetItem):
        itemText = item.text()
        logger.debug("Removing '%s' from the list", itemText)
        # not really needed, because we took it from the QWidgetList,
        # but who cares (we want to be safe as almighty Java people)
        if itemText in self._addedFiles:
            del self._addedFiles[itemText]
            self.takeItem(self.row(item))

    def removeSelectedItems(self):
        selectedItems = self.selectedItems()
        logger.debug("Files to be removed from the list: %d", len(selectedItems))
        for item in selectedItems:
            self._removeItem(item)

    # TODO it should present a pop up asking if user is sure
    def removeAllItems(self):
        allItems = self.count()
        logger.debug("All files to be removed from the list: %d", allItems)

        # remove all items
        while self.count():
            item = self.takeItem(0)
            self._removeItem(item)

        # reset _addedFiles dict
        self._addedFiles = {}

    def _addItem(self, item: str):
        itemPath = Path(item)
        itemText = itemPath.name

        if itemText not in self._addedFiles:
            logger.debug("Adding '%s' to the list", itemText)
            self._addedFiles[itemText] = itemPath
            self.addItem(itemText)
        else:
            logger.warning("Ignoring '%s', already on the list", itemText)

    def addItemsFromDialog(self):
        openDir = str(APP_DATA.getLastDir())

        selectedFiles, _ = QFileDialog.getOpenFileNames(
            self,
            "Add file(s)",
            openDir,
            "PDF files (*.pdf *.PDF *.Pdf)",
            options=QFileDialog.DontUseNativeDialog,
        )

        if selectedFiles:
            # save lastOpenedDir in settings file
            APP_DATA.save_setting("lastDir", str(Path(selectedFiles[0]).parent))

            for _file in selectedFiles:
                self._addItem(_file)

    def saveFile(self):
        # ignore if no files were added
        if not self._addedFiles:
            logger.debug("Ignoring save action due to empty list")
            return

        openDir = str(APP_DATA.getLastDir())
        newFile, _ = QFileDialog.getSaveFileName(
            self,
            "Save file",
            openDir,
            "PDF files (*.pdf *.PDF *.Pdf)",
            options=QFileDialog.DontUseNativeDialog,
        )

        # skip if file name was not specified or cancel button was pressed
        if not newFile:
            return

        pdfWriter = PDFWriter()
        pdfWriter.merge_files(*self._addedFiles.values())
        pdfWriter.save(newFile)

        QMessageBox.information(
            self, "MergePDFs", f"File {newFile} was successfully saved", QMessageBox.Ok
        )
