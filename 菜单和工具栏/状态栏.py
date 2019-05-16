import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


'''
状态栏是用来显示应用的状态信息的组件。

```
状态栏是由QMainWindow创建的。

```
self.statusBar().showMessage('Ready')
```
调用`QtGui.QMainWindow`类的`statusBar()`方法，创建状态栏。第一次调用创建一个状态栏，返回一个状态栏对象。`showMessage()`方法在状态栏上显示一条信息。
'''