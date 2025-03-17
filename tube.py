import os
from pytubefix import YouTube, request
from tqdm import tqdm
import subprocess

request.default_range_size = 1048576
progress_bar = None

def on_progress(video_stream, data_chunk, bytes_remaining):
    global progress_bar
    current_downloaded = video_stream.filesize - bytes_remaining
    progress_update = current_downloaded - progress_bar.n
    progress_bar.update(progress_update)

def download_youtube(video_url):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    highest_res_stream = yt.streams.get_highest_resolution()
    global progress_bar
    progress_bar = tqdm(
        total=highest_res_stream.filesize,
        unit='B',
        unit_scale=True,
        desc=yt.title[:15]
    )
    highest_res_stream.download()
    progress_bar.close()
    print("✅ Download complete:", yt.title)

def download_spotify(spotify_url):
    print("🎵 Downloading from Spotify:", spotify_url)
    try:
        subprocess.run(["spotdl", spotify_url], check=True)
        print("✅ Spotify download complete!")
    except subprocess.CalledProcessError as e:
        print("❌ Error downloading from Spotify:", e)

def main():
    video_urls = []
    print("\n🎥 Enter YouTube/YouTube Music/Spotify URLs (Press Enter on a blank line when done):")
    while True:
        link = input("URL: ").strip()
        if not link:
            break
        video_urls.append(link)

    if not video_urls:
        print("⚠ No URLs provided.")
        return

    for link in video_urls:
        if "youtube.com" in link or "youtu.be" in link or "music.youtube.com" in link:
            try:
                download_youtube(link)
            except Exception as e:
                print("❌ Error downloading YouTube:", link, e)
        elif "spotify.com" in link:
            try:
                download_spotify(link)
            except Exception as e:
                print("❌ Error downloading Spotify:", link, e)
        else:
            print("⚠ Unsupported link:", link)

if __name__ == "__main__":
    main()