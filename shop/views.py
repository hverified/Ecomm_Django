from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json


def shopIndexView(request):
    # context = {
    #     'no_of_slides': nSlides,
    #     'n_range': range(1, nSlides),
    #     'product': products
    # }
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    allProds = []
    prodCats = Product.objects.values('category', 'id')
    cats = sorted({item['category'] for item in prodCats})
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - n // 4)
        allProds.append([prod, range(1, nSlides), nSlides])

    context = {'allProds': allProds}

    return render(request, "shop/index.html", context)


def aboutView(request):

    return render(request, "shop/about.html")


def contactView(request):

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')

        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
        contacted = True
        return render(request, "shop/contact.html", {'contacted': contacted, 'name': name})

    return render(request, "shop/contact.html")


def trackerView(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=order_id, email=email)
            if len(order):
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                HttpResponse('error')
        except Exception as e:
            return HttpResponse('error')

    return render(request, "shop/tracker.html")


def searchView(request):

    return render(request, "shop/search.html")


def productView(request, pid):
    # Fetching products using product id
    prod = Product.objects.filter(id=pid)
    # print(prod)

    return render(request, "shop/prodView.html", {'product': prod[0]})


def checkoutView(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json, name=name, email=email, address=address,
                       city=city, state=state, pincode=pincode, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc='The Order has been placed.')
        update.save()
        thank = True
        id = order.order_id
        return render(request, "shop/checkout.html", {'thank': thank, 'id': id})

    return render(request, "shop/checkout.html")
