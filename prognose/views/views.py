from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@login_required
def home(request):
    """
    Renders the home page.

    :param request: HttpRequest: Standard httprequest from Django
    :return: rendering of the page
    """
    assert isinstance(request, HttpRequest)

    return render(request,
                  'prognose/prognose.html',
                  {"title": "ETR Prediction"})


@login_required
def about(request):
    """
    Render an about page, which current no content
    :param request: HttpRequest: standard http request from Django
    :return: rendering of the page
    """
    return render(request,
                  'prognose/prognose.html',
                  {"title": "About"})

