from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
from pages.eeg import magic


def home_view(request, *args, **kwargs): # *args, **kwargs
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        imagesTable = magic(filename)

        return render(request, 'images.html', {
            'scan1': imagesTable[1], 'scan2':imagesTable[0], 'scan3': imagesTable[2], 'scan4':imagesTable[3], 'scan5':imagesTable[4]
        })
    return render(request, "home.html", {})


