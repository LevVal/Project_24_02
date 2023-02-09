from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
#from django.template.defaultfilters import filesizeformat

def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get("a", '')
    b = request.GET.get("b", '')
    result = a + b
    context = {
        "a": a,
        "b": b,
        "result": result
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)

def user_forms(request: HttpRequest) -> HttpResponse:
    return render(request, 'requestdataapp/user-bio-form.html')

def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        file_size = fs.size(myfile.name)
        print("file_size: ", file_size)
        if file_size < 1000:
            filename = fs.save(myfile.name, myfile)
            print("filename: ", filename)
    return render(request, 'requestdataapp/file-upload.html')
