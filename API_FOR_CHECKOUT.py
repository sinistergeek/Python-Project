from django.shortcuts import render
import requests
import base64
import json
from datetime import datetime


tokens = '{{APPLICATION_TOKEN}}:{{ADMIN_ACCESS_TOKEN}}'
encoded = base64.b64encode(tokens.encode('ascii'))
headers = {
     'Content-Type': 'application/json',
     'Authorization': 'Basic ' + encoded.decode('utf-8')
}

def getCardCredentials(token):
    url = '{{BASE_URL}}cards/' + token + '/showpan?show_cvv_number=true'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        res = json.loads(response.text)
        return res['pan'], res['cvv_number']
    
    return "", ""

def getLists(response):
    isSuccess = False
    data = ''
    count = 0
    message = 'Server error!'
    if response.status_code == 200:
        data = json.loads(response.text)['data']
        count = json.loads(response.text)['count']
        isSuccess = True
    elif response.status_code == 400:
        message = 'Bad request!'

    return isSuccess, message, data, count

def getResponse(response):
    isSuccess = False
    message = 'Server error!'
    if response.status_code == 201:
        isSuccess = True
        message = 'Request processed successfully!'
    elif response.status_code == 400:
        message = 'User input error / Bad request!'
    elif response.status_code == 409:
        message = 'Request already processed with a different payload!'
    elif response.status_code == 412:
        message = 'Pre-condition setup issue!'
    
    return isSuccess, message

def dashboard(request):
    return render(request, 'administrator/dashboard.html')

def listUsers(request):
    url = '{{BASE_URL}}users'
    response = requests.get(url, headers=headers)
    
    isSuccess, message, data, count = getLists(response)
    
    allUsers = []

    if isSuccess:
        for user in data:
            tempUser = dict()
            tempUser['token'] = user['token']
            tempUser['full_name'] = user['first_name'] + ' ' + user['last_name']
            tempUser['created_date'] = datetime.strptime(user['created_time'], "%Y-%m-%dT%H:%M:%SZ").date()
            tempUser['status'] = user['status']
            allUsers.append(tempUser)

    return render(request,'administrator/listUsers.html', {'users': allUsers, 'isSuccess': isSuccess, 'message': message, 'count': count})

def createUser(request):
    if request.method == 'POST':
        url = '{{BASE_URL}}users'

        data = json.dumps({
            "first_name": request.POST.get("firstName"),
            "last_name": request.POST.get("lastName"),
            "gender": request.POST.get("gender"),
            "email": request.POST.get("email"),
            "address1": request.POST.get("address"),
            "city": request.POST.get("city"),
            "state": request.POST.get("state"),
            "postal_code": request.POST.get("postalCode"),
            "country": request.POST.get("country"),
            "phone": request.POST.get("phone"),
            "birth_date": request.POST.get("dateOfBirth")
        })

        response = requests.post(url, headers=headers, data=data)

        isSuccess, message = getResponse(response)

        return render(request,'administrator/createUser.html', {'isSuccess': isSuccess, 'message': message})

    return render(request, 'administrator/createUser.html')

def listCards(request):
    if request.method == 'POST':
        url = '{{BASE_URL}}cards/user/' + request.POST.get("userToken")
        
        response = requests.get(url, headers=headers)
        
        isSuccess, message, data, count = getLists(response)
        
        allCards = []

        if isSuccess:
            for card in data:
                tempCard = dict()
                tempCard['card_product_token'] = card['card_product_token']
                tempCard['token'] = card['token']
                tempCard['expiry_date'] = datetime.strptime(card['expiration_time'], "%Y-%m-%dT%H:%M:%SZ").date()
                tempCard['state'] = card['state']
                tempCard['pan'], tempCard['cvv_number'] = getCardCredentials(card['token'])
                allCards.append(tempCard)

        return render(request,'administrator/listCards.html', {'cards': allCards, 'isSuccess': isSuccess, 'message': message, 'count': count})

    return render(request, 'administrator/listCards.html', {'userTokens': getUserTokens()})

def createCard(request):
    if request.method == 'POST':
        url = '{{BASE_URL}}cards?show_cvv_number=' + str(request.POST.get("showCVV")) + '&show_pan='+ str(request.POST.get("showPAN"))

        data = json.dumps({
            "user_token": request.POST.get("userToken"),
            "card_product_token": request.POST.get("cardProductToken"),
            "fulfillment": {
                "card_personalization": {
                    "text": {
                        "name_line_1": {
                            "value": request.POST.get("name")
                        }
                    }
                },
                "shipping": {
                    "recipient_address": {
                        "address1": request.POST.get("address"),
                        "city": request.POST.get("city"),
                        "state": request.POST.get("state"),
                        "postal_code": request.POST.get("postalCode"),
                        "country": request.POST.get("country")
                    }
                }
            }
        })

        response = requests.post(url, headers=headers, data=data)

        isSuccess, message = getResponse(response)
        
        return render(request,'administrator/createCard.html', {'userTokens': getUserTokens(), 'cardProductTokens': getCardProductTokens(), 'isSuccess': isSuccess, 'message': message})

    return render(request, 'administrator/createCard.html', {'userTokens': getUserTokens(), 'cardProductTokens': getCardProductTokens()})

def listCardProducts(request):
    url = '{{BASE_URL}}cardproducts'
    
    response = requests.get(url, headers=headers)
    
    isSuccess, message, data, count = getLists(response)

    allCardProducts = []

    if isSuccess:
        for cardProduct in data:
            tempCardProduct = dict()
            tempCardProduct['token'] = cardProduct['token']
            tempCardProduct['name'] = cardProduct['name']
            tempCardProduct['activation_date'] = datetime.strptime(cardProduct['start_date'], "%Y-%m-%d").date()
            allCardProducts.append(tempCardProduct)

    return render(request,'administrator/listCardProducts.html', {'cardProducts': allCardProducts, 'isSuccess': isSuccess, 'message': message, 'count': count})

def createCardProduct(request):
    if request.method == 'POST':
        url = '{{BASE_URL}}cardproducts'

        data = json.dumps({
            "name": request.POST.get("name"),
            "active": request.POST.get("status"),
            "start_date": request.POST.get("startDate"),
            "config": {
                "poi": {
                    "ecommerce": request.POST.get("ecommerce"),
                    "atm": request.POST.get("atm")
                }
            }
        })

        response = requests.post(url, headers=headers, data=data)

        isSuccess, message = getResponse(response)

        return render(request,'administrator/createCardProduct.html', {'isSuccess': isSuccess, 'message': message})

    return render(request, 'administrator/createCardProduct.html')

def getUserTokens():
    url = '{{BASE_URL}}users'
    
    response = requests.get(url, headers=headers)
    
    userTokens = {}
    if response.status_code == 200:
        users = json.loads(response.text)['data']
        for user in users:
            userTokens[user['first_name'] + ' ' + user['last_name']] = user['token']
    return userTokens

def getCardProductTokens():
    url = '{{BASE_URL}}cardproducts'
    
    response = requests.get(url, headers=headers)
    
    cardProductTokens = {}
    if response.status_code == 200:
        cardProducts = json.loads(response.text)['data']
        for cardProduct in cardProducts:
            cardProductTokens[cardProduct['name']] = cardProduct['token']
    return cardProductTokens
