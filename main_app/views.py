from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)

from .models import (
    Customer,
    Purchase
)
# Create your views here.
def index(request):
    data = Customer.objects.all()
    context = {
        'title': 'Customer List',
        'data': data,
    }
    return render(request, 'main_app/index.html', context)

def open_customer(request, uid):
    data = Customer.objects.get(uid=uid)
    context = {
        'title': f'{data.full_name}',
        'data': data,
    }
    return render(request, 'main_app/open_customer.html', context)

@csrf_exempt
def add_record(request, uid):
    data = Customer.objects.get(uid=uid)
    if request.method == 'POST':
        jsn_data = json.loads(request.body)
        table_data = jsn_data.get('table_data', [])
        for row in table_data:
            item_name = row.get('item_name', [])
            item_qnty = row.get('item_qnty', [])
            item_price = row.get('item_price', [])
            entry = Purchase(
                customer=data,
                item_name=item_name,
                item_qnty=int(item_qnty) if item_qnty else 0,
                item_price=int(item_price) if item_price else 0,
            )
            entry.save()
    context = {
        'title': f'{data.full_name} | Add new purchase record',
        'data': data,
    }
    return render(request, 'main_app/add_new_record.html', context)