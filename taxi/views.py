from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    paginate_by = 5
    queryset = Manufacturer.objects.order_by("name")
    template_name = "templates/taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    template_name = "templates/taxi/car_list.html"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
