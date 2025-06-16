from pytube import YouTube

def Download(link):
    try:
        youtubeObject = YouTube(link)
        stream = youtubeObject.streams.get_highest_resolution()
        print(f"Downloading: {youtubeObject.title}")
        stream.download()
        print("Download is completed successfully")
    except Exception as e:
        print("An error has occurred:", e)

link = input("Enter the YouTube video URL: ")
Download(link)
