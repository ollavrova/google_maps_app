from app.forms import CoordinatesForm
from app.models import Coordinates
from app.serializers import CoordinatesSerializer
from django.shortcuts import render
from google_maps_app.settings import APP_KEY
import googlemaps
from rest_framework import generics, permissions


def home(request):
    """
    view for home page
    :param request:
    :return: rendering page
    """
    data = Coordinates.objects.all().order_by('-created')[:50]
    form = CoordinatesForm()
    if request.method == 'POST':
        if 'address' in request.POST:
            form = CoordinatesForm(request.POST)
            if form.is_valid():
                address = form.cleaned_data['address']
                result = find_coord(address)
                if result:
                    c = Coordinates(address=address,
                                    lat=result['lat'],
                                    lng=result['lng'])
                    c.save()
                else:
                    result = 'Nothing found'

            return render(request, 'home.html', {'results': result,
                                                 'data': data,
                                                 'address': address,
                                                 'form': form})

    return render(request, 'home.html', {'data': data, 'form': form})


def find_coord(addr):
    """
    Function which looking for coordinates in googlemaps api by address
    :param addr:  string address for find coordinates
    :return: dict with coordinates (latitude and longitude)
    """
    gmaps = googlemaps.Client(key=APP_KEY)
    try:
        geocode_result = gmaps.geocode(addr)[0]['geometry']['location']
    except IndexError:
        geocode_result = {}
    return {'address': addr,
            'lat': geocode_result.get('lat'),
            'lng': geocode_result.get('lng')}


class CoordinatesList(generics.ListCreateAPIView):
    """
    API endpoint for list of coordinates
    """
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CoordinatesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for detail of coordinates
    """
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

coord_list = CoordinatesList.as_view()
coord_detail = CoordinatesDetail.as_view()
