from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

def showe_win ():
    victory_win = QMessageBox()
    victory_win.setText('Правильно!')
    victory_win.exec_()


def showe_lose ():
    defeat_lose = QMessageBox()
    defeat_lose.setText('Не правильно!')
    defeat_lose.exec_()

#Підключеня модулів
app = QApplication([])
main_win = QWidget()
#Основне вікно
main_win.setWindowTitle('Конкурс від Crazy People')
main_win.resize(400,200)

qustion = QLabel("В якому році канал отримав золоту кнопку від YouTube?")
btn1 = QPushButton('2005')
btn2 = QPushButton('2010')
btn3 = QPushButton('2015')
btn4 = QPushButton('2020')

layoutH1 =QHBoxLayout()
layoutH2 =QHBoxLayout()
layoutH3 =QHBoxLayout()

main_layout = QVBoxLayout()

layoutH1.addWidget(qustion,alignment = Qt.AlignCenter)
layoutH2.addWidget(btn1,alignment = Qt.AlignCenter)
layoutH2.addWidget(btn2,alignment = Qt.AlignCenter)
layoutH3.addWidget(btn3,alignment = Qt.AlignCenter)
layoutH3.addWidget(btn4,alignment = Qt.AlignCenter)

main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)

main_win.setLayout(main_layout)

btn1.clicked.connect(showe_win)
btn2.clicked.connect(showe_lose)
btn3.clicked.connect(showe_lose)
btn4.clicked.connect(showe_lose)

main_win.show()
app.exec_()

