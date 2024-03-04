import subprocess
import platform
import win32gui
import win32con

def open_app(app_path, window_title):
	try:
		subprocess.Popen([app_path])
		 # Minimize the window using win32gui
		if platform.system() == "Windows":
			hwnd = win32gui.FindWindow(None, window_title)
			if hwnd:
				win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

	except Exception as e:
		print(e)
