from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
@login_required()
def profile_info(request):
    user_profile = User.objects.get(username=request.user)
    context = {
        'user_info': user_profile,
    }
    return render(request, 'profiles/profile.html', context)

