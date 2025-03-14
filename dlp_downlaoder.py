from yt_dlp import YoutubeDL

def download(url:str):

    with YoutubeDL() as ytd:
        ytd.download(url)
        info = ytd.extract_info(url)
        print(f"'{info['title']}' successfully downloaded")
    
def main():
    while True:
        try:

            url = input("enter the link of the video you wnat to downlaod: ")
            history = []
            if "https" or "www" not in url:
                raise ValueError("please insert a correct url link")
    
    
        
            print("downloading video...")
            download(url)
            print("url saved to history") 
            history.append(url)

                
                
            url_history = input("Show download history or exit? (Y/n/exit): ").lower()

            if url_history == "y":
                print(history)
                continue
            elif url_history == 'n':
                continue
            elif url_history == "exit":
                print("exiting, goodbye..." )
                break
            
                
                

        except ValueError:
            print("Something went wrong, please try again")
            

if __name__ == "__main__":
    main()