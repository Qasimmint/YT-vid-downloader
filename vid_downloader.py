from pytube import YouTube
from pytube import Playlist

def sole_video():
    url = "https://www.youtube.com/watch?v=Kljl8oRoaX8"
    vid_tube = YouTube(url)
    title = vid_tube.title
    views = vid_tube.views
    length = vid_tube.length
    caption = vid_tube.captions
    rating = vid_tube.rating
    thumbnail = vid_tube.thumbnail_url
    author = vid_tube.author

    info_values = [title, views, length, caption, rating, thumbnail, author]
    info_keys = ["Title", "Views", "Length", "Caption", "Rating", "Thumbnail", "Author"]
    info_list = list(zip(info_keys, info_values))

    for info in info_list:
        print(info)
    print()
    choice = int(input("Enter only_audios[0], all_videos[1]: "))
    if choice == 1:
        vid_quality = vid_tube.streams.filter(only_video=True)
        vid_list = list(enumerate(vid_quality))
        for i in vid_list:
            print(i)

        resolution = int(input("Chose resolution: "))
        vid_quality[resolution].download()
        print("Downloading Completed Successfully!")

    elif choice == 0:
        vid_quality = vid_tube.streams.filter(only_audio=True)
        vid_list = list(enumerate(vid_quality))
        for i in vid_list:
            print(i)
        resolution = int(input("Chose quality: "))
        vid_quality[resolution].download()
        print("Downloading completed successfully!")

    else:
        print("Enter valid choice")

def playList():
    url = ""
    pl = Playlist(url)

    pl.populate_video_urls()

    descrip = pl.description
    html = pl.html
    length = pl.length
    owner = pl.owner
    owner_id = pl.owner_id
    owner_url = pl.owner_url
    title = pl.title
    views = pl.views

    info = f"description: {descrip}, html:{html}, length: {length}, owner :{owner}, ownder_id: {owner_id}, ownder_url:{owner_url}, title:{title}, views:{views}"
    print(info)

    for videos in pl.videos:
        videos.streams.first.download()
    print("Playlist Downloaded Successfully!")
    print()
    vid_urls = int(input("Wanna check the urls of videos Yes[1], No[0]"))
    if vid_urls == 1:
        for vidz in pl.video_urls:
            print(vidz) 
    else:
        print("Thanks for checking in there!")
        None

def videoType():
    print("Hi, Welcome to YouTube video downloader!")
    option = int(input("What do You want to download, sole_video[0] or playlist[1]"))
    if option == 0:
        return sole_video()
    elif option == 1:
        return playList()
    else:
        print("Chose only through given choices")