from django.shortcuts import render, get_object_or_404, redirect
from .models import Elon, SubscribedUser, UserDetail, ContactMessage
from .forms import SubscribeForm, ElonlarForm, UserUpdate, ProfileUpdate
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from blog_post.models import Post
from django.views.generic import DetailView, ListView, TemplateView
from blog_post.models import Post
# from django.contrib.auth.models import User

# Create your views here.

def index(request):
    user = User.objects.all()
    posts = Post.objects.all()
    elonlar = Elon.objects.all()
    elon = Elon.objects.order_by('-sana','-vaqt')[:3]
    context = {
                'elon':elon,    
                'user':user,
                'elonlar':elonlar,
                'posts':posts
                }
    return render(request, 'index.html', context)

def agents(request):
    users = User.objects.all()
    return render(request, 'agents.html',{'users':users})

#agentlar bergan elonlarni saralab olish
class AgentDetailView(DetailView):
    model = User
    template_name = 'agents_properties.html'
    def get(self, request, id):
        elonlar = Elon.objects.filter(author = id)
        agent = User.objects.get(pk=id)

        elonlar_list = Elon.objects.filter(author=id).order_by('-sana')
        page = request.GET.get('page',1)
        paginator = Paginator(elonlar_list,6)
        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            announcements = paginator.page(1)
        except EmptyPage:
            announcements = paginator.page(paginator,num_pages)
        return render(self.request, self.template_name,{'announcements':announcements})



@login_required
def profile(request):
    if request.method == 'POST':    
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.userdetail)

        if u_form.is_valid() and p_form.is_valid():
            print()
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.userdetail)
    return render(request, 'accounts/profile.html',{'u_form':u_form,'p_form':p_form})

@login_required
def oneannouncement(request, blog_id):
    elon = get_object_or_404(Elon, pk=blog_id)
    return render(request, "announcement/oneannouncement.html", {'elon': elon})


@login_required
def edit_announcement(request,blog_id):
    elon = get_object_or_404(Elon, pk=blog_id)
    form = ElonlarForm(instance=elon)
    
    if request.method == 'POST':

        form = ElonlarForm(request.POST, request.FILES, instance=elon)
        
        if form.is_valid():
            form.save()
            return redirect('/oneannouncement/')
    context = {'form': form}
    return render(request, 'announcement/update.html', context)

@login_required
def delete_announcement(request, blog_id):
    elon = get_object_or_404(Elon, pk=blog_id)
    if request.method == "POST":
        elon.delete()
        return redirect('index')



@login_required
def oneannouncement(request, blog_id):
    elon = get_object_or_404(Elon, pk=blog_id)
    return render(request, "announcement/oneannouncement.html", {'elon': elon})

# @login_required
# def edit_announcement(request, blog_id):
#     if request.method == "GET":
#         elon = Elon.objects.get(pk=blog_id)
#         return render(request, "announcement/update.html", {'elon': elon})
#     else:
#         elon = Elon.objects.get(pk=blog_id)
#         form = ElonlarForm(request.POST, request.FILES, instance=elon)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

def edit_announcement(request,blog_id):
    elon = get_object_or_404(Elon, pk=blog_id, author=request.user)
    form = ElonlarForm(instance=elon)
    
    if request.method == 'POST':

        form = ElonlarForm(request.POST, request.FILES, instance=elon)
        
        if form.is_valid():
            form.save()
            return redirect('/oneannouncement/')
    context = {'form': form}
    return render(request, 'announcement/update.html', context)


def delete_announcement(request, blog_id):
    elon = get_object_or_404(Elon, pk=blog_id, author=request.user)
    if request.method == "POST":
        elon.delete()
        return redirect('index')

# def add(request):
#     if request.method == "POST" or request.FILES:
#         form = ElonlarForm(request.POST, request.FILES)
#         if form.is_valid():
#             # form.save()
#             rasm111 = request.FILES.get('rasm1')
#             metall = request.POST['metall']
#             eskiNarx = request.POST['eskiNarx']
#             hozirgiNarx = request.POST['hozirgiNarx']
#             m2 = request.POST['m2']
#             rasm2 = request.FILES.getlist('rasm2')
#             rasm3 = request.FILES.getlist('rasm3')
#             qushimcha = request.POST['qushimcha']
#             sana = request.POST['sana']
        

#         new_form = ElonlarForm(
#             rasm1=rasm111, 
#             metall=metall, 
#             eskiNarx=eskiNarx, 
#             hozirgiNarx=hozirgiNarx, 
#             m2=m2, rasm2=rasm2,
#             rasm3=rasm3, 
#             qushimcha=qushimcha, sana=sana,
#             )
#         print(form,'ooooooooooooooooooooooooooooooooooooo')
#         # new_form.save()
#         new_form1 = new_form.save(commit=False)
#         new_form1.author=request.user
#         new_form1.save()
#         # return redirect('index')
#         return render(request, 'agents.html', {'form':ElonlarForm()})
#     else:
#         return render(request, 'agents.html', {'form':ElonlarForm()})
        


def about(request):
    user = User.objects.all()
    elonlar = Elon.objects.all()
    posts = Post.objects.all()
    context = {
        'user':user,
        'elonlar':elonlar,
        'posts':posts
        }
    return render(request, 'about-us.html', context)

def properties(request):
    elonlar = Elon.objects.all().order_by('-sana','-vaqt')
    pgn = Paginator(elonlar, 6)
    page_nums = request.GET.get('page',1)
    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)
    return render(request, 'properties.html',{'elonlar':page})

def elonFilter(request):
    qs = Elon.objects.all()
    title_contains = request.GET.get('title_contains')
    print(title_contains)
    return render(request, 'index.uz')



def elements(request):
    return render(request, 'elements.html')



def contact(request):
    return render(request, 'contact.html')


def base(request):

    if request.method == 'POST':
        email = request.POST['subscribe']        

        send_mail(
            'Yangi xabar',
            'saytdan ' + ' ' + email + ' ro`yxatdan o`tdi',
            settings.EMAIL_HOST_USER,
            ['sardorbek.uktamov.1@mail.ru'],
            fail_silently=False
        )
        subscribed_user = SubscribedUser(email=email)
        subscribed_user.save()
        subscribed = SubscribedUser(email=email)
        return render(request, 'base.html', {'form':subscribed})
    else:
        subscribed = SubscribedUser(email=email)
        return render(request, 'base.html', {'form':subscribed})

#contact qismidan xabar yuborish
def sendmail(request):
    
    if request.method == "POST":
        name       = request.POST['name']
        email      = request.POST['email']
        subject    = request.POST['subject']
        message    = request.POST['message']
        msg = 'Sizga ***** saytidan '+ name +' xabar yubordi. '+ '\n' + 'elektron pochtasi: ' + email + '\n' + 'xabar maqsadi: '+ subject + '\n' + 'xabar mazmuni: '+'\n'+message
        send_mail(
            'Yangi xabar',
            msg,
            settings.EMAIL_HOST_USER,   #xabar jo`natuvchi elektron pochta
            ['sardorbek.uktamov.1@mail.ru'], #xabar keluvchi elektron pochta
            fail_silently=False,
        )

        contact_user = ContactMessage(
            full_name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact_user.save()
        messages.info(request,"Xabaringiz muvoffaqiyatli yuborildi! Tez orada elektron pochtangizga javob olasiz.")
        return redirect('contact')
    else:
        messages.info(request,"Xabaringiz yuborilmadi! iltimos qaytadan urunib ko'ring. ")
        
        return redirect('services')
