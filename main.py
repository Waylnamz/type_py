import tkinter as tk
import pyautogui

loops = 0
paused = False  # To keep track of whether typing is paused
endless = True  # To keep track of whether typing is on turbo


def type_word():
    global loops, paused
    word = word_entry.get()
    count = int(count_entry.get())
    app = app_entry.get()

    word_label.config(text="")
    count_label.config(text="")

    if not paused and not endless:
        pyautogui.getWindowsWithTitle(app)[0].activate()
        while count > 0:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            count = count - 1

    if not paused and endless:
        pyautogui.getWindowsWithTitle(app)[0].activate()
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        window.after(100, type_word)


def toggle_pause():
    global paused
    paused = not paused
    pause_button.config(text="Resume" if paused else "Pause")


def toggle_endless():
    global endless
    endless = not endless
    endless_button.config(text="Endless On" if endless else "Endless Off")


# Create the main window
window = tk.Tk()

# Create a label to display the word
word_label = tk.Label(window, text="")
word_label.pack(side=tk.TOP)
count_label = tk.Label(window, text="")
count_label.pack(side=tk.LEFT)
app_label = tk.Label(window, text="")
app_label.pack(side=tk.LEFT)

# Create an entry field to enter the word
word_entry = tk.Entry(window)
word_entry.pack(side=tk.TOP)
count_entry = tk.Entry(window)
count_entry.pack(side=tk.LEFT)
app_entry = tk.Entry(window)
app_entry.pack(side=tk.LEFT)

# Create a button to trigger the word typing
button = tk.Button(window, text="Type Word", command=type_word)
button.pack(side=tk.LEFT)

# Create a button to pause/resume typing
pause_button = tk.Button(window, text="Pause", command=toggle_pause)
pause_button.pack(side=tk.LEFT)

# Create a button to turbo typing
endless_button = tk.Button(window, text="Endless", command=toggle_endless)
endless_button.pack(side=tk.LEFT)

# Start the application's main event loop
window.mainloop()
