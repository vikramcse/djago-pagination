from django.http import HttpResponse
import json

from api.models import Customer


def getlist(request):
    resp = []
    customer_object = Customer.objects.all()

    for customer in customer_object:
        single_customer = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'email': customer.email,
            'gender': customer.gender,
            'ip_address': customer.ip_address
        }

        resp.append(single_customer)

    return HttpResponse(json.dumps(resp))
