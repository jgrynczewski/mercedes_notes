from django.shortcuts import render


# Create your views here.
def first_view(request):
    return render(
        request,
        'inheritance/first.html'
    )


def second_view(request):
    return render(
        request,
        'inheritance/second.html'
    )