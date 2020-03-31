from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Piece


def post_list(request):
    pieces = Piece.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'portfolio/art_pieces.html', {'pieces': pieces})


def piece_detail(request, pk):
    piece = get_object_or_404(Piece, pk=pk)
    return render(request, 'portfolio/piece_detail.html', {'piece': piece})
