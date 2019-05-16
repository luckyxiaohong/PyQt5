import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

'''
下面是一个能勾选菜单的例子
```

本例创建了一个行为菜单。这个行为／动作能切换状态栏显示或者隐藏。

```
viewStatAct = QAction('View statusbar', self, checkable=True)
```
用`checkable`选项创建一个能选中的菜单。

```
viewStatAct.setChecked(True)
```
默认设置为选中状态。

```
def toggleMenu(self, state):
    
    if state:
        self.statusbar.show()
    else:
        self.statusbar.hide()
```
依据选中状态切换状态栏的显示与否。
'''