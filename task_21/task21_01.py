import PySimpleGUI as sg
import time



def main():
    layout = [[sg.Text('타이머') , sg.Button('START')],
                [sg.Text(size=(40, 1), key='-OUTPUT-')],
                [sg.Button('STOP') , sg.Button('Exit')]]

    window = sg.Window('타이머', layout)

    counting = False

    while True:

        event, values = window.read(timeout=1000)

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        elif event == 'START':
            counting = True
            for i in range(10, 0, -1):
                window['-OUTPUT-'].update(f"{i}초")
                window.read(timeout=1000)

            if not counting:
                window['-OUTPUT-'].update(f"타이머 종료")

        # elif event == "STOP":



                # window['-OUTPUT-'].update(f"{i}초")

        # elif event == "STOP":
        #     breakpoint(event == 'start')
        #     window['-OUTPUT-'].update(f"{i}초")

    window.close()

if __name__ == "__main__":
    main()