import PySimpleGUI as sg
import random



def spitto():
    num_range = list(range(1, 46))
    lotto = []
    for i in range(6):
        r = random.choice(num_range)
        if r not in lotto:
            lotto.append(r)
        elif r in lotto:
            R = int(r)
            num_range.remove(R)
            x = random.choice(num_range)
            lotto.append(x)
    return lotto

def main():

    result_a = []

    layout = [
        [sg.Text('복권번호추첨') , sg.Button('START')],
        [sg.Text(size=(40, len(result_a)), key='-OUTPUT-')],
        [sg.Button('RESET')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('복권 번호 추첨', layout)

    result = ''

    while True:
        event, values = window.read()

        # lotto = spitto()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        elif event == 'START':
            result += f'{spitto()}\n'
            window['-OUTPUT-'].update(f'{result}')
            result_a.append(result)


        elif event == 'RESET':
            window['-OUTPUT-'].update('')

            # if event == 'START':
                # window['-OUTPUT-'].input('\n')
                # window['-OUTPUT-'].input(f"{spitto()}")

    window.close()

if __name__ == "__main__":
    main()