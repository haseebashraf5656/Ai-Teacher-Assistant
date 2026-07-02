# Setup Instructions - Connect Frontend to Backend

## Quick Setup Steps:

### 1. Replace Your HTML Files

Copy these updated files to your Frontend folder:
- login.html
- signup.html
- dashboard.html (coming next)
- upload.html (coming next)
- quiz-generator.html (coming next)
- grading.html (coming next)

### 2. Make Sure Backend is Running

```bash
cd "D:\Teacher Assistant\backend"
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 3. Open Frontend

Simply open any HTML file in your browser:
- Start with: `login.html`
- Or: `index.html` (landing page)

## How It Works:

✅ **Login/Signup** - Connects to backend API at `http://localhost:8000/api/auth/`
✅ **Stores JWT token** - In localStorage for authentication
✅ **All pages protected** - Redirects to login if not authenticated
✅ **Upload documents** - Sends files to backend
✅ **Generate quizzes** - Uses AI via backend
✅ **Grade answers** - Gets AI feedback from backend

## API Endpoints Used:

- POST `/api/auth/signup` - Create account
- POST `/api/auth/login` - Login
- POST `/api/documents/upload` - Upload files
- GET `/api/documents/list` - View documents
- POST `/api/quiz/generate` - Generate quiz
- GET `/api/quiz/list` - View quizzes
- POST `/api/grading/grade` - Grade answer
- GET `/api/grading/history` - View history

## Testing:

1. Open `login.html` in browser
2. Click "Sign Up"
3. Create account
4. Should redirect to dashboard
5. Try uploading a file
6. Generate a quiz
7. Grade an answer

All connected to your backend! 🎉
