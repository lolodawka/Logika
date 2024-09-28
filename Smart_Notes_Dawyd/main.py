from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

#Выкно програми
app = QApplication([])
window = QWidget()
window.setWindowTitle('Smart Notes')
window.resize(800,600)
window.move(0,0)
window.setStyleSheet('backgroun-color : rgb(152,152,152); font-size: 15px')


text_editor = QTextEdit()
text_editor.setPlaceholderText('Введыть текст замыток.....')

list_widget_1 = QListWidget()
list_widget_2 = QListWidget()

text_searcher = QLineEdit()                                #Пошук ро тексту
text_searcher.setPlaceholderText('Введіть текст......')

text_searcher = QLineEdit()                                 #Пошук по тегу
text_searcher.setPlaceholderText('Введіть тег....')

#Кнопки
make_note = QPushButton()
make_note.setText('Створити замітку')

delete_note = QPushButton()
delete_note.setText('Видалити замітку замітку')

save_note = QPushButton()
save_note.setText('Зберегти замітку')

search_for_text = QPushButton()
search_for_text.setText('Шукати за текстом')

search_for_tag = QPushButton()
search_for_tag.setText('Шукати за тегом')

add_to_note = QPushButton()
add_to_note.setText('Додати тег до заміток')

unpin_to_note = QPushButton()
unpin_to_note.setText('Відкріпити тег від замітки')

convert_to_note = QPushButton()
convert_to_note.setText('Конвертувати до txt формату')

action_theme_btn = QPushButton()
action_theme_btn.setText('Змінити тему')

#Макет

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

cold1 = QVBoxLayout()
cold1.addWidget(text_editor)

cold2 = QVBoxLayout()
cold2.addWidget(QLabel('Список заміток:'))
cold2.addWidget(list_widget_1)
cold2.addLayout(row1)
cold2.addWidget(save_note)
cold2.addWidget(QLabel('Список тегів:'))
cold2.addWidget(search_for_text)
#Нижні з кнопок
cold2.addWidget(search_for_tag)
cold2.addWidget(add_to_note)
cold2.addWidget(unpin_to_note)
cold2.addWidget(convert_to_note)
cold2.addWidget(action_theme_btn)
#Злиття
layout_not = QHBoxLayout()
layout_not.addLayout(cold1)
layout_not.addLayout(cold2)
#Макет на екран
window.setLayout(layout_not)


window.show()
app.exec_()