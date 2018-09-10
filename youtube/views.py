import youtube_dl
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from .forms import LinkForm
from .models import Link


def index(request):
    form = LinkForm()
    link_list = Link.objects.all()
    paginator = Paginator(link_list, 5)
    page = request.GET.get('page')

    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        links = paginator.page(1)
    except EmptyPage:
        links = paginator.page(paginator.num_pages)

    context = {
        'form': form,
        'links': links,
    }

    return render(request, 'youtube/index.html', context)

def download_video(request):
    form = LinkForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            youtubeUrl = request.POST.get('url')

            url = Link(url=youtubeUrl)
            url.save()

            options = {
                'outtmpl': '%(title)s-%(id)s.%(ext)s',
                'format': 'best'
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                r = ydl.extract_info(youtubeUrl, download=False)
                videoUrl = r['url']
            print(videoUrl)

            file_name = 'video.mp4'
            response = HttpResponsePermanentRedirect(videoUrl)
            response['Content-Type'] = 'application/force-download'
            response['Content-Disposition'] = 'attachment; filename=%s' % file_name

            return response
        else:
            print('Form is not valid!')
