from tkinter import *
from center import centering
from pygame import mixer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F6E4F6"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

MINUTES = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN]
TEXTS = ["Work", "Break", "Work", "Break", "Work", "Break", "Work", "Break", "Break"]
indeks = 0
check_str="✔"

window = Tk()
window.title("Pomodoro technique")
window.resizable(False, False)
window.configure(bg=PINK)
window.geometry("{}x{}+{}+{}".format(centering(window)[0], centering(window)[1], centering(window)[2], centering(window)[3]))

# ---------------------------- TIMER RESET ------------------------------- #
should_continue = True
def reset_count():
    global should_continue, start, indeks, check_str
    indeks = 0
    lbl1.configure(text="Welcome")
    check_str="✔"
    lbl2.configure(text="✔")
    should_continue = False
    start = False
# ---------------------------- TIMER MECHANISM ------------------------------- #
start = False
def start_count():
    global start, should_continue
    if not start:
        start = True
        should_continue = True
        lbl1.configure(text=TEXTS[indeks])
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global indeks, check_str
    if count>=0:
        minutes = "{:0>2d}".format(count//60)
        seconds = "{:0>2d}".format(count%60)
        if should_continue:
            canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
            window.after(1000, count_down, count - 1)
        else:
            minutes = "{:0>2d}".format(WORK_MIN)
            canvas.itemconfig(timer, text=f"{minutes}:00")
    else:
        window.deiconify()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        indeks += 1
        indeks = indeks % 9
        if indeks == 0:
            check_str = "✔"
        elif indeks % 2 == 0 and indeks != 8:
            check_str += "✔"
        lbl2.configure(text=check_str)
        lbl1.configure(text=TEXTS[indeks])
        mixer.music.play()
        count_down(MINUTES[indeks]*60)

# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=202, height=223, bg=PINK, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(102, 111, image=img)
if WORK_MIN < 10:
    WORK_MIN = f"0{WORK_MIN}"
timer = canvas.create_text(102, 121, text=f"{WORK_MIN}:00", fill="white", font=("Courier", 24, "bold"))
WORK_MIN = int(WORK_MIN)
canvas.grid(row=2, column=2)
mixer.init()
mixer.music.load("notification.mp3")

lbl1 = Label(text="Welcome", font=("Courier", 30, "bold"),bg=PINK, anchor="s", height=3, fg="#472D2D")
lbl1.grid(row=1, column=2)

strt = Button(text="Start",font=("Courier", 10), height=2, width=8, command=start_count)
strt.grid(row=3, column=1, padx=(160,10))

rst = Button(text="Reset", font=("Courier", 10), height=2, width=8, command=reset_count)
rst.grid(row=3, column=3, padx=10)

lbl2 = Label(text=check_str, font=("Courier", 10, "bold"),anchor="n", bg=PINK, height=3)
lbl2.grid(row=4, column=2)
window.mainloop()