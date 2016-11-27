from django.http import JsonResponse

from api.models import Customer


def getlist(request):
    data = []
    customer_object = Customer.objects.all()

    for customer in customer_object:
        single_customer = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'email': customer.email,
            'gender': customer.gender,
            'ip_address': customer.ip_address
        }

        data.append(single_customer)

    return JsonResponse({'data': data})
