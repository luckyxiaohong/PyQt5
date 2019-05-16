from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


'''
`QCheckBox`组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景。

```
这个例子中，有一个能切换窗口标题的单选框。

```
cb = QCheckBox('Show title', self)
```
这个是`QCheckBox`的构造器。

```
cb.toggle()
```
要设置窗口标题，我们就要检查单选框的状态。默认情况下，窗口没有标题，单选框未选中。

```
cb.stateChanged.connect(self.changeTitle)
```
把`changeTitle()`方法和`stateChanged`信号关联起来。这样，`changeTitle()`就能切换窗口标题了。

```
def changeTitle(self, state):
    
    if state == Qt.Checked:
        self.setWindowTitle('QCheckBox')
    else:
        self.setWindowTitle('')
```
控件的状态是由`changeTitle()`方法控制的，如果空间被选中，我们就给窗口添加一个标题，如果没被选中，就清空标题。
'''