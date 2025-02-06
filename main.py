import speech_recognition as sr
import os
import psutil
import pyttsx3
import subprocess  # todo: For running Android Studio
import webbrowser
import pyautogui
import datetime
import google.generativeai as genai
import re
from config import apiKey
from constants import * 

print(apiKey)

# Configure API Key
genai.configure(api_key=apiKey)

# Initialize recognizer
recognizer = sr.Recognizer()

# todo: Initialize text-to-speech engine
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()
    

# Function to generate a valid filename from a question
def generate_filename(question):
    # Remove special characters and spaces, then convert to lowercase
    filename = re.sub(r'[^a-zA-Z0-9]+', '_', question).lower()  
    filename = filename.strip('_')  # Remove leading/trailing underscores
    return filename

def ask_gemini(question):
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel("gemini-pro")
        
        # Generate response
        response = model.generate_content(question)

        # Get response text
        answer = response.text

        # Generate a unique filename with date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        # Generate a valid filename based on the question
        filename = f"{generate_filename(question)}_{timestamp}.txt"


        # Define the file path inside the Gemini folder
        file_path = os.path.join(gemini_folder, filename)

        # Save the answer to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(answer)

        print(f"✅ Answer saved to: {file_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

def takeCommand():
    # Use the microphone as source
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Capture the audio
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            text = recognizer.recognize_google(audio, language="en-in")  # Convert speech to text using Google API
            print("You said:", text)
            return text
            
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return "Sorry, I could not understand you."
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
            return "Sorry, there was an error with the service."
            
def open_android_studio():
    android_studio_path = r"C:\Program Files\Android\Android Studio\bin\studio64.exe"  # Update path if different
    try:
        subprocess.Popen([ANDROID_STUDIO_PATH])  # Open Android Studio
        print(ANDROID_STUDIO_IS_OPENING)
        say(OPENING_ANDROID_STUDIO)
    except Exception as e:
        say(f"Failed to open Android Studio. Error: {e}")

def close_android_studio():
    found = False
    # Iterate over all processes and look for 'studio.exe' or 'java.exe' (Android Studio may use Java in the background)
    for proc in psutil.process_iter(['pid', 'name']):
        # print(f"Checking process: {proc.info['name']}")  # Debugging step to print all process names
        if 'studio.exe' in proc.info['name'].lower() or 'java.exe' in proc.info['name'].lower()  or 'studio64.exe' in proc.info['name'].lower():
            proc.terminate()  # Kill the process
            print(ANDROID_STUDIO_IS_CLOSED)
            say(ANDROID_STUDIO_HAS_BEEN_CLOSED)
            found = True
            break
    
    if not found:
        say(ANDROID_STUDIO_IS_NOT_RUNNING)
        
def open_office_project(project_name):
    # Path to the project folder
    project_paths = {
        "office": OFFICE_PROJECT,
        "mobile": OFFICE_ICPX_MOBILE_PROJECT
    }
    project_path = project_paths.get(project_name.lower(), None)
    if project_path is None:
        print(f"Project path for {project_name} not found.")
        say(f"Project path for {project_name} not found.")
        return
    
    print(f"Project path: {project_path}") 
    try:
        subprocess.Popen(["code", f'"{project_path}"'])  # Open Visual Studio Code with the project folder
        print(f"Opening Office Project in Visual Studio Code...")
        say("Opening your office project in Visual Studio Code now.")
    except Exception as e:
        say(f"Failed to open the project. Error: {e}")

def close_vsc():
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        # Debugging to print the process name
        print(f"Checking process: {proc.info['name']}")
        if 'code.exe' in proc.info['name'].lower() or 'Code.exe' in proc.info['name'].lower() :   # 'code.exe' is the process name for VSC
            proc.terminate()  # Kill the process
            print("Visual Studio Code is closed.")
            say(VISUAL_STUDIO_CODE_CLOSED)
            found = True
            break

    if not found:
        say(VISUAL_STUDIO_CODE_IS_NOT_RUNNING)

def take_screenshot():
    # Get the user's Downloads folder path
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Get the current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    screenshot_filename = f"screenshot_{timestamp}.png"

    # Define the screenshot filename
    screenshot_path = os.path.join(downloads_folder, screenshot_filename)

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot in the Downloads folder
    screenshot.save(screenshot_path)

while True:
    query = takeCommand()
    sites = [
        ["YouTube", YOUTUBE_URL],
            ["Wikipedia", WIKIPEDIA_URL],
            ["google", GOOGLE_URL],
            ["chat gpt", CHAT_GPT],
            ["code list", CODE_LIST],
            ["linkedin", LINKEDIN]
            ]
    for site in sites:
        if query and f"Open {site[0]}".lower() in query.lower():
            webbrowser.open(site[1])
            say(query)
            
    # Check if the command is to open Android Studio
    if "open android studio".lower() in query.lower():
        open_android_studio()  # Call the method to open Android Studio
    
    # Check if the command is to close Android Studio
    if "close android studio".lower() in query.lower():
        close_android_studio()  # Call the method to close Android Studio
    
 
            
    if "open my office project".lower() in query.lower() or "open office project"in query.lower():
        open_office_project("office")
    elif "open office mobile app project".lower() in query.lower() or "open mobile project"in query.lower():
        open_office_project("mobile")
        
    # Check if the command is to close Visual Studio Code
    if "close office project" in query.lower() or "close visual studio code" in query.lower():
        close_vsc()  # Call the method to close VSC
    
    # Check for stop condition, you can change the stop phrase as per your need
    if "stop listening".lower() in query.lower():
        say(STOP_LISTENING)
        break  # Break the loop to stop listening
    
    if "the time".lower() in query.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"sir the time is {current_time}")
        # Break the loop to stop listening
    
    if "take screenshot".lower() in query.lower() or "take a screenshot".lower():
        take_screenshot()
        
        
    if "hey gemini tell me".lower() in query.lower():
        say("Sure! Ask your question.")
        if query:
            ask_gemini(question = query)
        else:
            say("Sorry, I couldn't hear your question.")
    else:
        continue

