from fastapi import FastAPI

app = FastAPI(
    title = 'Role-Based Authentication System API',
    version = '1.0.0'
)

# @app.get("/api/health") - creates an HTTP GET endpoint.
# GET /api/health will execute: health_check()
@app.get('/api/health')
def health_check():
    return {
        'status': 'OK',
        'message': 'Backend is running'
    }