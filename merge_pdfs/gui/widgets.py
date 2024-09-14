from __future__ import annotations

import logging
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFileDialog,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
)

from merge_pdfs.app_data import APP_DATA
from merge_pdfs.pdf_writer import PDFWriter

logger = logging.getLogger(__name__)


class PDFListWidget(QListWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setObjectName("listViewWidget")
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(
            QAbstractItemView.SelectionMode.ExtendedSelection
        )

        # dict that maps item label with its paths
        self._addedFiles: dict[str, Path] = {}

    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        logger.debug("DragEnterEvent %s", e)
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        # check drop action
        dropAction = event.dropAction()

        # if action is MoveAction use parent behavior
        # it basically means we want to change order of existing items
        if dropAction == Qt.DropAction.MoveAction:
            super().dropEvent(event)

        # if action is CopyAction we are dropping local files to QListWidget
        elif dropAction == Qt.DropAction.CopyAction:
            mimeData = event.mimeData()
            if mimeData.hasUrls():
                event.accept()

                for url in mimeData.urls():
                    if url.isLocalFile():
                        self._addItem(url.toLocalFile())

            else:
                event.ignore()

        # otherwise ignore action
        else:
            event.ignore()

    def _removeItem(self, item: QListWidgetItem) -> None:
        itemText = item.text()
        logger.debug("Removing [%s] item from the list", itemText)
        if itemText in self._addedFiles:
            del self._addedFiles[itemText]
            self.takeItem(self.row(item))

    def removeSelectedItems(self) -> None:
        selectedItems = self.selectedItems()
        logger.debug("Removing [%d] files from the list", len(selectedItems))
        for item in selectedItems:
            self._removeItem(item)

    # TODO: add pop up asking if the user is sure
    def removeAllItems(self) -> None:
        logger.debug("Removing all [%d] files from the list", self.count())

        # remove all items
        while self.count():
            item = self.takeItem(0)
            self._removeItem(item)

        # reset _addedFiles dict
        self._addedFiles = {}

    def _addItem(self, item: str) -> None:
        itemPath = Path(item)
        itemText = itemPath.name

        if itemText not in self._addedFiles:
            logger.debug("Adding [%s] file to the list", itemText)
            self._addedFiles[itemText] = itemPath
            self.addItem(itemText)

    def addItemsFromDialog(self) -> None:
        dir = APP_DATA.getSetting(setting="last_dir")
        if not dir:
            dir = str(Path.home())

        selectedFiles, _ = QFileDialog.getOpenFileNames(
            self,
            caption="Add file(s)",
            dir=dir,
            filter="PDF Files (*.pdf);;Images (*.png *.jpg *.jpeg)",
            options=QFileDialog.Option.DontUseNativeDialog,
        )

        if selectedFiles:
            # save lastOpenedDir in settings file
            APP_DATA.updateSetting(
                setting="last_dir",
                value=str(Path(selectedFiles[0]).parent),
            )

            for _file in selectedFiles:
                self._addItem(_file)

    def saveFile(self) -> None:
        # ignore if no files were added
        if not self._addedFiles:
            logger.warning("Nothing to be saved")
            return

        dir = APP_DATA.getSetting(setting="last_dir")
        if not dir:
            dir = str(Path.home())

        newFile, _ = QFileDialog.getSaveFileName(
            self,
            caption="Save file",
            dir=dir,
            filter="PDF files (*.pdf)",
            options=QFileDialog.Option.DontUseNativeDialog,
        )

        # skip if file name was not specified or cancel button was pressed
        if not newFile:
            return

        # make sure files will be saved in correct order
        # save as they appear in the UI
        orderedKeys = [self.item(item).text() for item in range(self.count())]
        orteredValues = [self._addedFiles[key] for key in orderedKeys]

        PDFWriter().write(path=Path(newFile), files=orteredValues)

        QMessageBox.information(
            self,
            "MergePDFs",
            f"File {newFile} was successfully saved",
        )
