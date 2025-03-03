from pytube import YouTube

def main():


    options = [ "audio", 'resolution', 'HD', 'LD']

    while True:
        
        url = input("please paste the url of the video or 'exit' to quit: ").strip()

        if url.lower()== "exit":
            print("goodbye")
            break

        definition =input(f"what definiton would you like?\n please choose from{options}: ")

        
        try:
            yt = YouTube(url)

            if definition == "audio":
                yt.streams.get_audio_only().download()
            
            elif definition == "resolution":
                res = input("Enter resolution (e.g., 720p, 480p, etc.): ").strip()
                stream = yt.streams.filter(res=res).first()
                if stream:
                    stream.download()
                    print(f"video downloaded at {res} resolution")
                else:
                    print("resolution not avaiable")

            elif definition == "HD":
                yt.streams.get_highest_resolution().download()
                print("highest resolution downlaoded")

            elif definition == "LD":
                yt.streams.get_lowest_resolution().download()
                print("lowest resolution downloaded")

            else:
                if definition not in options:
                    print(f"invalid option, please choose from {options} ")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    main()