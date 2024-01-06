from pytube import Playlist
from moviepy.editor import VideoFileClip, AudioFileClip
import os

url = str(input('Enter the url of playlist. Should be like this: (www.youtube.com/playlist?) :  ')) 
location = 'Downloads'
p = Playlist(url)
i=1
for videos in p.videos:
    try:
        print(f'Downloading {i}')
        out = videos.streams.first().download(location)
        new = out.replace('.mp4','.mp3')
        videofile = AudioFileClip(out)
        audiofile = videofile.write_audiofile(new)
        os.remove(out)
        print(f"{i} downloaded successfully")
        i+=1
    except:
        print(f'Error downloading{i}, Check your connection. Skipping download')
        
        

    
        
    