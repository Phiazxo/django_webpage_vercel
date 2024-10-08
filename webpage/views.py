from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def indexPage(request):
    return render(request, "index.html")

def aboutPage(request):
    return render(request, "about.html")

def contactPage(request):
    return render(request, 'contact.html')


def forPage(request):
    context = {}
    lt = list(range(1, 101))

    first_names = ["Mark", "Jacob", "Larry", "John", "Jane", "Alice", "Bob", "Charlie", "David", "Emily"]
    last_names = ["Otto", "Thornton", "the Bird", "Smith", "Doe", "Johnson", "Brown", "Williams", "Jones", "Miller"]
    handles = ["@Mark", "@Jacob", "@Larry", "@John", "@Jane", "@Alice", "@Bob", "@Charlie", "@David", "@Emily"]

    data = []
    for i in lt:
        first_name = first_names[(i - 1) % len(first_names)]
        last_name = last_names[(i - 1) % len(last_names)]
        handle = handles[(i - 1) % len(handles)]
        data.append({
            "id": i,
            "first_name": first_name,
            "last_name": last_name,
            "handle": handle
        })

    context["list"] = data

    return render(request, 'for_test.html', context)

def cardPage(request):
    cards = []
    base_url = 'https://images.pexels.com/photos/12475794/pexels-photo-12475794.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    
    for i in range(1, 101):
        image_url = f'{base_url}&{i}'
        card = {
            'image_url': image_url,
            'title': f'Card Dogs {i}',
            'link': f'#card-{i}'
        }
        cards.append(card)

    context = {
        'cards': cards
    }
    return render(request, 'card.html', context)

def cardcolorPage(request):
    context = {
        'color': 'All',
    }

    if request.method == "GET" and request.GET.get('color') != None:
        context['color'] = request.GET.get('color')

    return render(request, 'card_color.html', context)

def formPage(request):
    return render(request, 'form.html')

@csrf_exempt
def submit_registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # ทำการบันทึกข้อมูลลงฐานข้อมูลหรือประมวลผลตามต้องการ
        # ตัวอย่างการตอบกลับ
        return JsonResponse({'status': 'success', 'message': 'บันทึกข้อมูลเรียบร้อยแล้ว'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def detallPage(request):
    return render(request, "detall.html")

def buttonsPage(request):
    return render(request, "buttons.html")

def cardsPage(request):
    return render(request, "cards.html")

def colorsPage(request):
    return render(request, "colors.html")

def bordersPage(request):
    return render(request, "borders.html")

def animationsPage(request):
    return render(request, "animations.html")

def otherPage(request):
    return render(request, "other.html")

def loginPage(request):
    return render(request, "login.html")

def registerPage(request):
    return render(request, "register.html")

def forgot_passwordPage(request):
    return render(request, "forgot_password.html")

def errorPage(request):
    return render(request, "404_page.html")

def blankPage(request):
    return render(request, "blank_page.html")

def chartsPage(request):
    return render(request, "charts.html")

def tablesPage(request):
    return render(request, "tables.html")