# 🔐 LifeVault – Personal Digital Life Manager

LifeVault is a full-stack web application that helps users securely manage their personal digital information in one place. The application provides user authentication and serves as a foundation for securely storing documents, passwords, notes, and reminders.

## 🚀 Features

- User Registration
- User Login Authentication
- Secure Password Hashing
- SQLite Database Integration
- FastAPI REST APIs
- React Frontend
- Responsive User Interface
- Dashboard after Login

## 🛠 Tech Stack

### Frontend
- React.js
- Vite
- Axios
- React Router DOM
- CSS

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Passlib (bcrypt)
- Python

## 📁 Project Structure

```
Life-Vault/
│
├── client/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── server/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Life-Vault.git
```

### Frontend

```bash
cd client
npm install
npm run dev
```

### Backend

```bash
cd server
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Frontend runs at:

```
http://localhost:5173
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register a new user |
| POST | /login | User Login |

## 🔒 Security

- Passwords are securely hashed using bcrypt.
- Sensitive environment variables are stored in a `.env` file.
- SQLite is used for persistent data storage.

## 📈 Future Enhancements

- JWT Authentication
- Password Vault
- Secure Notes
- Document Upload
- Reminder Management
- Profile Management
- Search Functionality
- Dark Mode
- Cloud Storage Integration

## 👩‍💻 Author

**Manaswini Reddy**
