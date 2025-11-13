# FitTrack

FitTrack is a prototype of a fitness tracking web application built with Django.  
It was developed as a college project to demonstrate the structure of a simple, mobile-first web app for gyms and personal trainers.  
The project focuses on clean design, essential functionality, and simplicity over production-level features.

---

## Features

- **User Registration**: Create a profile with name, height, weight, age, experience level, frequency, and fitness goal.
- **Login Simulation**: Simple login and redirect to the user’s dashboard.
- **User Home**: Displays mock data such as current plan, training days per month, and last workouts.
- **Workout Page**: Lists static training information for demonstration.
- **Responsive Design**: Mobile-first layout with a light theme and orange as the primary color.

---

## Technologies Used

- **Python 3.12+**
- **Django 5+**
- **HTML5 / CSS3**
- **Poppins font (Google Fonts)**

---

## Project Structure
```
fittrack/
│
├── manage.py
├── fittrack/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── core/
├── migrations/
├── templates/core/
│ ├── base.html
│ ├── login.html
│ ├── cadastro.html
│ ├── home.html
│ └── treinos.html
├── static/core/css/style.css
├── models.py
├── forms.py
├── views.py
└── urls.py
```

---

## How to Run

**Clone the repository**

   ```bash
   git clone https://github.com/xyz-leo/fittrack.git
   cd fittrack
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   pip install django
   python manage.py migrate
   python manage.py runserver
   ```
Access the app with your browser at http://localhost:8000

## Notes

- This is a prototype intended for educational purposes.
- Authentication is simulated for demonstration and not secure.
- Data such as user stats and workouts are mocked for presentation.
