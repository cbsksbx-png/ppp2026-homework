import PySimpleGUI as sg
import random


def main():
    score = 0
    life = 3

    layout = [
        [sg.Text('구구단 게임') , sg.Button('START')],
        [sg.Text('', key='-QUESTION-', size=(20,1))],
        [sg.Input(key='-INPUT-', size=(10,1)), sg.Button('확인')],
        [sg.Text(size=(40, 1), key='-OUTPUT-')],
        [sg.Text('점수 : 0', key='-SCORE-')],
        [sg.Text('목숨: 3', key='-LIFE-')],
        [sg.Text('', key='-RESULT-', size=(30,1))],
        [sg.Button('Exit')]
    ]

    window = sg.Window('구구단', layout)

    a = 0
    b = 0
    chance = 10

    while True:


        event,ans = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        elif event == 'START':
            a = random.randint(2, 9)
            b = random.randint(1, 9)

            window['-QUESTION-'].Update(f'{a} X {b} = ?')

        elif event == '확인':


            if a*b == int(ans['-INPUT-']):
                score += 10
                window['-OUTPUT-'].update('정답입니다.')
                window['-SCORE-'].update(f'점수 : {score}')


            elif a*b != int(ans['-INPUT-']) and life > 0:
                life -= 1
                window['-OUTPUT-'].update(f'오답입니다. 정답은 {a * b}입니다.')
                window['-LIFE-'].update(f'목숨 : {life}')

            elif life == 0:
                window['-RESULT-'].update(f"게임 종료! 점수: {score}")
                break

            a = random.randint(2, 9)
            b = random.randint(1, 9)
            window['-QUESTION-'].update(f'{a} X {b} = ?')
            window['-INPUT-'].update('')

            # elif a*b != int(ans['-INPUT-']):
            #     life -= 1
            #
            # elif life == 0 :
            #     window['-RESULT-'].update(f"게임 종료! 점수: {score}")

    window.close()

if __name__ == "__main__":
    main()