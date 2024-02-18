@echo off
cd /d "D:\00. WorkSpace\SkylandsmcBot"
call ".\venv\Scripts\activate"
timeout 5
"D:\00. WorkSpace\SkylandsmcBot\venv\Scripts\python" -m watchdog.watchmedo auto-restart --patterns="*.py" --recursive --directory="./" -- "D:\00. WorkSpace\SkylandsmcBot\venv\Scripts\python" -u ./main.py
