from django.forms import modelformset_factory
from .models import Gallery, Image
from .forms import ImageForm, GalleryForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def add_gallery_view(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

    if request.method == "GET":
        gallery_form = GalleryForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'index.html', {"gallery_form":gallery_form, "formset":formset})
    elif request.method == "POST":
        pass
    elif request.method == "POST":
        gallery_form = GalleryForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if gallery_form.is_valid() and formset.is_valid():
            gallery_obj = gallery_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(image=image, gallery=gallery_obj)
            return HttpResponseRedirect('/')
        else:
            print(gallery_form.errors, formset.errors)

def gallery_view(request, pk):
    gallery = Gallery.objects.get(id=pk)
    return render(request, 'gallery.html', {"gallery":gallery})

