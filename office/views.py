from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Appointee, Appointment
from django.utils import timesince, timezone


# Create your views here.
def home(request):
    # now = timezone.now()
    # diff = timesince.timesince()
    appoints = Appointment.objects.all()
    paginator = Paginator(appoints, 2) #10 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)

    template = 'office/home.html'
    context = {'posts': posts, 'page': page,}
    return render(request, template, context)

def details(request, pk):
    detail = get_object_or_404(Appointment, pk=pk)

    template = 'office/details.html'
    context = {'detail': detail}
    return render(request, template, context)

def profile(request):
    user = request.user
    profile_user = Appointee.objects.get(user=user)
    template = 'office/profile.html'
    context = {'profile': profile_user}
    return render(request, template, context)


def login(request):


    template = 'office/login.html'
    context = {}
    return render(request, template, context)
