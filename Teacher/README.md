# TutoraHub LMS Teacher API

This is the Teacher API server for TutoraHub LMS, built with FastAPI.

## Features
- JWT-based authentication (shared with other services)
- Teacher profile and classes endpoints
- Modular, production-ready structure

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```

## Authentication
- Obtain a JWT token by POSTing to `/token` with form data `username` and `password`.
- Use the returned token as a Bearer token in the `Authorization` header for all protected endpoints.

## Example Usage

### Get a Token
```bash
curl -X POST "http://localhost:8000/token" -d "username=teacher1&password=yourpass"
```

### Access Protected Endpoint
```bash
curl -H "Authorization: Bearer <access_token>" http://localhost:8000/v1/teacher/me
```

## Project Structure
```
Teacher/
  main.py
  requirements.txt
  v1_api/
    teacher_router.py
  README.md
```

## License
MIT 