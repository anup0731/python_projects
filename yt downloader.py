from pytube import YouTube
link = input("please provide your link")
youtube_1 = YouTube(link)
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("please provide your index you want to download"))
videos[strm].download()
print("successfully")  