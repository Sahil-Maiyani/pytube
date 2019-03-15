import os
import subprocess
from pprint import pprint


def info(folder_path):
    files = os.listdir(folder_path)
    videos = []
    for file in files:
        file, ext = os.path.splitext(file)
        if ext == ".wav":
            videos.append(file + ext)

    hour, min, sec = 0, 0, 0
    for video in videos:
        duration = _getlength(folder_path, video)
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

    hour, min, sec = conversion(hour, min, sec)
    print("Collected {} hours {} minutes {} seconds of data so far:)".format(hour, min, sec))


def _getlength(folder_path, file_path):
    result = subprocess.Popen(["ffprobe", folder_path + "/" + file_path],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # pprint(result.stdout.readlines())
    for line in result.stdout.readlines():
        line = line.decode()
        if "Duration" in line:
            duration = line.split(',')[0].split(':')
            print(duration)
            return duration[1:]


path = input("Enter path:")
info(path)
# /home/sahil/pytube_test
