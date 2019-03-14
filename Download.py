import os
from pytube import Playlist


class Download:
    def __init__(self):
        self.folder_path = input("Enter folder path: ")
        self.playlist_file = input("Enter playlist file path: ")

    def start(self):
        file_flag = self.check_file_exists()
        if file_flag == -1:
            print("ERR in path")
            return -1

        playlists = self._extract_playlist_links()

        for i, link in enumerate(playlists):
            print(" Working with PLAYLIST:", i)
            pl = Playlist(link)
            vid_lists = pl.download_all(self.folder_path)
            with open(self.folder_path, 'a') as csv_file:
                for vid, srt in vid_lists:
                    csv_file.write(vid + "," + srt + '\n')

        print("Done :)")
        return 0

    def _extract_playlist_links(self):
        playlists = []
        with open(self.playlist_file) as file:
            for link in file:
                playlists.append(link.strip())
        return playlists

    def check_file_exists(self):
        if os.path.isdir(self.folder_path) and os.path.isfile(self.playlist_file):
            if not os.path.isdir(self.folder_path + "/video"):
                os.mkdir(self.folder_path + "/video")

            if not os.path.isdir(self.folder_path + "/srt"):
                os.mkdir(self.folder_path + "/srt")
            return 0
        else:
            return -1


d = Download()
d.start()
