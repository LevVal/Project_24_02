from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.files.storage import FileSystemStorage


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'requestdataapp/user-bio-form.html')


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        check_file_size(fs.size(myfile.name))

    return render(request, 'requestdataapp/file-upload.html')


def check_file_size(size: int) -> None:
    if size > 10:
        raise Exception("File too big")
