from django.shortcuts import render,redirect
from seller.models import Food
from .models import Cart
from django.db.models import Sum
# from django.contrib.auth

# Create your views here.
def order_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object' : object
    }

    return render(request, 'order/order_detail.html', context)

def cart(request,pk):
    object_list = Food.objects.all().filter(user__id=request.user.id)
    context = {
        'object': object_list
    }
    return render(request, 'order/cart.html', context)




def add_cart(request):
    food_id = request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # 이전에 해당 음식에 대한 장바구니 정보가 있으면 get(food=food)
    # 없으면 새로 생성해서 적용
    try:
        cart = Cart.objects.get(user=request.user, food=food)
    except:
        cart = Cart.objects.create(user=request.user, food=food, amount=0)
    finally:
        pass
    cart.amount+=1
    cart.save()
    context = {
        'object': food
    }
    return render(request, 'order/cart.html', context)

def cart_delete(request,pk):    
    food = Food.objects.get(pk=pk)
    food.delete()
    return redirect('index')

def cart_remove(request,pk):    
    food_id = request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    cart, _ = Cart.objects.get_or_create(food=food)
    cart.amount-=1
    cart.save()
    context = {
        'object':food
    }
    return redirect(request, 'order/order_detail.html', context)

from django.http import JsonResponse
def modify_cart(request):
    # 어떤 음식(food_id)에 amount를 amountChange만큼 변경하고 
    # A사용자가 카트에 담은 B음식에 대해서 수량을 조정
    # 응답: 새롭게 변경된 수량, 전체 카트 음식 수량

    # 어떤 음식?
    user=request.user
    food_id = request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    # 카트 정보
    cart, _ = Cart.objects.get_or_create(user=user, food=food)
    cart.amount+=int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()
    
    # 유저가 주문한 전체 음식 개수
    # Question - Choice
    # 이 문제에 대한 초이스
    # question.choice_set
    totalQuantity = user.cart_set.aggregate(totalcount=Sum('amount'))['totalcount']
    # 변경된 최종 결과를 반환(JSON)
    context = {
        'newQuantity':cart.amount,
        'totalQuantity':totalQuantity,
        'message':'수량이 성공적으로 업데이트 되었습니다.',
        'success':True
    }
    return JsonResponse(context)
    # request.POST : <QueryDict: {'foodid': ['7'], 'amountCahnge': ['1']}>