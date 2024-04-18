from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# 자신이 판매하는 상품 리스트를 보여주기
# ->> 전체 Food에서 특정 user(판매자)인 food만 가져온다
# ->> 전체 Food에서 내가 올린 food만 filter한다.
# 상품 들록 기능

# Create your views here.
# def seller_index(request):
#     food = Food.objects.all().filter(user__id=request.user.id)
#     context = {
#         'object_list': food
#     }
#     return render(request, 'seller/seller_index.html', context)

# login_required 로그인이 필요한 뷰에 달아주면 로그인이 필요하다
@login_required
def seller_index(request):
    food = Food.objects.all().filter(user__id=request.user.id)
    context = {
        'object_list': food
    }
    return render(request, 'seller/seller_index.html', context)

def add_food(request):
    # get
    if request.method=='GET':
        return render(request, 'seller/seller_add_food.html') 
    
    # post
    elif request.method=='POST':
        # 폼에서 전달되는 각 값을 뽑아와서  DB에 저장
        user = request.user
        food_name = request.POST['name']
        food_price = request.POST['price']
        food_description = request.POST['description']
        
        # food_name, price, description
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        Food.objects.create(user= user, name=food_name, price= food_price, description=food_description, image_url=url)
         
        return render(request, 'seller/seller_index.html')
    

  

# 옛날방식
def show_add_food():pass
def save_added_food():pass

@login_required
def food_detail(request,pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object' : object
    }
    return render(request, 'seller/food_detail.html', context)

@login_required
def food_delete(request,pk):
    object = Food.objects.get(pk=pk)
    object.delete()  
    return redirect('seller:seller_index')
