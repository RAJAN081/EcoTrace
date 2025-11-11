# # locator/views.py
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import EwasteLocation

# def home(request):
#     return render(request, 'core/home.html')

# def find_facility(request):
#     return render(request, 'core/find_facility.html')

# def awareness(request):
#     return render(request, 'core/awareness.html')

# def locator(request):
#     return render(request, "core/locator.html")

# def locator_detail(request, pk):
#     loc = get_object_or_404(EwasteLocation, pk=pk)
#     return render(request, 'core/detail.html', {'loc': loc})

# def api_locations(request):
#     qs = EwasteLocation.objects.all()
#     data = []
#     for loc in qs:
#         data.append({
#             'id': loc.id,
#             'name': loc.name,
#             'address': loc.address,
#             'city': loc.city,
#             'state': loc.state,
#             'lat': float(loc.latitude),
#             'lng': float(loc.longitude),
#             'accepted_items': loc.accepted_items,
#             'timings': loc.timings,
#             'contact': loc.contact,
#         })
#     return JsonResponse({'locations': data})


# locator/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import EwasteLocation

def api_locations(request):
    qs = EwasteLocation.objects.all()
    data = []
    for loc in qs:
        data.append({
            'id': loc.id,
            'name': loc.name,
            'address': loc.address,
            'city': loc.city,
            'state': loc.state,
            'lat': float(loc.latitude),
            'lng': float(loc.longitude),
            'accepted_items': loc.accepted_items,
            'timings': loc.timings,
            'contact': loc.contact,
        })
    return JsonResponse(data, safe=False)

def locator(request):
    # main locator page (map + sidebar + detail pane)
    return render(request, "core/locator.html")

def locator_detail(request, id):
    loc = get_object_or_404(EwasteLocation, pk=id)
    return render(request, "core/locator_detail.html", {"loc": loc})

# small view stubs used by urls.py - keep previous behavior for other pages
def home(request):
    return render(request, "core/home.html")

def find_facility(request):
    return render(request, "core/find_facility.html")

def awareness(request):
    return render(request, "core/awareness.html")
