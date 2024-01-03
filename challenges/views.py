from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no biscuits for the month!",
    "february": "Walk every day of the month!",
    "march": "Learn Django for at least an hour a day!",
    "april": "Birthday month!!!",
    "may":"Mayday",
    "june":"Summer holidays",
    "july":"To warm this month",
    "august":"Wheres summer gone!!",
    "september":"Getting winter ready!!!",
    "october":"Getting ready for Halloween",
    "november":"Almost Christmas time!!!",
    "december":"Christmas time!!"
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    challenge_text = monthly_challenges.get(month, "<h1>This month is not supported!</h1>")
    return render(request, "challenges/challenge.html", {
        "text": challenge_text,
        "month_name": month
    })