import json
# import re

from django.http import JsonResponse
from django.views import View
from django.db  import IntegrityError
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError
from user.models import Account
from user.validators import validate_email, validate_password, validate_phone_number



# Create your views here.


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
       # email_regex = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
       # phone_regex = re.compile(r'^01([0|1]?)-?([0-9]{3,4})-?([0-9]{4})$')
       # password_regex = re.compile(r'^[a-zA-Z0-9!@#$%^&*()_+,./<>?;:`~]{8,}$')

        try:

            if not validate_email(data['email']):
                return JsonResponse({"message": "이메일 형식을 맞추어주세요"}, status=400)
            if not validate_password(data['password']):
                return JsonResponse({'message': 'Password 8자~20자까지 가능합니다. '}, status=400)
            if validate_phone_number(data['phone_number']) ==0:
                return JsonResponse({'message': '잘못된 형식의 번호입니다.'}, status=400)
            else:
                data['phone_number']=validate_phone_number(data['phone_number'])
            # if not validate_phone_number(data['phone_number']):
            #    return JsonResponse({'message': '잘못된 형식의 번호입니다.'}, status=400)
            if len(data['nick_name']) < 4 or len(data['nick_name']) > 12:
                return JsonResponse({'message': '닉네임을 4자~8자까지 입력해주세요.'}, status=400)
            # if Account.objects.filter(email=data['email']).exists():
            #    return JsonResponse({'message': '이메일이 이미 등록되어있습니다.'}, status=400)
            # validate_email(data['email'])
            # if not email_regex.match(data['email']):
            #    return JsonResponse({"message": "이메일 형식을 맞추어주세요"}, status=400)
            # if not password_regex.match(data['password']):
            #    return JsonResponse({'message': 'Password 8자~20자까지 가능합니다. '}, status=400)
            # if Account.objects.filter(nick_name=data['nick_name']).exists():
            #    return JsonResponse({'message': '닉네임이 이미 존재합니다.'}, status=400)
            # if Account.objects.filter(phone_number=data['phone_number']).exists():
            #    return JsonResponse({'message': '전화번호가 이미 등록되어있습니다.'}, status=400)
            # if not phone_regex.match(data['phone_number']):
            #    return JsonResponse({'message': '잘못된 형식의 번호입니다.'}, status=400)

            Account.objects.create(
                email=data['email'],
                password=data['password'],
                nick_name=data['nick_name'],
                phone_number=data['phone_number']
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        # except ValidationError:
        #    return JsonResponse({"message": "VALIDATION_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({"message" : "key_error"}, status=400)
        except IntegrityError:
            return JsonResponse({"message" : "IntegrityError"}, status=400)


    def get(self, request):
        results = []
        accounts = Account.objects.all()

        for account in accounts:
            results.append({
                "email" : account.email,
                "password" : account.password,
                "nick_name" : account.nick_name,
                "phone_number" : account.phone_number,

            })
        return JsonResponse({'results': results}, status=200)


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
