from django.http import HttpResponse

def homePage(request):
    return HttpResponse("hi")


def contactUs(request):
    return HttpResponse("Phone No. : 6969696969, Address : New York, USA")


def aboutUs(request):
    return HttpResponse("very big corpo beheheh")