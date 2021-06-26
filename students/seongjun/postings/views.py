import json

from django.http import JsonResponse
from django.views import View
from django.db.models import
from user.models import Account
from .models import Posting


# Create your views here.

class PostingView(View):
    def post(self, request):
        data        = json.loads(request.body)

        user        = Account.objects.get(nick_name=data.get('nick_name'))
        img_url     = data["img_url"]
        description = data["description"]

        if not user:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        Posting.objects.create(

            user        =user,
            img_url     =img_url,
            description =description
        )
        return JsonResponse({"message": "SUCCESS"}, status=201)

    def get(self, request):
        results     = []
        postings    = Posting.objects.all()

        for posting in postings:
            account = Posting.accounts_set.all()

            results.append({
                'name'          : account.nick_name,
                'img'           : posting.img_url,
                'description'   : posting.description,
                'created_at'    : posting.created_at
            })

        return JsonResponse({"results": results}, status=201)
