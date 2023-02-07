import requests
import re
import json
import subprocess

url = 'https://api.bilibili.com/x/player/playurl?qn=32&fnver=0&fnval=4048&fourk=1&voice_balance=1&avid=474270699&bvid=BV1SK411S7K9&cid=869586483'
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
response = requests.get(url=url, headers=headers)
json_data = json.loads(response.text)

audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]

file_name = "demo"
works_name = "requests_video.mp4"
video_name = file_name+".mp4"
audio_name = file_name+".mp3"

audio_url_response = requests.get(url=audio_url, headers=headers)
audio_data = audio_url_response.content
with open(audio_name, mode='wb') as f:
    f.write(audio_data)

video_url_response = requests.get(url=video_url, headers=headers)
video_data = video_url_response.content
with open(video_name, mode='wb') as f:
    f.write(video_data)

audio_url_response.close()
video_url_response.close()

cmd = f'ffmpeg -i {video_name} -i {audio_name} -acodec copy -vcodec copy {works_name}'
subprocess.call(cmd,shell=True)
print('完成')