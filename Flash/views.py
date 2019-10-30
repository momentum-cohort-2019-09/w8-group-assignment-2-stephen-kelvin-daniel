# from django.shortcuts import render



from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def testing(request):
    return render(request, 'Flash/testing.html')

def dashboard(request):
    return render(request, 'Flash/dashboard.html')

# @ login_required
# def index_views(request):
#     user = request.user
#     return render(request, "Flash/index.html", {"user": user})

