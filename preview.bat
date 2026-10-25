@echo off
cd /d "%~dp0"
echo.
echo  Starting your website preview at http://localhost:8000
echo  Leave this window open while you look around. Close it to stop.
echo.
start "" http://localhost:8000
python -m http.server 8000 || py -m http.server 8000 || (echo. & echo  Python was not found. Install it free from python.org, then double-click this file again. & pause)
