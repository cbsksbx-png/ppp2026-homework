from tkinter import *
from datetime import datetime
import calendar           # monthrange()로 월 총 일수 계산
from functools import partial  # 버튼 콜백에 인자를 미리 바인딩하기 위해 사용

from calender_list import file_module, find_notes, note_exists  # 날짜 클릭 시 호출되는 외부 모듈

# 전역 위젯 참조: main()에서 초기화되고 이벤트 핸들러에서 접근
spinbox_M = None   # 월 선택 Spinbox
spinbox_Y = None   # 연도 선택 Spinbox
buttons = {}       # 날짜 버튼 딕셔너리, 키: 'D{행}-{열}'
root = None        # 메인 tkinter 창
default_button_bg = None


def get_start_col(year, month):
    """해당 월 1일이 그리드의 몇 번째 열(요일)에 위치하는지 반환.

    그리드 열 배치: 0=일, 1=월, 2=화, 3=수, 4=목, 5=금, 6=토
    datetime.weekday()는 0=월~6=일 반환 → 일요일 기준 그리드에 맞게 +1 후 mod 7
      예) weekday()=6(일요일) → (6+1)%7 = 0 → col 0(일 열)
          weekday()=0(월요일) → (0+1)%7 = 1 → col 1(월 열)
    """
    return (datetime(year, month, 1).weekday() + 1) % 7


def clear_buttons():
    """날짜 버튼 6행×7열 전체를 빈 상태로 초기화.

    월을 변경할 때 이전 달의 날짜가 남지 않도록 render_calendar() 호출 전에 실행.
    """
    for r in range(6):
        for c in range(7):
            foreground = 'red' if c == 0 else 'blue' if c == 6 else 'black'
            buttons[f'D{r}-{c}'].config(
                text='', command='', bg=default_button_bg, fg=foreground
            )


def render_calendar():
    """Spinbox에서 연도·월을 읽어 달력 버튼 그리드를 그린다.

    알고리즘:
      1) 1일의 열 위치(start_col)를 구한다.
      2) 날짜 d(1-based)의 그리드 절대 위치 = start_col + (d - 1)
      3) divmod(절대위치, 7) → (행, 열)
      4) 해당 버튼에 날짜 텍스트와 클릭 콜백을 설정한다.
    """
    year = int(spinbox_Y.get())
    month = int(spinbox_M.get())

    clear_buttons()

    start_col = get_start_col(year, month)
    total_days = calendar.monthrange(year, month)[1]  # (첫째 날 요일, 총 일수)[1]
    today = datetime.today().date()

    for day in range(1, total_days + 1):
        # 절대 셀 위치를 행/열로 변환
        row, col = divmod(start_col + day - 1, 7)
        filename = f'{year:04d}-{month:02d}-{day:02d}.txt'
        is_today = datetime(year, month, day).date() == today
        has_note = note_exists(filename)
        background = '#ffcc80' if is_today and has_note else '#fff59d' if is_today else '#c8e6c9' if has_note else default_button_bg

        buttons[f'D{row}-{col}'].config(
            text=day,
            bg=background,
            # partial로 날짜 문자열을 콜백에 미리 바인딩
            # (lambda를 쓰면 루프 변수 캡처 문제로 모든 버튼이 같은 날짜를 가리킴)
            command=partial(file_module, filename, root, render_calendar)
        )


def render_calendar_if_valid(event=None):
    """직접 입력 중인 Spinbox 값이 유효할 때만 달력을 갱신한다."""
    try:
        render_calendar()
    except ValueError:
        pass


def open_monthly_search():
    """현재 선택한 월의 저장 메모를 파일명과 본문으로 검색한다."""
    year = int(spinbox_Y.get())
    month = int(spinbox_M.get())
    window = Toplevel(root)
    window.title(f'{year}년 {month}월 메모 검색')
    window.geometry('360x300')

    query = StringVar()
    Entry(window, textvariable=query).pack(fill=X, padx=10, pady=(10, 4))
    result_list = Listbox(window)
    result_list.pack(fill=BOTH, expand=True, padx=10, pady=4)
    status = Label(window)
    status.pack(pady=(0, 10))

    def refresh_results(*_):
        filenames = find_notes(year, month, query.get())
        result_list.delete(0, END)
        for filename in filenames:
            result_list.insert(END, filename.removesuffix('.txt'))
        status.config(text=f'{len(filenames)}개의 메모')

    def open_selected(event=None):
        selected = result_list.curselection()
        if selected:
            filename = f'{result_list.get(selected[0])}.txt'
            file_module(filename, root, render_calendar)

    query.trace_add('write', refresh_results)
    result_list.bind('<Double-Button-1>', open_selected)
    Button(window, text='메모 열기', command=open_selected).pack(pady=(0, 10))
    refresh_results()


