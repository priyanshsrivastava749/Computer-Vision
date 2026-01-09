@echo off
echo Starting Phone Detector...
echo 1. Opening Browser to http://localhost:8000
start "" "http://localhost:8000/index.html"
echo 2. Starting Local Web Server...
echo --------------------------------------------
echo KEEP THIS WINDOW OPEN while using the app!
echo --------------------------------------------
"C:\Users\HP\AppData\Local\Python\bin\python.exe" -m http.server 8000
pause
