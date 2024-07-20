from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
aap = QApplication([]) #Створюємо обєкт додаток
main_wind = QWidget()
main_wind.resize(400,200)
main_wind.move(200,200)

btn1 = QPushButton('Згенерувати') #Створюємо кнопку
text = QLabel('Переможець')

line = QVBoxLayout()
line.addWidget(btn1, alignment= Qt.AlignCenter)
line.addWidget(text, alignment= Qt.AlignCenter,)

main_wind.setLayout(line)


main_wind.show()
aap.exec_()