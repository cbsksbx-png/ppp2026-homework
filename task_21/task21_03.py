import PySimpleGUI as sg
import random

from practice.hangman import words


def main():
    list = ["apple" , "banana" , "pineapple"]
    trial = 7
    game_started = False

    layout = [
        [sg.Text('행맨 게임'), sg.Button('START')],
        [sg.Text('', key='-WORD-', size=(20, 1))],
        [sg.Input(key='-INPUT-', size=(10, 1)), sg.Button('확인')],
        [sg.Text('', key='-OUTPUT-')],
        [sg.Text('목숨: 7', key='-LIFE-')],
        [sg.Text('사용한 글자: ', key='-USED-', size=(30, 1))],
        [sg.Text('', key='-RESULT-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Window Title', layout)

    word = ''
    answer = []

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'START':
            word = random.choice(list)
            answer = ['_'] * len(word)
            trial = 7
            used_letters = set()
            game_started = True


            window['-WORD-'].update(f'{answer}')
            window['-LIFE-'].update(f'목숨: {trial}')
            window['-OUTPUT-'].update('')
            window['-RESULT-'].update('게임을 시작하겠습니다. 이니셜을 입력하시오')

        elif event == '확인':
            initial = values['-INPUT-'].strip().lower()
            window['-INPUT-'].update('')

            if len(initial) != 1 or not initial.isalpha():
                window['-OUTPUT-'].update('알파벳 한 글자만 입력하세요.')
                continue

            if initial in used_letters:
                window['-OUTPUT-'].update(f"'{initial}' 는 이미 입력한 글자입니다.")
                continue

            used_letters.add(initial)

            if initial in word:
                for i, ch in enumerate(word):
                    if ch == initial:
                        answer[i] = initial
                window['-OUTPUT-'].update(f"'{initial}' 정답입니다.")
            else:
                trial -= 1
                window['-OUTPUT-'].update(f"'{initial}' 틀렸습니다.")

            window['-WORD-'].update(' '.join(answer))
            window['-LIFE-'].update(f'목숨: {trial}')
            window['-USED-'].update('사용한 글자: ' + ', '.join(sorted(used_letters)))

            if '_' not in answer:
                window['-RESULT-'].update(f'정답입니다! 단어는 "{word}" 입니다.')
                game_started = False

            elif trial <= 0:
                window['-RESULT-'].update(f'게임 오버! 정답은 "{word}" 입니다.')
                window['-WORD-'].update(' '.join(word))
                game_started = False

    window.close()




if __name__ == "__main__":
    main()