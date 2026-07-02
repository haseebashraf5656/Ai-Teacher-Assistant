# Quick Start Guide

Get your AI Teacher Assistant backend running in 5 minutes!

## Option 1: Quick Setup (SQLite - No Database Installation Required)

### Step 1: Install Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Configure Database
Open `main.py` and change line 54-56 to use SQLite:

```python
# Comment out PostgreSQL:
# DATABASE_URL = "postgresql://postgres:password@localhost:5432/teacher_assistant"

# Uncomment SQLite:
DATABASE_URL = "sqlite:///./teacher_assistant.db"
```

### Step 3: Run the Server
```bash
python main.py
```

That's it! Visit http://localhost:8000/docs to see the API documentation.

### Step 4: Test the API
```bash
# In a new terminal (keep server running)
python test_api.py
```

## Option 2: Docker Setup (Everything Included)

### Prerequisites
- Docker and Docker Compose installed

### One Command Setup
```bash
docker-compose up
```

This will:
- Start PostgreSQL database
- Start FastAPI application
- Automatically connect them

Visit http://localhost:8000/docs

## Option 3: PostgreSQL Setup (Production)

### Step 1: Install PostgreSQL
- Download from https://www.postgresql.org/download/

### Step 2: Create Database
```sql
CREATE DATABASE teacher_assistant;
```

### Step 3: Update Configuration
In `main.py` line 54, update your credentials:
```python
DATABASE_URL = "postgresql://your_username:your_password@localhost:5432/teacher_assistant"
```

### Step 4: Install Dependencies & Run
```bash
pip install -r requirements.txt
python main.py
```

## Testing Your Setup

### Using the Test Script
```bash
python test_api.py
```

### Using cURL
```bash
# Create account
curl -X POST "http://localhost:8000/api/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","full_name":"Test User","password":"test123"}'
```

### Using Browser
Go to http://localhost:8000/docs and use the interactive API documentation!

## Next Steps

1. ✅ Server is running
2. 📝 Read the full README.md for detailed documentation
3. 🧪 Test all endpoints using `/docs` interface
4. 🔨 Start building your frontend
5. 🎨 Customize the API for your needs

## Common Issues

**Can't connect to database?**
- Use SQLite instead (see Option 1)

**Port 8000 already in use?**
```bash
# Change port in main.py last line:
uvicorn.run(app, host="0.0.0.0", port=8001)
```

**Import errors?**
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

## API Overview

Once running, you have these endpoints:

- `POST /api/auth/signup` - Create teacher account
- `POST /api/auth/login` - Login
- `POST /api/documents/upload` - Upload teaching material
- `POST /api/quiz/generate` - Generate quiz questions
- `POST /api/grading/grade` - Grade student answers
- `GET /api/documents/list` - View uploaded documents
- `GET /api/quiz/list` - View created quizzes
- `GET /api/grading/history` - View grading history

## Support

- 📚 Full documentation: README.md
- 🌐 Interactive API docs: http://localhost:8000/docs
- 🔍 Alternative docs: http://localhost:8000/redoc

Happy coding! 🚀
