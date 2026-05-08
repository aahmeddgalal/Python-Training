import yt_dlp
import os

def download_video():
    link = input("Enter the YouTube URL: ").strip()

    print("\n--- Choose Browser for Cookies (to bypass bot check) ---")
    print("1. Chrome")
    print("2. Firefox")
    print("3. Edge")
    print("4. Use cookies.txt file (Recommended for Chrome)")
    print("5. No cookies")
    browser_choice = input("Select your primary option (1-5): ")

    browsers = {'1': 'chrome', '2': 'firefox', '3': 'edge'}
    
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    if browser_choice in browsers:
        selected_browser = browsers[browser_choice]
        ydl_opts['cookiesfrombrowser'] = (selected_browser,)
    elif browser_choice == '4':
        cookies_file = input("Enter the path to your cookies.txt file (e.g. cookies.txt): ").strip()
        if os.path.exists(cookies_file):
            ydl_opts['cookiefile'] = cookies_file
        else:
            print("Cookie file not found. Proceeding without cookies.")
    elif browser_choice == '5':
        pass
    else:
        print("Invalid choice. Proceeding without cookies.")

    print("\n--- Choose Format ---")
    print("1. Video (Best Quality)")
    print("2. Audio Only (MP3)")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
    elif choice == '2':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("\nSuccess!")
    except Exception as e:
        print(f"\nError: {e}")
        error_msg = str(e).lower()
        if "dpapi" in error_msg:
            print("\nTIP: Chrome's new security features prevent direct cookie extraction.")
            print("Please use a 'Get cookies.txt LOCALLY' extension to export cookies to a file, and use Option 4.")
        elif "locked" in error_msg or "database is locked" in error_msg:
            print("\nTIP: Your browser might be locking the cookies database. Please fully close your browser and try again.")
        else:
            print("\nTIP: Make sure the video is playable in your browser before running.")

if __name__ == "__main__":
    download_video()
