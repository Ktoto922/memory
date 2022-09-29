from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton,  QPushButton, QLabel)
from random import shuffle
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Какой город не существует', 'Коноха', 'Вашингтон', 'Москва', 'Алматы'))
 
app = QApplication([])
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!') 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)

ResultGroupBox = QGroupBox("Результат теста")
lb_Result1 = QLabel('прав ты или нет?') 
lb_Correct1 = QLabel('ответ будет тут!') 

layout_res1 = QVBoxLayout()
layout_res1.addWidget(lb_Result1)
layout_res1.addWidget(lb_Correct1)
ResultGroupBox.setLayout(layout_res1)
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question,)
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line2.addWidget(ResultGroupBox)
AnsGroupBox.hide() 
ResultGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ResultGroupBox.hide()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    ResultGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_test_result():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    ResultGroupBox.show()
    btn_OK.setText('Начать заново')
    lb_Result1.setText('Завершено')
    lb_Correct1.setText('Результат теста: ' + str(window.points) + ' из ' + str(window.questions))
    lb_Question.hide()
    window.points = 0
    window.questions = 0


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)  
    show_question()
 
def show_correct(res):
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    if answers[0].isChecked():
        window.points += 1
        window.questions += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            window.questions += 1
            show_correct('Неверно!')
 
def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        lb_Correct.setText('Вопросы закончились')
        btn_OK.setText('Завершить тест')
        window.cur_question = -1 
    else:
        lb_Question.show()
        q = questions_list[window.cur_question] 
        ask(q)
 
def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() 
    elif btn_OK.text() == 'Завершить тест':
        show_test_result()
    else:
        next_question()
 
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1    
window.points = 0 # 
window.questions = 0
btn_OK.clicked.connect(click_OK) 

next_question()
window.resize(400, 300)
window.show()
app.exec()