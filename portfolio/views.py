from django.shortcuts import render
from django.utils import timezone
from .models import Piece


def post_list(request):
    pieces = Piece.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'portfolio.html', {'pieces': pieces})
