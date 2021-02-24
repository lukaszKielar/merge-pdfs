from PyQt5.QtWidgets import QAction


class ActionAdd(QAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.objectName = u"actionAdd"
        self.shortcut = "Ctlr+A"


class ActionRemove(QAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.objectName = u"actionRemove"
        self.shortcut = "Del"


class ActionSave(QAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.objectName = u"actionSave"
        self.shortcut = "Ctrl+S"


class ActionLightMode(QAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.objectName = u"actionLightMode"
        self.isCheckable = True
        self.isChecked = True
        self.shortcut = "Ctrl+L"


class ActionDarkMode(QAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.objectName = u"actionDarkMode"
        self.isCheckable = True
        self.isChecked = False
        self.shortcut = "Ctrl+D"
