from yt_dlp import YoutubeDL

def download(url):

    with YoutubeDL() as ytd:
        ytd.download(url)

def main():
    url = input("enter the link of the video you wnat to downlaod: ")
    history = []
    if "https" not in url:
        raise ValueError("please insert a correct url link")
    
    
    try:
        print("downloading video...")
        download(url)
        print("download complete")
        print("url saved to history")
        history.append(url)

            
            
        url_history = input("do you want to see your download history Y/n? ").lower()

        if url_history == "y":
            print(history)
        elif url_history == 'n':
            pass

    except ValueError:
        print("Something went wrong, please try again")

if __name__ == "__main__":
    main()