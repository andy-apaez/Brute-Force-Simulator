Brute Force Attack Simulator 🔐

A real-time password guessing simulator built with Python (Flask) and JavaScript.
This educational tool demonstrates how brute-force and dictionary attacks work, streaming live guesses, progress, and speed directly in the browser.
It helps users understand the importance of strong, complex passwords and common vulnerabilities.

---
## Demo 

![ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/89776196-8bc1-479e-b726-e087b542308e)

---
Features ✨

Dictionary Attack – Quickly guesses common passwords from a wordlist.

Mutated Variations – Tests variations like capitalized words, numbers, and common substitutions.

Brute Force Attack – Attempts all possible combinations of characters up to a specified length. (current is 5 characters long, but can be configured)

Real-Time Streaming – Live progress bar, attempts counter, and current guess display.

---
Installation ⚙️

Clone the repository:

`git clone https://github.com/andy-apaez/Brute-Force-Tester.git
cd Brute-Force-Tester`

---
Install dependencies:

`pip install flask`


Make sure index.html is in a folder called templates and style.css is in a folder called static

---
Usage (Open Terminal) 🚀

Run the Flask app:

`python app.py` OR `python3 app.py`


Open your browser at:

http://127.0.0.1:5000

Enter a password to simulate and click Start Attack.

---
Watch the progress bar, current guesses, attempts, and speed update in real time.

⚠ Tip: Start with short passwords (1–3 characters) for testing. Brute force time grows exponentially with length and character set.

---
Configuration 🛠️

Max Password Length: Modify max_length in app.py or configure from the frontend.

Character Set: Default is lowercase letters + digits; can be extended to uppercase and symbols.

Wordlist: Replace wordlist.txt with your own list of common passwords for dictionary attacks.

---
Learning Outcomes 📚

Understand the mechanics of brute-force and dictionary attacks.

Learn how password complexity affects security.

Explore real-time data streaming with Flask and Server-Sent Events (SSE) using JavaScript.

Gain experience in building interactive web-based security simulations.

---
License 📝

This project is for educational purposes only. Use responsibly and never test passwords on accounts you do not own.
