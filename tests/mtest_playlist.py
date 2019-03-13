from pytube import Playlist

pl = Playlist("https://www.youtube.com/playlist?list=PLRAV69dS1uWTesDLqDluecCuxHVv4BTJ7")
pl.download_all("/home/sahil/pytube_test/nptl/")
print("done:)")