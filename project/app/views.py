from django.shortcuts import render, redirect , get_object_or_404
from .forms import ImageUploadForm, SearchForm
from .models import Image
from django.db.models import Q
from django.contrib.auth.decorators import login_required , user_passes_test
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
# @user_passes_test(lambda u: u.is_staff)
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
            return redirect('image_detail', image.id)
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {'form': form})

def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'image_detail.html', {'image': image})

def search(request):
    form = SearchForm()
    query = request.GET.get('q')
    if query:
        images = Image.objects.filter(Q(caption__icontains=query) | Q(tags__name__icontains=query))
        paginator = Paginator(images, 10)
        page = request.GET.get('page')
        images = paginator.get_page(page)
    else:
        images = []
    return render(request, 'search_results.html', {'images': images, 'query': query, 'form': form})

