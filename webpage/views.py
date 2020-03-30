from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def portfolio_page(request):
    return render(request, '../portfolio/templates/portfolio/art_pieces.html')


def blog_page(request):
    return render(request, '../blog/templates/blog/post_list.html')
