from django.shortcuts import render, redirect, get_object_or_404
from sotuvapp.models import Elon
from django.contrib.auth.models import User
from .forms import ElonForm
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required




def index(request, username):
    user = User.objects.filter(username=username)
    elonlar1 = Elon.objects.filter(author=request.user).order_by('-sana','-vaqt')
    pgn = Paginator(elonlar1, 6)
    page_nums = request.GET.get('page',1)
    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)
    return render(request, "accounts/personal_area.html", {'elonlar': page, 'user': user})

# def oneannouncement(request, blog_id):
#     elon = get_object_or_404(Elon, pk=blog_id)
#     return render(request, "accounts/oneannouncement.html", {'elon': elon})


@login_required
def add_announcement(request, username):
    if request.user.is_staff:
        metal = Elon.objects.all()
        if request.method == "POST" and request.FILES:
            rasm1       = request.FILES.get('rasm1')
            eskiNarx    = request.POST['eskiNarx']
            hozirgiNarx = request.POST['hozirgiNarx']
            m2          = request.POST['m2']
            qushimcha   = request.POST['qushimcha']
            rasm2       = request.FILES.get('rasm2')
            rasm3       = request.FILES.get('rasm3')
            metall      = request.POST['metall']
            time        = request.POST['time']

            elonlar = Elon(
                rasm1 = rasm1,
                eskiNarx = eskiNarx,
                hozirgiNarx = hozirgiNarx,
                m2 = m2,
                qushimcha = qushimcha,
                rasm2 = rasm2,
                rasm3 = rasm3,
                metall = metall,
                sana = time,
                author = request.user            
            )

            elonlar.save()
            return redirect('index')
        else:
            if len(request.user.groups.filter(name="Admin")) != 0:
                return render(request, 'announcement/add_announcement.html', {'form':ElonForm(), 'metal':metal})
            return redirect('/')
    else:
        return HttpResponse("<h1>Siz mumkin bo'lmagan sahifaga kirishga urindingiz !!!</h1>") 
