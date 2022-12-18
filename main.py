from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
import json

app = QApplication([])

notes = {
    "Добро пожаловать!" : {
        "текст" : "Добро пожаловать в приложение для заметок",
        "теги" : ["добро", "инструкция"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file)


mainWidget = QWidget()
mainWidget.setWindowTitle('Notes')
mainWidget.resize(900,600)

listNotes = QListWidget()
listLabel = QLabel('Список заметок')

buttonCreateNote = QPushButton('Создать заметку')
buttonDeleteNote = QPushButton('Удалить заметку')
buttonSaveNote = QPushButton('Сохранить заметку')

fieldTeg = QLineEdit('')
fieldTeg.setPlaceholderText('Введите тег...')
fieldText = QTextEdit()
buttonAddToNote = QPushButton('Добавить к заметке')
buttonDeleteTeg = QPushButton('Открепить от заметки')
buttonFieldTeg = QPushButton('Искать заметки по тегу')

labelListTeg = QLabel('Список тегов')
listTag = QListWidget()

mainLayout = QHBoxLayout()

lay_1 = QVBoxLayout()
lay_1.addWidget(fieldText)

lay_2 = QVBoxLayout()
lay_2.addWidget(listLabel)
lay_2.addWidget(listNotes)

layB_1 = QHBoxLayout()
layB_2 = QHBoxLayout()
layB_1.addWidget(buttonCreateNote)
layB_1.addWidget(buttonDeleteNote)
layB_2.addWidget(buttonSaveNote)

lay_2.addLayout(layB_1)
lay_2.addLayout(layB_2)

lay_2.addWidget(labelListTeg)
lay_2.addWidget(listTag)
lay_2.addWidget(fieldTeg)

layB_3 = QHBoxLayout()
layB_4 = QHBoxLayout()

layB_3.addWidget(buttonAddToNote)
layB_3.addWidget(buttonDeleteTeg)

layB_4.addWidget(buttonFieldTeg)

lay_2.addLayout(layB_3)
lay_2.addLayout(layB_4)

mainLayout.addLayout(lay_1,stretch=2)
mainLayout.addLayout(lay_2,stretch=1)

mainWidget.setLayout(mainLayout)

def show_note():
    #получаем текст из заметки с выделенным названием и отображаем его в поле редактирования
    key = listNotes.selectedItems()[0].text()
    print(key)
    fieldText.setText(notes[key]["текст"])
    listTag.clear()
    listTag.addItems(notes[key]["теги"])

listNotes.itemClicked.connect(show_note)


mainWidget.show()
with open("notes_data.json", "r") as file:
    notes = json.load(file)
listNotes.addItems(notes)

app.exec_()





