import webbrowser
import datetime
import os
import wikipedia
import subprocess


# -------------------------------
# Time Function
# -------------------------------
def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}"


# -------------------------------
# Date Function
# -------------------------------
def get_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    return f"Today's date is {current_date}"


# -------------------------------
# Open Google
# -------------------------------
def open_google():
    webbrowser.open("https://www.google.com")
    return "Opening Google."


# -------------------------------
# Open YouTube
# -------------------------------
def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube."


# -------------------------------
# Search Wikipedia
# -------------------------------
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except Exception:
        return "Sorry, I couldn't find information on Wikipedia."


# -------------------------------
# Google Search
# -------------------------------
def google_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for {query}"


# -------------------------------
# Open Notepad
# -------------------------------
def open_notepad():
    try:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."
    except Exception:
        return "Unable to open Notepad."


# -------------------------------
# Open Calculator
# -------------------------------
def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        return "Opening Calculator."
    except Exception:
        return "Unable to open Calculator."


# -------------------------------
# Play Music
# -------------------------------
def play_music():
    try:
        music_url = "https://music.youtube.com"
        webbrowser.open(music_url)
        return "Opening YouTube Music."
    except Exception:
        return "Unable to play music."

# -------------------------------
# Take Screenshot
# -------------------------------
import pyautogui

def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return "Screenshot taken and saved successfully."
    except Exception:
        return "Unable to take screenshot."