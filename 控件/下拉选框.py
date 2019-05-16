from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


'''
`QComboBox`组件能让用户在多个选择项中选择一个。

```
本例包含了一个`QComboBox`和一个`QLabel`。下拉选择框有五个选项，都是Linux的发行版名称，标签内容为选定的发行版名称。

```
combo = QComboBox(self)
combo.addItem("Ubuntu")
combo.addItem("Mandriva")
combo.addItem("Fedora")
combo.addItem("Arch")
combo.addItem("Gentoo")
```
创建一个`QComboBox`组件和五个选项。

```
combo.activated[str].connect(self.onActivated) 
```
在选中的条目上调用`onActivated()`方法。

```
def onActivated(self, text):
  
    self.lbl.setText(text)
    self.lbl.adjustSize() 
```
在方法内部，设置标签内容为选定的字符串，然后设置自适应文本大小。
'''