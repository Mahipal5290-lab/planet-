@echo off
title Beyond Andromeda Server
cd /d "%~dp0"
echo ========================================================
echo       Beyond Andromeda - Deep Space Mission Console
echo ========================================================
echo Starting server at http://localhost:8080 ...
start http://localhost:8080
python serve.py 8080
pause
