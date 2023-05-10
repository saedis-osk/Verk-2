from django.shortcuts import render
from home.models import PopularOffer
from home.forms.forms import OfferPopularCreateForm

# def index(request):
#     return render(request, 'home/index.html')

def popular_offers(request):
    if request.method == 'POST':
        form = OfferPopularCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            offer = form.save(commit=False)
            offer_image = request.FILES.get('image')
            if offer_image:
                offer.image = offer_image
            offer.save()
    offers = PopularOffer.objects.all()
    context = {'offers': offers}
    return render(request, 'home/index.html', context)

