# Torrent Downloader CLI

A CLI agent for searching torrent and downloading it using qbittorrent.

## Getting Started
### Prerequisities
1. Python-3.6 or above
2. BeautifulSoup or bs4
3. pyperclip
4. requests
5. re
6. selenium
7. time
8. qbittorrent

### Setting up Qbittorent
Open the WebUI setting page on qbittorrent

![qbit_settings_open](screenshots/qbit_settings_open.png)
![qbit_webui](screenshots/qbit_webui.png)

1. Enable the Web User Interface(Remote Control) option.
2. Set the username and password(by default it will be set to admin).
3. Right click and open file `torrent_downloader.py` in your desired text editor, at line 7 replace the `admin` and `password` with the username and password you set.
4. Save the file

### Installing
Clone or download it from github and install all the requirements. You can install them easily by this command `pip3 install requirements.txt` or install one by one, and then run main.py
`py main.py`

### Screenshots
![CLI](screenshots/result_terminal.png)
![qbit](screenshots/result_qbit.png)


## License
This project is licensed under the [MIT License](LICENSE).

