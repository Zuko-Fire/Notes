from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import json

app = QApplication([])

mainWidget = QWidget()
mainWidget.setWindowTitle('Умные заметки')
mainWidget.resize(900, 600)

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

mainLayout.addLayout(lay_1, stretch=2)
mainLayout.addLayout(lay_2, stretch=1)

mainWidget.setLayout(mainLayout)


def add_note():
    name, result = QInputDialog.getText(mainWidget, "Добавить заметку", "Название заметки:")
    if result and name != '':
        notes[name] = {"текст": "", "теги": []}
        listNotes.addItems(notes)
        listTag.addItems(notes[name]["теги"])
        with open("notes_data.json", "a") as file:
            json.dump(notes, file)


def save_note():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()
        notes[key]["текст"] = fieldText.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для сохранения не выбрана!")


def del_note():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()
        del notes[key]
        listNotes.clear()
        fieldText.clear()
        listNotes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для удаления не выбрана!")


def show_note():
    # получаем текст из заметки с выделенным названием и отображаем его в поле редактирования
    key = listNotes.selectedItems()[0].text()
    print(key)
    fieldText.setText(notes[key]["текст"])
    listTag.clear()
    listTag.addItems(notes[key]["теги"])


def add_tag():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()
        tag = fieldTeg.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            listTag.addItem(tag)
            fieldTeg.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для добавления тега не выбрана!")


def del_tag():
    if listTag.selectedItems():
        key = listNotes.selectedItems()[0].text()
        tag = listTag.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        listTag.clear()
        listTag.addItems(notes[key]["теги"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Тег для удаления не выбран!")


def search_tag():
    print(buttonFieldTeg.text())
    tag = fieldTeg.text()
    if buttonFieldTeg.text() == "Искать заметки по тегу" and tag:
        print(tag)
        notes_filtered = {}  # тут будут заметки с выделенным тегом
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note] = notes[note]
        button_tag_search.setText("Сбросить поиск")
        listNotes.clear()
        listTag.clear()
        listNotes.addItems(notes_filtered)
        print(buttonFieldTeg.text())
    elif buttonFieldTeg.text() == "Сбросить поиск":
        fieldTeg.clear()
        listNotes.clear()
        listTag.clear()
        listNotes.addItems(notes)
        buttonFieldTeg.setText("Искать заметки по тегу")
        print(buttonFieldTeg.text())
    else:
        pass


listNotes.itemClicked.connect(show_note)
buttonCreateNote.clicked.connect(add_note)
buttonDeleteNote.clicked.connect(del_note)
buttonSaveNote.clicked.connect(save_note)
buttonFieldTeg.clicked.connect(search_tag)
buttonAddToNote.clicked.connect(add_tag)
buttonDeleteTeg.clicked.connect(del_tag)
mainWidget.show()
with open("notes_data.json", "r") as file:
    notes = json.load(file)
listNotes.addItems(notes)

app.exec_()










