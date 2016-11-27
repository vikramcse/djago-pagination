from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from api.models import Customer


def index(request):
    return render(request, 'index.html')


def getlist(request):
    data = []
    customer_object = Customer.objects.all()

    for customer in customer_object:
        single_customer = {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'email': customer.email,
            'gender': customer.gender,
            'ip_address': customer.ip_address
        }

        data.append(single_customer)

    return JsonResponse({'data': data})


def get_list_with_django_pagination(request):
    data = []
    page_index = request.GET.get('pageIndex', None)
    page_size = 10
    customer_object = Customer.objects.all()

    if page_index is not None:
        paginator_object = Paginator(customer_object, page_size)

        try:
            obj = paginator_object.page(page_index)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            obj = paginator_object.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            obj = paginator_object.page(paginator_object.num_pages)

        for customer in obj:
            single_customer = {
                'id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'email': customer.email,
                'gender': customer.gender,
                'ip_address': customer.ip_address
            }

            data.append(single_customer)

        return JsonResponse({'data': data, 'count': paginator_object.count})
