import youtube_dl
import requests
import json
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task(name='convert')
def convert(url, email):

    ydl_opts = {
        'extractaudio': True,
        'audioformat': "mp3",
        'outtmpl': settings.MEDIA_ROOT + '/mp3/%(id)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    playlist_id = url.rsplit('=', 1)[-1]
    youtube_api_key = 'э нэт токена'
    youtube_uri = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={}&fields=items&key={}'
    format_youtube_uri = youtube_uri.format(playlist_id, youtube_api_key)
    content = requests.get(format_youtube_uri).text
    data = json.loads(content)

    video_list = []

    for item in data.get('items'):
        video_id = item['snippet']['resourceId']['videoId']

        if id:
            youtube_item_url = 'https://www.youtube.com/watch?v='
            video_item = youtube_item_url + video_id
            video_list.append(video_item)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(video_list)

        video_id = ''.join(video_list).rsplit('=', 1)[-1]

        generated_mp3 = '{domain}{path}{filename}{format}'.format(
            domain='http://127.0.0.1:8000',
            path=settings.MEDIA_URL+'mp3/',
            filename=video_id,
            format='.mp3'
        )

        list_mp3 = []
        list_mp3.append(generated_mp3)

        title = 'Скачивание MP3'

        message = '''
            Вы скачали MP3 из этого видео - %s
            ссылка на скачивание MP3 - %s
        ''' % (url, list_mp3)

        send_mail(title, message, settings.EMAIL_HOST_USER, [email])