from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import LinkForm
from .models import Link
from .tasks import convert


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
        'links': links
    }

    return render(request, 'mp3/index.html', context)


def download_mp3(request):
    form = LinkForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            url = request.POST['url']
            email = request.POST['email']

            convert.delay(url, email)

            url = Link(url=url)
            url.save()

            return render(request, 'mp3/index.html', {'form': form})
        return render(request, 'mp3/index.html', {'form': form})