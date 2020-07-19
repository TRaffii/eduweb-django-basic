from django.http import HttpResponse

# Create your views here.


def add_question(request):
    return HttpResponse("Adding a review")


def show_question(request, question_id):
    print(f"Passed question id: {question_id}")
    return HttpResponse("Showing question...")

