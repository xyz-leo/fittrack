# FitTrack

FitTrack is a prototype of a fitness tracking web application built with Django.  
It was developed as a college project to demonstrate the structure of a simple, mobile-first web app for gyms and personal trainers.  
The project focuses on clean design, essential functionality, and simplicity over production-level features.

---

## Disclaimer

This project is a **prototype** developed as a **minimum viable product (MVP)** to demonstrate the structure and functionality of a fitness tracking web application built with Django.  
It was created for educational and presentation purposes to showcase how core concepts such as user registration, basic navigation, and data display can be implemented within a web framework.  

The system does **not include production-level features**, such as advanced authentication, security measures, or data persistence for real-world deployment.  
Its goal is to illustrate a functional design flow and the integration of backend and frontend components in a clean, mobile-first interface.

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

---

## Data Model Overview

### `Student` Model

The `Student` model represents a user within the FitTrack prototype.  
It stores essential information about the student's physical attributes, training preferences, and login data (for demonstration purposes only).
```
| Field | Type | Description |
|-------|------|--------------|
| `full_name` | `CharField` | The student's complete name. |
| `email` | `EmailField` (unique) | Used as a unique identifier for login. |
| `password` | `CharField` | Stored in plaintext for simplicity — **not secure** and only acceptable in prototypes. |
| `height_cm` | `PositiveIntegerField` | Height in centimeters (optional). |
| `weight_kg` | `DecimalField` | Weight in kilograms, supports decimal values (optional). |
| `age` | `PositiveIntegerField` | Student’s age (optional). |
| `level` | `CharField` with choices | Indicates training level: *Beginner*, *Intermediate*, or *Advanced*. |
| `frequency_per_week` | `PositiveIntegerField` | How many times per week the student trains (default: 3). |
| `objective` | `CharField` with choices | Defines the student’s fitness goal: *Mass Gain*, *Fat Loss*, or *Maintenance*. |
| `created_at` | `DateTimeField` | Automatically stores the date/time when the record was created. |

**Helper methods:**

- `first_name()`: Returns the student's first name, extracted from `full_name`.
- `__str__()`: Returns a readable string representation, e.g. `John Doe <john@example.com>`.
```
---

## Template Integration

The data from the `Student` model is passed from Django views to the templates using the template context.  
Inside the template, Django’s template language is used to display data dynamically.

Example snippet from a template:

```html
<h2>{{ student.first_name }}</h2>
<p class="muted">
  {{ student.level|title }} • {{ student.objective|cut:"_"|title }}
</p>
```

**Explanation:**

- `{{ student.first_name }}`  
  Calls the model method `first_name()` and displays only the first word of the `full_name` field.  
  Example: `"John Doe"` → `"John"`.

- `{{ student.level|title }}`  
  Uses Django’s built-in `title` filter to capitalize the first letter of each word.  
  Example: `"beginner"` → `"Beginner"`.

- `{{ student.objective|cut:"_"," "|title }}`  
  First replaces underscores (`_`) with spaces (` `), then applies the `title` filter.  
  Example: `"mass_gain"` → `"Mass Gain"`.

These template expressions dynamically render student information, applying formatting directly in the HTML layer while keeping the Python model clean and focused on data.


## CSS and Design Approach

The CSS was written with a **mobile-first** mindset, ensuring the interface looks clean and functional on small screens, such as smartphones, before scaling up to desktop layouts.  
The design uses a **light theme** with **orange as the highlight color**, combined with **neutral grays** for balance. The typography is based on **Poppins**, a friendly and modern sans-serif font that provides good readability and visual appeal.

Key design choices:
- **Responsive layout:** Uses flexible containers and relative units (`%`, `rem`) to adapt to different screen sizes.  
- **Hamburger menu:** A simplified icon that appears on both mobile and desktop for consistency.  
- **Consistent spacing:** Padding and margins ensure proper breathing space between elements.  
- **Card-based sections:** Information such as the user’s plan and training summary is presented inside rounded boxes with soft shadows to improve visual hierarchy.  
- **Minimalist color palette:** Light backgrounds, orange accents, and black text for optimal contrast and readability.

The goal was to keep the CSS **simple, readable, and easy to extend**, while still achieving a visually cohesive result suitable for an MVP demonstration.
