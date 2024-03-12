from django.shortcuts import render, HttpResponse
import os
from django.http import JsonResponse
import openai
openai.api_key = "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"
def chat(request):
    return render(request, 'index.html')


def ChatAPI(request):
    if request.method == "POST":
        prompt = request.POST["prompt"]
        print(prompt)
        response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                max_tokens=256,
                messages=[
                            {
                                "role": "user",
                                "content": prompt,
                            }
                        ],
                    )
        bot_response = response.choices[0].message.content
        return JsonResponse(bot_response, safe=False)
    
    return HttpResponse("Bad Request")


def home(request):
    context = {
        'page': 'home',
    }
    return render(request, 'home.html', context)
