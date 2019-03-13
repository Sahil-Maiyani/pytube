from pytube import YouTube

yt = YouTube("https://youtu.be/fV2k2ivttL0")
caption = yt.captions.get_by_language_code('en')
with open(yt.title + '.srt', 'w') as file:
    file.write(caption.generate_srt_captions())
print("done:)")