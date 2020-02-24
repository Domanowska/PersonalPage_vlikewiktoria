from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def gallery_page(request):
    return render(request, 'gallery.html')


def blog_page(request):
    return render(request, '../blog/templates/blog/post_list.html')
