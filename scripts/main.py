import magnet_link_finder
import torrent_downloader

output_path = "C:/Users/chitr/Desktop/torrents"

def menu():
	print("1)Search for torrent \n2)Exit")
	choice = input()

	if (choice == '1'):
		try:
			query = input("Name: ")
			# extracting the magnet link
			magnet_link = magnet_link_finder.search_torrent(query)
			# downloading the torrent
			torrent_downloader.torrent_download(magnet_link, output_path)

		except Exception as e:
			print(e)
	
	elif (choice == '2'):
		exit()

if __name__ == '__main__':
	menu()

