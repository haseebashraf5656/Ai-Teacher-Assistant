# AI Teacher Assistant - Backend API

This is the backend API for the AI-Based Teacher Assistant System built with FastAPI, PostgreSQL, and Google Gemini AI.

## Features

- **User Authentication**: Secure signup and login for teachers
- **Document Upload**: Upload PDF, PPT, or TXT files
- **AI Quiz Generation**: Generate quizzes with customizable difficulty (Easy, Medium, Hard)
- **AI Answer Grading**: Automatically grade student answers with detailed feedback
- **Data Persistence**: All data stored in PostgreSQL database

## Technology Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL (SQLite option available for development)
- **AI**: Google Gemini API
- **Authentication**: JWT tokens with bcrypt password hashing
- **File Processing**: PyPDF2 (PDF), python-pptx (PowerPoint)

## Project Structure

```
ai_teacher_backend/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- PostgreSQL (or use SQLite for development)
- Gemini API key (already configured)

### Step 1: Clone/Download the Project

```bash
cd ai_teacher_backend
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

#### Option A: PostgreSQL (Recommended for Production)

1. Install PostgreSQL
2. Create a database:
```sql
CREATE DATABASE teacher_assistant;
```

3. Update the `DATABASE_URL` in `main.py` line 54:
```python
DATABASE_URL = "postgresql://username:password@localhost:5432/teacher_assistant"
```

#### Option B: SQLite (Easier for Development)

Simply uncomment line 56 in `main.py`:
```python
DATABASE_URL = "sqlite:///./teacher_assistant.db"
```

And comment out the PostgreSQL line above it.

### Step 5: Run the Application

```bash
python main.py
```

Or use uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication

#### 1. Signup
```http
POST /api/auth/signup
Content-Type: application/json

{
  "email": "teacher@example.com",
  "full_name": "John Doe",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user_info": {
    "id": 1,
    "email": "teacher@example.com",
    "full_name": "John Doe"
  }
}
```

#### 2. Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "teacher@example.com",
  "password": "securepassword123"
}
```

### Document Management

#### 3. Upload Document
```http
POST /api/documents/upload
Authorization: Bearer {access_token}
Content-Type: multipart/form-data

file: [PDF/PPT/TXT file]
```

**Response:**
```json
{
  "message": "Document uploaded successfully",
  "document_id": 1,
  "filename": "chapter1.pdf",
  "content_length": 5234
}
```

#### 4. List Documents
```http
GET /api/documents/list
Authorization: Bearer {access_token}
```

### Quiz Generation

#### 5. Generate Quiz
```http
POST /api/quiz/generate
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "document_id": 1,
  "difficulty": "Medium",
  "selected_portion": "Optional: specific text portion"
}
```

**Response:**
```json
{
  "quiz_id": 1,
  "questions": [
    {
      "question_number": 1,
      "question_text": "What is photosynthesis?",
      "marks": 5,
      "reference_answer": "Photosynthesis is the process..."
    }
  ],
  "message": "Successfully generated 3 questions at Medium difficulty"
}
```

#### 6. List Quizzes
```http
GET /api/quiz/list
Authorization: Bearer {access_token}
```

### Answer Grading

#### 7. Grade Answer
```http
POST /api/grading/grade
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "quiz_id": 1,
  "question_number": 1,
  "student_answer": "Photosynthesis is when plants make food from sunlight",
  "total_marks": 5
}
```

**Response:**
```json
{
  "grading_id": 1,
  "marks_obtained": 3.5,
  "total_marks": 5,
  "feedback": "Good understanding of the basic concept. The answer correctly identifies that photosynthesis involves plants and sunlight. However, it lacks detail about the conversion of light energy to chemical energy and the production of glucose. Marks deducted for missing key details about chlorophyll and the chemical equation.",
  "percentage": 70.0
}
```

#### 8. Grading History
```http
GET /api/grading/history
Authorization: Bearer {access_token}
```

## Usage Example with Python

```python
import requests

