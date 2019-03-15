import os
from pprint import pprint


class Separator:
    def __init__(self, work_path, videos_path):
        self.work_path = work_path
        self.videos_path = videos_path
        self.fwav_list = None
        self.fvtt_list = None

    def check_file_exists(self):
        self.work_path = "/home/sahil/pytube_test"
        self.videos_path = self.work_path
        if os.path.isdir(self.work_path) and os.path.isdir(self.videos_path):
            if not os.path.isdir(self.work_path + "/audio"):
                os.mkdir(self.work_path + "/audio")

            if not os.path.isdir(self.work_path + "/srt"):
                os.mkdir(self.work_path + "/srt")
            return 0
        else:
            return -1

    def sepatate_wav_n_vtt(self):
        print("Starting...move vtt file")
        self.check_file_exists()
        files_list = []
        for file in os.listdir(self.work_path):
            fname, ext = os.path.splitext(file)
            files_list.append((fname, ext))
        self.fwav_list, self.fvtt_list = [file for file in files_list if file[1] == ".wav"], [file for file in
                                                                                              files_list if
                                                                                              file[1] == ".vtt"]

        for vtt in self.fvtt_list:
            os.rename(self.videos_path + "/" + vtt[0] + vtt[1], self.work_path + "/srt/" + vtt[0] + vtt[1])
        print("Done...move vtt file")




work_path = input("Enter work path:")
videos_path = input("Enter videos folder path:")

s = Separator(work_path, videos_path)
s.sepatate_wav_n_vtt()
