import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User,Question,History,Category, Quiz
import random

@csrf_exempt
def quiz(request, username):
        user = User.objects.get(username=username)
        # quiz = Quiz(name="This quiz is for", quiz={})
        result = {}
        for elm in Category.objects.all():
            q = list(elm.q_to_c.filter(category=elm.id))
            # print(q)
            rq = random.sample(q, 4)
            result[elm.title] = [r.description for r in rq]
        
        # print(result.values())
        l = []
        for elm in result.values():
            for i in elm:
                l.append(i)
        a = Question.objects.values('title', 'select')
        javab = {}
        for elm in a:
            if elm['title'] in l:
                javab[elm['title']]=elm['select']
        print(javab)
        history = History.objects.create(user=user, quiz=result)
        if request.method == "GET":
            # print(javab)
            if History.objects.values('quiz') == result:
                return JsonResponse({"status": "azmon tekrari"})
            else:
                return JsonResponse({"status": "successful", "quiz": result})
        elif request.method == "POST":
            natije = 0
            answer_sheet = json.loads(request.body.decode("utf-8"))
            # print(javab.values())
            jl = []
            for i in javab.values():
                jl.append(i)
            for j in answer_sheet.values():
                if j in jl:
                    natije += 1
            history.score = natije
            history.save()
            return JsonResponse({"status": "successful", "natije nahayi": natije})
            
