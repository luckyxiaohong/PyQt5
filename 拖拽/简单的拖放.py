from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)
import sys


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()



'''
本例使用了`QLineEdit`和`QPushButton`。把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）。

```
class Button(QPushButton):
  
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
        self.setAcceptDrops(True)
```
为了完成预定目标，我们要重构一些方法。首先用`QPushButton`上构造一个按钮实例。

```
self.setAcceptDrops(True)
```
激活组件的拖拽事件。

```
def dragEnterEvent(self, e):
    
    if e.mimeData().hasFormat('text/plain'):
        e.accept()
    else:
        e.ignore() 
```
首先，我们重构了`dragEnterEvent()`方法。设定好接受拖拽的数据类型（plain text）。

```
def dropEvent(self, e):

    self.setText(e.mimeData().text()) 
```
然后重构`dropEvent()`方法，更改按钮接受鼠标的释放事件的默认行为。

```
edit = QLineEdit('', self)
edit.setDragEnabled(True)
```
`QLineEdit`默认支持拖拽操作，所以我们只要调用`setDragEnabled()`方法使用就行了。
'''