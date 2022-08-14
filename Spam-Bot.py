import tkinter as tk
from tkinter import messagebox as msg
from pyautogui import write, press
from time import time, sleep


def start(time_sleep, content, times, delay):
    sleep(time_sleep)
    first_time = time()
    for i in range(times):
        write(content)
        press("enter")
        sleep(delay)
    print("Done")
    final_time = time() - first_time
    msg.showinfo("DONE!", f"Done!\nIt took {round(final_time,2)} seconds to write {content} {times} times!")
    print(f"Done!\nIt took {final_time} seconds to write {content} {times} times!")


if __name__ == "__main__":
    # Main Window
    print("Launching..")
    root = tk.Tk()
    root.geometry("500x410+50+50")
    root.resizable(False, False)
    root.title("Spam-Bot")
    root.config(bg="black")

    # Entries
    e1 = tk.Entry(root)
    e1.place(x=180, y=122, width=300)
    e2 = tk.Entry(root)
    e2.place(x=180, y=162, width=300)
    e3 = tk.Entry(root)
    e3.place(x=180, y=202, width=300)
    e4_value = tk.StringVar(value="0")
    e4 = tk.Entry(root, textvariable=e4_value)
    e4.place(x=180, y=242, width=300)

    # Labels
    l1 = tk.Label(root, text="Content:", font=("Arial", 25), bg="black", fg="white")
    l1.place(x=10, y=120)
    l2 = tk.Label(root, text="How often:", font=("Arial", 25), bg="black", fg="white")
    l2.place(x=10, y=160)
    l3 = tk.Label(root, text="Start delay:", font=("Arial", 25), bg="black", fg="white")
    l3.place(x=10, y=200)
    l4 = tk.Label(root, text="Delay:", font=("Arial", 25), bg="black", fg="white")
    l4.place(x=10, y=240)
    main_text = tk.Label(root, text="A completely normal", font=("PT mono bold", 40), bg="black", fg="white")
    main_text.place(x=30, y=0)
    main_text2 = tk.Label(root, text="Spam-Bot", font=("menlo bold", 50), bg="black", fg="white")
    main_text2.place(x=130, y=50)

    # Start with parameters
    def start_local():
        try:
            start(int(e3.get()), e1.get(), int(e2.get()), int(e4.get()))
        except ValueError:
            print("Not all values are integers!")
            msg.showwarning("FATAL VALUE ERROR", "FATAL ERROR!\nNot all text fields are filled with integers!")


    # Buttons
    start_button = tk.Button(root, text="Start", fg="green", bg="white", height=2, width=6, font=("Arial Bold", 40),
                             command=start_local)
    start_button.place(x=150, y=290)

    root.mainloop()
