from yt_dlp import YoutubeDL

def download(url):

    with YoutubeDL() as ytd:
        ytd.download(url)

def main():
    url = input("enter the link of the video you wnat to downlaod: ")

    print("downloading video...")
    download(url)
    print("download complete")

if __name__ == "__main__":
    main()