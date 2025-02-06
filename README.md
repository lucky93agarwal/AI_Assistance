# Astra - Windows Desktop AI Assistant 🤖

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A voice-activated AI assistant for Windows that performs system operations, web navigation, and intelligent interactions using Gemini AI.

## 🌟 Features Overview

### **Application Control**
- Open/Close Windows Applications
- Launch Developer Tools (Android Studio)
- Manage Music Playback
- System Command Execution

### **System Operations**
- Launch/Close Windows Applications (Notepad, Calculator, etc.)
- Terminate Android Studio processes
- Manage Assistant listening state
- System resource monitoring

### **Web Automation**
- Open Websites: 
  `YouTube, Instagram, Google, Wikipedia, ChatGPT, Codelist`
- Smart Search Integration
- Custom Web Shortcuts

### **AI Capabilities**
- Gemini AI Integration 🧠
- Natural Language Processing (NLP)
- Voice Command Recognition
- Contextual Conversations

### **Core Functionality**
- Background Listening Mode 🎤
- Voice Activation/Deactivation
- Cross-Platform Control
- Custom Command Configuration

### **Media & Utilities**
- Music playback control 🎤
- Screenshot capture (Downloads/ directory)
- Voice-controlled screenshot management
- Joke telling functionality

## 🚀 Installation

### **Prerequisites**
- Python 3.8+
- Windows 10/11
- Microphone (Recommended)
- Windows 10/11 (64-bit)
- Administrative privileges (for system operations)
- Google account (for Gemini API)

```bash
# Clone repository
git clone https://github.com/yourusername/windows-ai-assistant.git
cd windows-ai-assistant

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
```


## Required Libraries 📚

### **Virtual Environment:**
- To manage project dependencies, create a virtual environment with the following command:
  ```bash
  python -m venv venv
  ```
- Then activate it:
  ```bash
  venv\Scripts\activate
  ```
### **Install Dependencies:**
- Audio Handling:
  ```bash
  pip install pyaudio
  ```
- Speech Recognition:
  ```bash
  pip install SpeechRecognition
  ```
- Text-to-Speech (TTS):
  ```bash
  pip install pyttsx3
  ```
- Google Gemini API:
  ```bash
  pip install google-generativeai
  ```
- Joke Functionality:
  ```bash
  pip install pyjokes
  ```
- Screenshot Capture (pyautogui):
  ```bash
  pip install pyautogui
  ```

## Running the Assistant 🎤
Once the environment is set up and dependencies are installed, run your assistant with:
```bash
python assistant_script.py
```
The assistant will begin listening for commands, such as:
- "Open YouTube"
- "Close Android Studio"
- "Play music"
- "Talk with Gemini"
  
## Command List 📜

### **System Operations:**
- "Open [Application Name]" (e.g., "Open Notepad")
- "Close [Application Name]" (e.g., "Close YouTube")

### **Web Automation:**
- "Open [Website Name]" (e.g., "Open Google")
- "Search [Query]" (e.g., "Search Python tutorials")

### **Music Control:**
- "Play music"
- "Pause music"
- "Stop music"

### **Screenshots:**
- "Take a screenshot"
- "Show screenshot"

### **AI Interaction:**
- "Talk with Gemini"
- "Ask Gemini about [topic]"

## 🌟 Troubleshooting 🛠️

### **Python Version Check**
To verify if Python is installed:
```bash
python --version
# or
python3 --version
```

### **Setting Up Virtual Environment**

- Install Virtual Environment:
```bash
pip install virtualenv
```

- Activate the Virtual Environment:
```bash
venv\Scripts\activate
```

- Install Dependencies:
```bash
pip install -r requirements.txt
```

## 🌟 File Structure 📂
```bash
windows-ai-assistant/
├── src/
│   ├── main.py            # Main application entry
│   ├── speech_engine.py   # Speech recognition/TTS
│   ├── ai_handler.py      # Gemini integration
│   └── system_utils.py    # OS operations
├── config/
│   ├── app_paths.json     # Application shortcuts
│   └── commands.json      # Voice command mappings
├── requirements.txt       # Dependency list
└── .env                   # Environment variables
```

## Visitors Count

<img align="left" src = "https://profile-counter.glitch.me/local_notifications/AI_Assistance.svg" alt ="Loading">
