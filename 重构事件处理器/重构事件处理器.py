import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


'''
在PyQt5中，事件处理器经常被重写（也就是用自己的覆盖库自带的）。
```
这个例子中，我们替换了事件处理器函数`keyPressEvent()`。

```
def keyPressEvent(self, e):
    
    if e.key() == Qt.Key_Escape:
        self.close()
```
此时如果按下ESC键程序就会退出。

程序展示：

这个就一个框，啥也没，就不展示了。
'''