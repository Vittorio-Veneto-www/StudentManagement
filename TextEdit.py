from PyQt5 import QtCore, QtWidgets

class TextEdit(QtWidgets.QTextEdit):
    """
    A TextEdit editor that sends editingFinished events 
    when the text was changed and focus is lost.
    """

    editingFinished = QtCore.pyqtSignal()
    receivedFocus = QtCore.pyqtSignal()
    
    def __init__(self, tr='', parent=None):
        super(TextEdit, self).__init__(parent)
        self._changed = False
        self.setTabChangesFocus( True )
        self.setText(tr)
        self.textChanged.connect(self._handle_text_changed)

    def focusInEvent(self, event):
        super(TextEdit, self).focusInEvent( event )
        self.receivedFocus.emit()

    def focusOutEvent(self, event):
        if self._changed:
            self.editingFinished.emit()
        super(TextEdit, self).focusOutEvent( event )

    def _handle_text_changed(self):
        self._changed = True

    def setTextChanged(self, state=True):
        self._changed = state