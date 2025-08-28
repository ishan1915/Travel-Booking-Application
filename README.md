# Travel-Booking-Application
# 🧳 Travel Booking System

A web-based **Travel Booking System** built with **Django**.  
Users can sign up, log in, manage their profiles, book travel options, view booking history, and cancel bookings.  

---

## 🚀 Features

- 🔐 **User Authentication**
  - Sign up, log in, and log out.
  - Profile management with editable details.

- 🚌 **Travel Booking**
  - Create bookings with travel options, seats, and total price.
  - Automatic booking timestamp.

- 📜 **Booking History**
  - View all past bookings.
  - Filter by **type, source, destination, and date**.
  - Cancel bookings with a single click.

- 🎨 **UI & Styling**
  - Clean design with **Bootstrap 5**.
  - Responsive templates.

---

## 🛠️ Tech Stack

- **Backend**: Django 5
- **Frontend**: Django Templates + Bootstrap 5
- **Database**: SQLite (default) / PostgreSQL (production-ready)
- **Authentication**: Django’s built-in auth system
- **Static Files**: Managed with Whitenoise

---

## 📂 Project Structure

travel-booking-system/
│── booking/ # App for bookings
│── users/ # App for profiles & authentication
│── templates/ # HTML templates
│── static/ # CSS, JS, Images
│── manage.py
│── requirements.txt
│── README.md

 

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/travel-booking-system.git
   cd travel-booking-system
Create and activate a virtual environment

 
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
Install dependencies

 
pip install -r requirements.txt
Run migrations

 
python manage.py migrate
Create a superuser

 
python manage.py createsuperuser
Run the development server

 
python manage.py runserver
Open in your browser: http://127.0.0.1:8000/

📸 Screenshots
Signup Page

User Dashboard

Booking History with Filters

(Add screenshots here after running the project)

📝 Future Improvements
✅ Payment Gateway Integration

✅ Email/SMS booking confirmation

✅ Admin dashboard for managing travel options

✅ PDF/Excel download for booking history

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a new branch (feature-new)

Commit your changes

Push and create a Pull Request

📄 License
This project is licensed under the MIT License – feel free to use and modify it.

