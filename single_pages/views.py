from django.shortcuts import render

# Create your views here.
def main(request):
    return render(
        request,
        'single_pages/main.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )