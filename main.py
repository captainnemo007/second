import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.initUi()

    def initUi(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ell(qp)
            qp.end()

    def draw_ell(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(5):
            w = randint(20, 150)
            coord_x = randint(w,800-w)
            coord_y = randint(w,600-w)
            qp.drawEllipse(coord_x, coord_y,
                           w, w)
    def paint(self):
        self.do_paint = True
        self.repaint()

    def run(self):
        self.paint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
