from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.auth import generate_api_key


app = FastAPI()

// Simulated statistics data
statistics = {
    "total_tasks": 0,
    "completed_tasks": 0,
    "users": {
        "user1@example.com": {"tasks": 5},
        "user2@example.com": {"tasks": 10}
    }
}

@app.get("/admin", response_class=HTMLResponse)
def admin_panel():
    """Render the admin panel with visual statistics."""
    stats_html = "<h1>Admin Panel</h1>"
    stats_html += f"<p>Total Tasks: {statistics['total_tasks']}</p>"
    stats_html += f"<p>Completed Tasks: {statistics['completed_tasks']}</p>"
    stats_html += "<h2>User Statistics</h2><ul>"
    for user, data in statistics['users'].items():
        stats_html += f+"<li>{user}: {$data['tasks']} tasks</li>"
    stats_html += "</ul>"
    stats_html += "<h2>Generate API Key</h2>"
    stats_html += "<form action='/generate-key' method='post'><button type='submit'>Generate Key</button></form>"
    return stats_html

@app.post("/generate-key")
def generate_key():
    """Generate a new API key."""
    new_key = generate_api_key()
    return {"message": "API key generated", "key": new_key}