from django.shortcuts import render,redirect
from django.http import HttpResponse
from home_app.models import Menu,Order
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # print(request.method)
    return render(request, 'home_app/index.html')

def login(request):
    return render(request,'home_app/login.html')

@csrf_exempt
def checkout(request):
    print('========checkout=======>')
    if request.method == "POST":
        order_details  = dict(request.POST)
        order = Order(amount=float(order_details['total'][0]),address=order_details['address'][0],ordered_by=order_details['name'][0],account_name=request.user)
        order.save()
        user_orders = Order.objects.filter(account_name=request.user).values().order_by("-pk")
        print(user_orders)
        return render(request,'home_app/track.html',{'order_items':list(user_orders)})
        # print('saved !!!')
        # return HttpResponse("<h1>Saved</h1>")
        # return redirect("track_order/")
    # if request.method == "GET":
    #     return redirect("menu/")

def track_order(request):
    user_orders=[]
    if request.method == "GET":
        if request.user.is_authenticated:
            print("=======track_order==GET===")
            user_orders = Order.objects.filter(account_name=request.user).values().order_by("-pk")
            print(user_orders)
    return render(request,'home_app/track.html',{'order_items':list(user_orders)})

@csrf_exempt
def menu(request):
    if request.method == "GET":
        menu_items = Menu.objects.all().values()

        return render(request,'home_app/menu.html',{'menu_items':list(menu_items)})    
    elif request.method == "POST":
        print("=======MENU==POST===")
        bill = []
        items_quantity_array  = dict(request.POST)
        food_items = list(items_quantity_array.keys())
        billing_info = Menu.objects.filter(pk__in=food_items)
        total = 0 
        for row in billing_info:
            bill_row = {}
            bill_row['item_name'] =  row.name
            bill_row['item_qty'] =  int(items_quantity_array[str(row.pk)][0])
            bill_row['unit_price'] = float(row.price)
            bill_row['amount'] = round(bill_row['item_qty'] * float(row.price),2)
            total  += bill_row['amount']
            bill.append(bill_row)
        print(bill)    
        print(total)    
        return render(request,'home_app/checkout.html',{'bill':bill,'total':round(total,2)})  
