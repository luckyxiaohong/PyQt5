import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


'''
关闭一个窗口最直观的方式就是点击标题栏的那个叉，这个例子里，我们展示的是如何用程序关闭一个窗口。这里我们将接触到一点single和slots的知识。

本例使用的是QPushButton组件类。

```
QPushButton(string text, QWidget parent = None)
```
`text`参数是想要显示的按钮名称，`parent`参数是放在按钮上的组件，在我们的 例子里，这个参数是`QWidget`。应用中的组件都是一层一层（继承而来的？）的，在这个层里，大部分的组件都有自己的父级，没有父级的组件，是顶级的窗口。

```
这里创建了一个点击之后就退出窗口的按钮。

```
from PyQt5.QtCore import QCoreApplication
```
程序需要`QtCore`对象。

```
qbtn = QPushButton('Quit', self)
```
创建一个继承自`QPushButton`的按钮。第一个参数是按钮的文本，第二个参数是按钮的父级组件，这个例子中，父级组件就是我们创建的继承自`Qwidget`的`Example`类。

```
qbtn.clicked.connect(QCoreApplication.instance().quit)
```
事件传递系统在PyQt5内建的single和slot机制里面。
点击按钮之后，信号会被捕捉并给出既定的反应。
`QCoreApplication`包含了事件的主循环，它能添加和删除所有的事件，`instance()`创建了一个它的实例。
`QCoreApplication`是在`QApplication`里创建的。 
点击事件和能终止进程并退出应用的quit函数绑定在了一起。
在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
'''