# import pysrt
# import pydub
# from gtts import gTTS
# from moviepy.editor import *
from pytube import YouTube

# Download the video
link = "https://www.youtube.com/watch?v=cHarsV6XSqQ"
yt = YouTube(link)
yt.streams.filter(subtype='mp4').first().download("./")

# Download the english subtitles
# caption_tracks = yt.captions.all()
# for track in caption_tracks:
#     if track.code == 'en':
#         track.download()
#         break

# # Translate the english subtitles to chinese
# subs = pysrt.open('original_subtitle.srt')
# for i in range(len(subs)):
#     subs[i].text = translate(subs[i].text, 'en', 'zh-cn')
# subs.save('translated_subtitle.srt', encoding='utf-8')

# # Overlay the chinese subtitles on the video
# video = VideoFileClip("original_video.mp4")
# subtitle = SubtitleClip("translated_subtitle.srt", video.fps)
# final_video = CompositeVideoClip([video, subtitle.set_pos(("center", "bottom"))])
# final_video.write_videofile("final_video.mp4")
# from douyin_uploader import DouyinUploader

# uploader = DouyinUploader(username='your_username', password='your_password')
# uploader.login()
# uploader.upload_video(video_path='path_to_your_video', caption='your_caption')