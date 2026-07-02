# 🎓 AI Teacher Assistant

An intelligent web application that helps teachers save time by automatically generating quizzes from uploaded teaching materials and providing AI-powered grading — powered by **Google Gemini AI**.

## ✨ Features

- 📁 **Document Upload** — Upload lesson notes as PDF, PowerPoint (.pptx / .ppt), or plain text files
- 🤖 **AI Quiz Generation** — Automatically generate custom quizzes (Easy / Medium / Hard) from your documents using Gemini AI
- ⚡ **AI Auto-Grading** — Get instant, detailed feedback on student answers with marks and explanations
- 🔐 **Secure Auth** — JWT-based teacher authentication (signup & login)
- 🗄️ **Persistent Storage** — All documents, quizzes, and gradings stored in SQLite (or PostgreSQL for production)

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Backend** | Python · FastAPI · SQLAlchemy |
| **AI** | Google Gemini 2.5 Flash (`google-generativeai`) |
| **Auth** | JWT (PyJWT) · bcrypt |
| **Database** | SQLite (dev) / PostgreSQL (production) |
| **File Parsing** | PyPDF2 · python-pptx |

## 📁 Project Structure

```
Ai-Teacher-Assistant/
├── Backend/
│   ├── main.py              # FastAPI application & all API endpoints
│   ├── run_server.py        # Server startup script
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Environment variable template
│   └── test_api_key.py      # Utility to verify Gemini API key
│
└── Frontend/
    ├── index.html           # Landing page
    ├── login.html           # Teacher login
    ├── signup.html          # Teacher registration
    ├── dashboard.html       # Main dashboard
    ├── upload.html          # Document upload page
    ├── quiz-generator.html  # Quiz generation page
    └── grading.html         # Student answer grading page
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A **Google Gemini API key** — get one free at [Google AI Studio](https://aistudio.google.com/app/apikey)

### 1. Clone the Repository

```bash
git clone https://github.com/haseebashraf5656/Ai-Teacher-Assistant.git
cd Ai-Teacher-Assistant
```

### 2. Set Up the Backend

```bash
cd Backend

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Copy the example file
copy .env.example .env    # Windows
# cp .env.example .env    # macOS / Linux
```

Open `.env` and fill in your values:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
SECRET_KEY=your_strong_random_secret_key
DATABASE_URL=sqlite:///./teacher_assistant.db
```

### 4. Run the Backend Server

```bash
python run_server.py
# or
uvicorn main:app --reload --port 8000
```

The API will be available at **http://localhost:8000**  
Interactive API docs: **http://localhost:8000/docs**

### 5. Open the Frontend

Simply open `Frontend/index.html` in your browser, or serve it with any static server:

```bash
cd ../Frontend
python -m http.server 3000
```

Then visit **http://localhost:3000**

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/signup` | Register a new teacher account |
| `POST` | `/api/auth/login` | Login and receive JWT token |
| `POST` | `/api/documents/upload` | Upload a PDF / PPT / TXT file |
| `GET`  | `/api/documents/list` | List all uploaded documents |
| `POST` | `/api/quiz/generate` | Generate quiz from a document |
| `GET`  | `/api/quiz/list` | List all generated quizzes |
| `POST` | `/api/grading/grade` | Grade a student's answer |

## 🔒 Security

- API keys and secrets are stored in `.env` files — **never committed to Git**
- Passwords are hashed using **bcrypt**
- All protected routes require a valid **JWT Bearer token**
- `.env` is listed in `.gitignore` to prevent accidental exposure

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with ❤️ using FastAPI and Google Gemini AI
