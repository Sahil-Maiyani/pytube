import os
import subprocess
from pprint import pprint

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

    def info(self):
        videos = os.listdir(self.folder_path)
        hour, min, sec = 0, 0, 0
        for video in videos:
            duration = self._getlength(video)
            hour += int(duration[0])
            min += int(duration[1])
            sec += float(duration[2])

        def conversion(hour, min, sec):
            if sec >= 60:
                m, sec = divmod(sec, 60)
                min += m
            if min >= 60:
                h, min = divmod(min, 60)
                hour += h
            return hour, min, sec

        print("Collected {} hours {} minutes {.3f} seconds of data so far:)".format(hour, min, sec))

    def _getlength(self, file_path):
        result = subprocess.Popen(["ffprobe", self.folder_path + "/" + file_path],
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in result.stdout.readlines():
            line = line.decode()
            if "Duration" in line:
                duration = line.split(',')[0].split(':')
                break

        return duration[1:]


d = Download()
d.info()
