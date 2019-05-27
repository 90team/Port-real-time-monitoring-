::start Real_Time_Port_Scaner.py
@echo off
set/a _time_1=60*60*3
start "" "Real_Time_Port_Scaner.py"
for /l %%a in (%_time_1% -1 1) do (
cls& echo 剩余时间: %%a [Real_Time_Port_Scaner.exe 已运行]
timeout /t 1 /nobreak>nul)