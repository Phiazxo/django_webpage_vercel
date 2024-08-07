from django.shortcuts import render

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
    base_url = 'https://static.wikia.nocookie.net/ultra/images/4/4d/EMI_104.png/revision/latest/thumbnail/width/360/height/360?cb=20240615095817'
    
    for i in range(1, 101):
        image_url = f'{base_url}&{i}'
        card = {
            'image_url': image_url,
            'title': f'Card Emi {i}',
            'description': f'Emi (エミ, Emi) is a Gigantron hatchling and later the foster child of Ultraman/Ken Sato, who attempts to protect her from the machinations of the conniving KDF in Ultraman: Rising.',
            'link': f'#card-{i}'
        }
        cards.append(card)

    context = {
        'cards': cards
    }
    return render(request, 'card.html', context)
