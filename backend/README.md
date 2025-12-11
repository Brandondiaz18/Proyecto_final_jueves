Backend FastAPI para Todo List.

Run locally:
1. instalar dependencias:
   pip install -r requirements.txt
2. exportar variables:
   export DATABASE_URL="mongodb+srv://user:pass@host/dbname"
   export ALLOWED_ORIGIN="http://localhost:5173"
3. ejecutar:
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