BASE_URL = "http://localhost:8000"

# 1. Signup
signup_data = {
    "email": "teacher@school.com",
    "full_name": "Jane Smith",
    "password": "mypassword123"
}
response = requests.post(f"{BASE_URL}/api/auth/signup", json=signup_data)
token = response.json()["access_token"]

headers = {"Authorization": f"Bearer {token}"}

# 2. Upload Document
with open("textbook.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(f"{BASE_URL}/api/documents/upload", 
                            files=files, headers=headers)
    document_id = response.json()["document_id"]

# 3. Generate Quiz
quiz_data = {
    "document_id": document_id,
    "difficulty": "Medium"
}
response = requests.post(f"{BASE_URL}/api/quiz/generate", 
                        json=quiz_data, headers=headers)
quiz = response.json()

# 4. Grade Answer
grading_data = {
    "quiz_id": quiz["quiz_id"],
    "question_number": 1,
    "student_answer": "Your answer here",
    "total_marks": 5
}
response = requests.post(f"{BASE_URL}/api/grading/grade", 
                        json=grading_data, headers=headers)
result = response.json()
print(f"Marks: {result['marks_obtained']}/{result['total_marks']}")
print(f"Feedback: {result['feedback']}")
```

## Configuration

### Security Settings

**IMPORTANT**: Before deploying to production:

1. Change the `SECRET_KEY` in `main.py` (line 49):
```python
SECRET_KEY = "use-a-long-random-string-here"
```

Generate a secure key:
```python
import secrets
print(secrets.token_urlsafe(32))
```

2. Update your Gemini API key if needed (line 44)

### Database Migration

The application automatically creates all tables on first run. If you need to reset the database:

**PostgreSQL:**
```sql
DROP DATABASE teacher_assistant;
CREATE DATABASE teacher_assistant;
```

**SQLite:**
```bash
rm teacher_assistant.db
```

Then restart the application.

## Testing the API

### Using cURL

```bash
# Signup
curl -X POST "http://localhost:8000/api/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","full_name":"Test User","password":"test123"}'

# Upload Document
curl -X POST "http://localhost:8000/api/documents/upload" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@document.pdf"
```

### Using Postman

1. Import the endpoints into Postman
2. Set up environment variables:
   - `base_url`: http://localhost:8000
   - `token`: Your JWT token from login/signup
3. Use `{{base_url}}` and `{{token}}` in your requests

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Make sure PostgreSQL is running
   - Check database credentials in `DATABASE_URL`
   - Or switch to SQLite for development

2. **Module Not Found Error**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt` again

3. **Gemini API Error**
   - Verify your API key is correct
   - Check your internet connection
   - Ensure you haven't exceeded API quota

4. **File Upload Error**
   - Check file size (max recommended: 10MB)
   - Ensure file format is PDF, PPT, or TXT
   - Verify file is not corrupted

## Features in Detail

### Quiz Generation
- Supports 3 difficulty levels: Easy, Medium, Hard
- Generates 2-3 questions per request
- Can work on full document or selected portions
- Questions are contextual and relevant

### Answer Grading
- Provides marks out of total specified
- Gives detailed feedback explaining the grade
- Highlights what was correct and incorrect
- Fair and transparent grading system

## Future Enhancements

Planned features for future versions:
- Multiple choice questions (MCQs)
- Plagiarism detection
- Student performance analytics
- Multi-language support
- Export quiz to PDF
- Batch grading

## License

This project is created for educational purposes.

## Support

For issues or questions:
1. Check the API documentation at `/docs`
2. Review this README
3. Check common issues in Troubleshooting section

## Notes

- Keep your Gemini API key secure
- Don't commit `.env` file to version control
- Use strong passwords for production
- Regular database backups recommended
- Monitor API usage to stay within Gemini quotas
