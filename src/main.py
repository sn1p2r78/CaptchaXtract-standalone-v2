from fastapi import FastAPI
from src.admin_panel import app as admin_panel_app

// Main FastAPI app
app = FastAPI()

# Include the admin panel app
app.mount("/admin-panel", admin_panel_app)
@app.get("/")
def read_root():
    return {"message": "Welcome to Captcha^Tract Standalone V2"}