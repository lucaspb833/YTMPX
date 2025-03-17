# **YTMPX - YouTube & Spotify Downloader**  

![GitHub repo size](https://img.shields.io/github/repo-size/Anshkabra2012/YTMPX)  
![GitHub last commit](https://img.shields.io/github/last-commit/Anshkabra2012/YTMPX)  
![GitHub stars](https://img.shields.io/github/stars/Anshkabra2012/YTMPX?style=social)  
![GitHub forks](https://img.shields.io/github/forks/Anshkabra2012/YTMPX?style=social)  

## **Overview**  
YTMPX is a command-line tool that allows you to download videos, music, and playlists from YouTube and Spotify. It ensures high-quality downloads while supporting bulk input for an efficient experience.  

## **Features**  
- Download videos in the highest available resolution from YouTube  
- Convert and download music from YouTube Music  
- Fetch high-quality audio from Spotify  
- Bulk download support  
- Progress bars for real-time updates  
- Automatic format selection based on the input link  

## **Installation**  

Make sure you have Python installed. Then, run:  

```
pip install pytubefix tqdm spotdl
```

To ensure smooth Spotify downloads, install FFmpeg:  

```
spotdl --download-ffmpeg
```

## **Usage**  

Run the script using:  

```
python downloader.py
```

Paste YouTube, YouTube Music, or Spotify links, one per line. Press enter on a blank line to start downloading.  

## **Example**  

```
python downloader.py
```

```
Enter YouTube or Spotify URLs (Press Enter on a blank line when done):
URL: https://www.youtube.com/watch?v=example1
URL: https://open.spotify.com/track/example2
URL: 

Downloading: Video Title (YouTube)
[#########----------------] 45% 

Downloading: Song Title (Spotify)
[########################] 100%
```

## **Supported Links**  
- YouTube videos and playlists  
- YouTube Music links  
- Spotify tracks, albums, and playlists  

## **Dependencies**  
- `pytubefix` (for YouTube downloads)  
- `spotdl` (for Spotify downloads)  
- `tqdm` (for progress bars)  
- `ffmpeg` (for audio conversion)  

## **Troubleshooting**  
If Spotify downloads fail due to FFmpeg, ensure it is installed correctly:  

```
spotdl --download-ffmpeg
```

If YouTube videos do not download, upgrade `pytubefix`:  

```
pip install --upgrade pytubefix
```

## **Contributing**  
Fork the repository, make improvements, and submit a pull request.  

## **License**  
This project is licensed under the Unlicense.  

## **Credits**  
Developed by Ansh Kabra.  
