#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QPushButton, QLabel, QDesktopWidget, QWidget, QMessageBox, QApplication, QComboBox


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel("Запуск невозможен", self)

        self.lbl.move(115, 55)

        self.resize(350, 140)
        self.center()
        self.setWindowTitle('Message box')
        self.show()

        self.setWindowTitle('Error')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
