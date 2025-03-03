from pytube import YouTube

def main():
    url = input("please paste the url of the video: ")

    yt = YouTube(url)

    yt.streams.get_highest_resolution().download


if __name__ == "__main__":
    main()