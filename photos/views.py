from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
    if request.method == "POST":
        new_photo = Photo(
            file=request.FILES["img"]
        )  # name as defined by form in index.html
        new_photo.save()
        return render(
            request, "index.html", {"new_url": str(new_photo.file.url)}
        )
    else:
        return render(request, "index.html")

