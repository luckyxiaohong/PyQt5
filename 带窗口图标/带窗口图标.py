import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 250, 800, 500)

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


'''
窗口图标通常是显示在窗口的左上角，标题栏的最左边。下面的例子就是怎么用PyQt5创建一个这样的窗口。

```
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        ...
```

面向对象编程最重要的三个部分是类(class)、数据和方法。我们创建了一个类的调用，这个类继承自`QWidget`。这就意味着，我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。`super()`构造器方法返回父级的对象。`__init__()`方法是构造器的一个方法。

```
self.initUI() 
```

使用`initUI()`方法创建一个GUI。

```
# 自己准备一个web.png
self.setGeometry(300, 300, 300, 220)
self.setWindowTitle('Icon')
self.setWindowIcon(QIcon('web.png'))  
```

上面的三个方法都继承自`QWidget`类。`setGeometry()`有两个作用：把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是`resize()`和`move()`的合体。最后一个方法是添加了图标。先创建一个QIcon对象，然后接受一个路径作为参数显示图标。


```
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

应用和示例的对象创立，主循环开始。
'''