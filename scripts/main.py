import magnet_link_finder
import torrent_downloader
import open_qbit

output_path = "" # put your output directory in it
app_path = "C:/Program Files/qBittorrent/qbittorrent.exe"
window_title = "qBittorrent v4.5.5"

def menu():
	print("1)Search for torrent \n2)Exit")
	choice = input()

	if (choice == '1'):
		try:
			query = input("Name: ")
			open_qbit.open_app(app_path, window_title)
			# extracting the magnet link
			magnet_link = magnet_link_finder.search_torrent(query)
			# downloading the torrent
			torrent_downloader.torrent_download(magnet_link, output_torrent_path)

		except Exception as e:
			print(e)
	
	elif (choice == '2'):
		exit()

if __name__ == '__main__':
	menu()

