from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import reverse
from .models import Questions
from .models import Tags
# from .forms import NameForm
from .forms import QuestionForm
from .forms import TagsForm
from .forms import TagsDeleteForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def signup(request):
    print(request.method == 'POST')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # log user in
            print('should be saved')
            # return redirect(reverse('index'))
            return redirect(request, 'main/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('here')
            return redirect(reverse('creatingquestion'))
    else:
        form = AuthenticationForm()
        print('here')
    return render(request, 'main/index.html', {'form': form})


def homescreen(request):
    return render(request, 'main/home.html')


def creatingquestion(request):
    all_questions = Questions.objects.order_by('question_id')
    all_tags = Tags.objects.order_by('tag_id')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            obj = Questions()
            obj.question_id = all_questions[len(all_questions)-1].get_question_id() + 1
            obj.question_details = form.cleaned_data['question_details']
            obj.question_answer = form.cleaned_data['question_answer']
            obj.question_tags = None
            obj.time_questions_used = 0
            obj.tests_id = None
            # obj.save()
    else:
        form = QuestionForm()

    context = {
        'all_tags': all_tags,
        'form': form,
    }

    return render(request, 'main/creatingquestion.html', context)


def generatingtests(request):
    return render(request, 'main/generatingtests.html')


def questionlibarary(request):
    all_questions = Questions.objects.order_by('question_id')
    context = {
        'all_questions': all_questions,
    }
    return render(request, 'main/questionlibarary.html', context)


def tagcreator(request):
    # TODO make it so repeat tags canno't be entered into the database
    all_tags = Tags.objects.order_by('tag_id')
    current_tags = []
    form = TagsForm(request.POST)

    for tag in all_tags:
        current_tags.append(tag.tag_name.lower())
    print(request.POST.get('delete'))
    if request.method == 'POST' and not request.POST.get('delete'):
        if form.is_valid() and form.cleaned_data['tag_name'].lower() not in current_tags:
            obj = Tags()
            obj.tag_id = all_tags[len(all_tags)-1].get_tag_id() + 1
            obj.times_used = 0
            obj.tag_name = form.cleaned_data['tag_name']
            obj.question_id = None
            obj.tests_id = None
            obj.user_id = None
            # obj.save()
            print('if')

        else:
            form = TagsForm()

    elif request.POST.get('delete'):
            obj = Tags()
            print('elif')
            # obj.delete()

    else:
        form = TagsForm()
        print('else')

    context = {
        'all_tags': all_tags,
        'form': form,
    }

    return render(request, 'main/tagcreator.html', context)


def testlibarary(request):
    return render(request, 'main/testlibarary.html')



class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')
