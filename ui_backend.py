from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import TextEdit

class ui_backend():
    def __init__(self, core):
        self.core = core
        self.setup()

    def setup(self):
        import sys
        app = QApplication(sys.argv)
        import Ui_gui
        class gui(QWidget):
            def closeEvent(self, event):
                if self.contentChanged:
                    x = QWidget()
                    reply = QMessageBox.information(x,'提示','是否保存', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
                    if reply == QMessageBox.Ok:
                        self.core.saveFile()
                super().closeEvent(event)
        MainWindow = gui()
        MainWindow.core = self.core
        self.ui = Ui_gui.Ui_Form()
        self.ui.setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.type = 0
        self.MainWindow.contentChanged = False
        self.resetTable()
        MainWindow.show()

        def infoQuery():
            self.type, self.dataList = 0, self.core.query(self.ui.infoEdit.toPlainText(), 0)
            self.drawTable()

        def scoreQuery():
            self.type, self.dataList = 1, self.core.query(self.ui.scoreEdit.toPlainText(), 1)
            self.drawTable()
        
        def saveFile():
            self.core.saveFile()
            self.MainWindow.contentChanged = False

        self.ui.infoQuery.clicked.connect(infoQuery)
        self.ui.scoreQuery.clicked.connect(scoreQuery)
        self.ui.save.clicked.connect(saveFile)

        sys.exit(app.exec_())
    
    def resetTable(self):
        self.dataList = self.core.query('', self.type)
        self.drawTable()
    
    def drawTable(self):
        self.ui.resultCount.setText("共找到%d条结果" % len(self.dataList))

        class tableModel(QAbstractTableModel):
            def __init__(self, ui, parent=None):
                super(tableModel, self).__init__(parent)
                self.ui = ui
                self.dataList, self.type, self.core = self.ui.dataList, self.ui.type, self.ui.core
                self.headers, self.properties = self.core.getHeaders(self.ui.type)
                self.headers += ['操作']
                self.data = ['' for _ in range(len(self.properties))]

            def rowCount(self, QModelIndex):
                return len(self.dataList) + 1

            def columnCount(self, QModelIndex):
                return len(self.properties) + 1

            def data(self, index, role):
                return QVariant()
    
            def headerData(self,section,orientation,role=Qt.DisplayRole):
                if role != Qt.DisplayRole:
                    return QVariant()
                elif orientation == Qt.Horizontal:
                    return self.headers[section]
                else:
                    return "%d" % (section + 1)

            def edit(self, index, data):
                tmp = {self.properties[index.column()]: data}
                self.core.changeValueByIndex(self.dataList[index.row()]['index'], tmp, self.type)
                self.ui.MainWindow.contentChanged = True

            def append(self):
                tmp = {}
                for i in range(len(self.properties)):
                    tmp[self.properties[i]] = self.data[i]
                self.core.append(tmp, self.type)
                self.ui.MainWindow.contentChanged = True
                self.ui.resetTable()

            def delete(self, index):
                self.core.delete(self.dataList[index]['index'], self.type)
                self.ui.resetTable()

        class tableContent(QItemDelegate):
            def __init__(self, model, parent = None):
                super(tableContent, self).__init__(parent)
                self.model = model

            def paint(self, painter, option, index):
                if not self.parent().indexWidget(index):
                    if index.column() == self.model.columnCount(None) - 1:
                        if index.row() < self.model.rowCount(None) - 1:
                            button = QPushButton(
                                self.tr('删除'),
                                self.parent(),
                                clicked=lambda: self.model.delete(button.index[0])
                            )
                            button.index = [index.row(), index.column()]
                            h_box_layout = QHBoxLayout()
                            h_box_layout.addWidget(button)
                            h_box_layout.setContentsMargins(0, 0, 0, 0)
                            h_box_layout.setAlignment(Qt.AlignCenter)
                            widget = QWidget()
                            widget.setLayout(h_box_layout)
                            self.parent().setIndexWidget(
                                index,
                                widget
                            )
                        else:
                            button = QPushButton(
                                self.tr('添加'),
                                self.parent(),
                                clicked=lambda: self.model.append()
                            )
                            button.index = [index.row(), index.column()]
                            h_box_layout = QHBoxLayout()
                            h_box_layout.addWidget(button)
                            h_box_layout.setContentsMargins(0, 0, 0, 0)
                            h_box_layout.setAlignment(Qt.AlignCenter)
                            widget = QWidget()
                            widget.setLayout(h_box_layout)
                            self.parent().setIndexWidget(
                                index,
                                widget
                            )
                    else:
                        if index.row() < self.model.rowCount(None) - 1:
                            textEdit = TextEdit.TextEdit(
                                self.model.dataList[index.row()][self.model.properties[index.column()]],
                                self.parent()
                            )
                            textEdit.editingFinished.connect(lambda: self.model.edit(index, textEdit.toPlainText()))
                            h_box_layout = QHBoxLayout()
                            h_box_layout.addWidget(textEdit)
                            h_box_layout.setContentsMargins(0, 0, 0, 0)
                            h_box_layout.setAlignment(Qt.AlignCenter)
                            widget = QWidget()
                            widget.setLayout(h_box_layout)
                            self.parent().setIndexWidget(
                                index,
                                widget
                            )
                        else:
                            textEdit = TextEdit.TextEdit(
                                parent=self.parent()
                            )
                            def func(x, y, z):
                                x[y] = z
                            textEdit.editingFinished.connect(lambda: func(self.model.data, index.column(), textEdit.toPlainText()))
                            h_box_layout = QHBoxLayout()
                            h_box_layout.addWidget(textEdit)
                            h_box_layout.setContentsMargins(0, 0, 0, 0)
                            h_box_layout.setAlignment(Qt.AlignCenter)
                            widget = QWidget()
                            widget.setLayout(h_box_layout)
                            self.parent().setIndexWidget(
                                index,
                                widget
                            )
        
        model = tableModel(self, self.ui.tableView)
        self.ui.tableView.setModel(model)
        self.ui.tableView.setItemDelegate(tableContent(model, self.ui.tableView))
        if self.type == 0:
            self.ui.tableView.setColumnWidth(3, 250)
            self.ui.tableView.setColumnWidth(4, 250)
        self.ui.tableView.show()