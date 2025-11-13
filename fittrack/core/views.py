# core/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from .models import Student
from django.urls import reverse
from django.contrib import messages  # optional, used for flash messages

# ---- Helper: get logged-in student from session ----
def get_logged_student(request):
    """
    Return Student instance if session has student_id, else None.
    We store 'student_id' in session upon login/signup.
    """
    student_id = request.session.get('student_id')
    if not student_id:
        return None
    try:
        return Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return None

# ---- Landing page (simple public page) ----
def landing(request):
    return render(request, 'core/landing.html')

# ---- Register view ----
def register(request):
    # If user already logged, redirect to home
    if get_logged_student(request):
        return redirect('core:home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save student (password stored as-is for prototype)
            student = Student(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                height_cm=form.cleaned_data.get('height_cm'),
                weight_kg=form.cleaned_data.get('weight_kg'),
                age=form.cleaned_data.get('age'),
                level=form.cleaned_data.get('level'),
                frequency_per_week=form.cleaned_data.get('frequency_per_week'),
                objective=form.cleaned_data.get('objective'),
            )
            student.save()
            # put student id in session to simulate login
            request.session['student_id'] = student.id
            return redirect('core:home')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})

# ---- Login view ----
def login_view(request):
    # If already logged, redirect
    if get_logged_student(request):
        return redirect('core:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Simple authentication: check email + password match record
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(email=email, password=password)
                request.session['student_id'] = student.id
                return redirect('core:home')
            except Student.DoesNotExist:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

# ---- Logout ----
def logout_view(request):
    # Remove session key to simulate logout
    request.session.pop('student_id', None)
    return redirect('core:landing')

# ---- Home page (for logged student) ----
def home(request):
    student = get_logged_student(request)
    if not student:
        return redirect('core:login')

    # Mocked statistics for this prototype
    # In a real app these would be calculated from workout logs.
    mock_plan = {
        'name': 'Standard Strength Plan',
        'price': 'Free (Student Plan)',
        'duration': 'Monthly',
    }
    # e.g., days trained this month randomized or fixed mock
    mock_days_trained = 8  # mocked number
    mock_last_trainings = [
        {'title': 'Upper Body - Hypertrophy', 'date': '2025-11-10'},
        {'title': 'Leg Day - Strength', 'date': '2025-11-07'},
        {'title': 'Full Body - Conditioning', 'date': '2025-11-05'},
    ]

    context = {
        'student': student,
        'plan': mock_plan,
        'days_trained': mock_days_trained,
        'last_trainings': mock_last_trainings,
    }
    return render(request, 'core/home.html', context)

# ---- Trainings page ----
def trainings(request):
    student = get_logged_student(request)
    if not student:
        return redirect('core:login')

    # For prototype, show some mock/trainings stored in DB (if any).
    # We didn't create a Training model, so we'll mock a list.
    mock_trainings = [
        {'title': 'Push / Pull / Legs', 'description': '3x week split focusing on compound lifts'},
        {'title': 'Full Body 3x', 'description': 'Full body session with circuits'},
        {'title': 'Upper Hypertrophy', 'description': 'Isolated work and higher volume'},
    ]
    return render(request, 'core/trainings.html', {'student': student, 'trainings': mock_trainings})

