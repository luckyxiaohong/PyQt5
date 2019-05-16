# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we display the x and y
coordinates of a mouse pointer in a label widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
'''  
事件对象是用python来描述一系列的事件自身属性的对象。

```
这个示例中，我们在一个组件里显示鼠标的X和Y坐标。

```
self.text = "x: {0},  y: {1}".format(x, y)

self.label = QLabel(self.text, self)
```
X
Y坐标显示在
`QLabel`
组件里

```
self.setMouseTracking(True)
```
事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件。

```


def mouseMoveEvent(self, e):
    x = e.x()
    y = e.y()

    text = "x: {0},  y: {1}".format(x, y)
    self.label.setText(text)


```
`e`
代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。`x()`
和
`y()`
方法得到鼠标的x和y坐标点，然后拼成字符串输出到
`QLabel`
组件里。
'''