# PocketLedger 💰

A simple, full-stack personal expense tracker. This project demonstrates a decoupled architecture using a **Django REST Framework** backend and a standalone **Vanilla JavaScript** frontend.

## ✨ Features
- **Add Transactions:** Log your Income and Expenses easily.
- **Live Feed:** View a list of your recent financial activity.
- **REST API:** Fully functional API endpoints for transaction management.
- **Dockerized:** Ready to deploy or run in a container.

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework (DRF), Python 3.12
- **Frontend:** HTML5, Bootstrap 5, Vanilla JavaScript (Fetch API)
- **Database:** SQLite (default)
- **DevOps:** Docker

---

## 🚀 How to Run Locally

### 1. Backend Setup
Make sure you have Python installed.

```bash
# Clone the repo
git clone [https://github.com/SatyajitKumar123/pocketledger.git](https://github.com/SatyajitKumar123/pocketledger.git)
cd pocketledger

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations and start server
python manage.py migrate
python manage.py runserver

# The API is now running at http://127.0.0.1:8000/api/transactions/

2. Frontend Setup
 1. Navigate to the frontend/ folder.

 2. Open index.html in your web browser.

 3. Start adding transactions!