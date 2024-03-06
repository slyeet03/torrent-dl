from qbittorrent import Client
import time

def torrent_download(magnet_link, output_path):
	# connecting to the web ui
	qb = Client("", timeout=10) #put "your ip address:port" between the '''

	# creds
	qb.login("", "") #put your username and password

	# downloading torrent
	qb.download_from_link(magnet_link, savepath=output_path)
	time.sleep(5)

	while True:
		# Sleep for a short duration before checking again
		time.sleep(60)

		# Check the status of downloading torrents
		torrent_info = qb.torrents()
		torrent_hash = torrent_info[0]['hash']
		torrent_state = str(torrent_info[0]['state'])

		if torrent_state == 'stalledUP':
			qb.pause(torrent_hash)
			print(f"Torrent {torrent_hash} has completed downloading and has been paused")
			break

		