def count_plus():
    """월 Spinbox를 1 증가시킨다. 12월을 넘으면 1월로 순환."""
    val = int(spinbox_M.get())
    year = int(spinbox_Y.get())

    if val >= 12:
        if year >= int(spinbox_Y.cget('to')):
            return
        val = 1
        spinbox_Y.delete(0, END)
        spinbox_Y.insert(0, year + 1)
    else:
        val += 1

    spinbox_M.delete(0, END)
    spinbox_M.insert(0, val)
    render_calendar()


def count_minus():
    """월 Spinbox를 1 감소시킨다. 1월 아래로 내려가면 12월로 순환."""
    val = int(spinbox_M.get())
    year = int(spinbox_Y.get())

    if val <= 1:
        if year <= int(spinbox_Y.cget('from')):
            return
        val = 12
        spinbox_Y.delete(0, END)
        spinbox_Y.insert(0, year - 1)
    else:
        val -= 1

    spinbox_M.delete(0, END)
    spinbox_M.insert(0, val)
    render_calendar()


def main():
    """tkinter 윈도우와 위젯을 초기화하고 이벤트 루프를 시작한다.

    그리드 레이아웃 (frame1 내부):
      row 0: 연도 Spinbox
      row 1: <- 버튼 | 월 Spinbox | -> 버튼
      row 2: 요일 헤더 (일~토)
      row 3~8: 날짜 버튼 6행 × 7열
      row 9: Exit 버튼
    """
    global spinbox_M, spinbox_Y, buttons, root, default_button_bg
    today = datetime.today()

    root = Tk()
    root.title("calendar")
    root.geometry("290x280")

    frame1 = Frame(root, relief="solid", bd=2)

    # ── 연도 선택 (row 0) ──────────────────────────────────────────
    year = IntVar(value=today.year)
    spinbox_Y = Spinbox(frame1, from_=1900, to=today.year + 100, width=5, textvariable=year)
    spinbox_Y.grid(row=0, column=3)
    Label(frame1, text="년").grid(row=0, column=4)
    Button(frame1, text='검색', command=open_monthly_search).grid(row=0, column=5)

    # ── 월 선택 (row 1) ───────────────────────────────────────────
    Button(frame1, text="<-", width=3, command=count_minus).grid(row=1, column=0)
    month = IntVar(value=today.month)
    spinbox_M = Spinbox(frame1, from_=1, to=12, width=2, textvariable=month)
    spinbox_M.grid(row=1, column=3)
    Label(frame1, text="월", width=3).grid(row=1, column=4)
    Button(frame1, text="->", width=3, command=count_plus).grid(row=1, column=5)

    for spinbox in (spinbox_Y, spinbox_M):
        spinbox.configure(command=render_calendar_if_valid)
        spinbox.bind('<Return>', render_calendar_if_valid)
        spinbox.bind('<FocusOut>', render_calendar_if_valid)

    # ── 요일 헤더 (row 2): 일요일(col 0) ~ 토요일(col 6) ────────────
    days = ['일', '월', '화', '수', '목', '금', '토']
    for i in range(7):
        Button(frame1, text=days[i], width=3).grid(row=2, column=i)

    # ── 날짜 버튼 그리드 (row 3~8) ────────────────────────────────
    # 키 형식: 'D{행}-{열}' (행 0~5, 열 0~6)
    # 일요일 열(col 0)은 빨간색, 토요일 열(col 6)은 파란색으로 구분
    buttons = {}
    for r in range(6):
        for c in range(7):
            btn = Button(frame1, text='', width=3)
            btn.grid(row=3 + r, column=c)
            buttons[f'D{r}-{c}'] = btn
            if default_button_bg is None:
                default_button_bg = btn.cget('bg')
            if c == 0:
                btn.config(fg='red')
            elif c == 6:
                btn.config(fg='blue')

    # frame1.quit은 mainloop만 중단 → 창이 남아 두 번 클릭해야 닫히는 문제 발생
    # root.destroy는 mainloop 중단 + 창 제거를 한 번에 처리
    Button(frame1, text='Exit', command=root.destroy).grid(row=9, column=6)
    frame1.pack(side="left", fill="both", expand=True)
    render_calendar()

    root.mainloop()


if __name__ == "__main__":
    main()
