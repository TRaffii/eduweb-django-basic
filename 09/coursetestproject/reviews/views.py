from django.http import HttpResponse

# Create your views here.


def add_question(request):
    return HttpResponse("Adding a review")


def show_question(request, question_id):
    print(f"Passed question id: {question_id}")
    return HttpResponse("Showing question...")


def show_by_year(request, year):
    print(f'Year is: {year}')
    if year is not None:
        return HttpResponse(f"Year if {year}")
    return HttpResponse(f"Year is missing")
