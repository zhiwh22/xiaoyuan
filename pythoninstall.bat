@echo off
echo 正在准备安装python,请稍后
echo 如果有是否同意上述条款?输入Y
pause
winget install python
echo 安装完毕
echo 正在下载python web库，请稍后...
pip install web.py
echo 正在下载python urllib.request库，请稍后...
pip install urllib.request
pause
exit