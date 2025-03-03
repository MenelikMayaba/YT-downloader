from pytube import YouTube

def main():
    """
    Main function to download YouTube videos based on user input.

    Prompts the user to enter a YouTube video URL and a desired download option,
    which can be audio, specific resolution, highest resolution (HD), or lowest
    resolution (LD). The function handles downloading the video according to the
    chosen option and provides feedback on the download status. The process
    continues until the user inputs 'exit' to quit. Handles exceptions and
    provides error messages for invalid inputs or download issues.
    """
    options = ["audio", "resolution", "HD", "LD"]

    while True:
        url = input("Please paste the URL of the video or 'exit' to quit: ").strip()

        if url.lower() == "exit":
            print("Goodbye")
            break

        definition = input(f"What definition would you like?\nPlease choose from {options}: ").strip()

        try:
            yt = YouTube(url)

            if definition == "audio":
                yt.streams.get_audio_only().download()
                print("Audio downloaded successfully.")

            elif definition == "resolution":
                res = input("Enter resolution (e.g., 720p, 480p, etc.): ").strip()
                stream = yt.streams.filter(res=res).first()
                if stream:
                    stream.download()
                    print(f"Video downloaded at {res} resolution.")
                else:
                    print("Resolution not available.")

            elif definition == "HD":
                yt.streams.get_highest_resolution().download()
                print("Highest resolution downloaded.")

            elif definition == "LD":
                yt.streams.get_lowest_resolution().download()
                print("Lowest resolution downloaded.")

            else:
                print(f"Invalid option, please choose from {options}.")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    main()