from pytube import Playlist

pl = Playlist("https://www.youtube.com/playlist?list=PLsRNoUx8w3rORV35WwnmW-YgYZRJF89bJ")
l = pl.download_all("/home/sahil/pytube_test/nptl/")
print(l)
print("done:)")