"""
Flask Web Application — Electricity Consumption Dashboard & Story Embed
Displays Tableau dashboard screenshots within a premium Flask UI.
"""

from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ─── Dashboard & Story Configuration ────────────────────────────────────
# Each entry maps to a dashboard screenshot or story video in static/images/
DASHBOARD_ITEMS = {
    "dashboard1": {
        "title": "Overview & Geographic Analysis",
        "description": "State-wise consumption maps for 2019 & 2020, regional pie chart, usage trends by year, and total consumption comparison across all 33 states.",
        "media": "images/dash1.png",
        "type": "image",
        "icon": "🗺️",
        "tags": ["Maps", "Bar Charts", "Line Charts", "Pie Chart"],
    },
    "dashboard2": {
        "title": "Comparative & Ranking Analysis",
        "description": "Regional usage comparison, Top N and Bottom N state rankings with parameter controls, and monthly consumption patterns for 2019 & 2020.",
        "media": "images/dash2.png",
        "type": "image",
        "icon": "📊",
        "tags": ["Top N Filter", "Bottom N Filter", "Monthly View", "Grouped Bars"],
    },
    "dashboard3": {
        "title": "Deep Dive & Lockdown Analysis",
        "description": "COVID-19 lockdown impact analysis, regionwise state breakdown, quarterwise usage, metro city comparison, and monthwise top consumption heatmap.",
        "media": "images/dash3.png",
        "type": "image",
        "icon": "🔒",
        "tags": ["Lockdown Impact", "Metro Cities", "Region Breakdown", "Quarterly View"],
    },
    "story": {
        "title": "Electricity Consumption Story",
        "description": "A narrative walkthrough of India's electricity consumption patterns from 2019 to 2020, exploring the impact of COVID-19 lockdown across states and regions.",
        "media": "images/story.mkv",
        "type": "video",
        "icon": "📖",
        "tags": ["Narrative", "COVID-19 Impact", "Year-over-Year", "Insights"],
    },
}


# ─── Demo credentials (for demonstration purposes) ─────────────────────
DEMO_USER = {"username": "admin", "password": "admin123"}


# ─── Authentication decorator ──────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Please log in to access the dashboards.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


# ─── Routes ─────────────────────────────────────────────────────────────
@app.route("/")
def index():
    """Landing page"""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page with demo authentication"""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == DEMO_USER["username"] and password == DEMO_USER["password"]:
            session["logged_in"] = True
            session["username"] = username
            flash("Login successful! Welcome to the dashboard.", "success")
            return redirect(url_for("dashboards"))
        else:
            flash("Invalid credentials. Try admin / admin123", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    """Logout and clear session"""
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


@app.route("/dashboards")
@login_required
def dashboards():
    """Dashboard gallery page"""
    return render_template("dashboards.html", items=DASHBOARD_ITEMS)


@app.route("/view/<dash_id>")
@login_required
def view_dash(dash_id):
    """Dashboard image viewer"""
    dash = DASHBOARD_ITEMS.get(dash_id)
    if not dash:
        flash("Dashboard not found.", "error")
        return redirect(url_for("dashboards"))
    return render_template("viewer.html", dash=dash, dash_id=dash_id, all_dashes=DASHBOARD_ITEMS)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
