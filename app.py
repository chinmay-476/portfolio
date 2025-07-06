from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

projects_data = [
    {
        "id": 1,
        "title": "🌐 Portfolio Website",
        "description": "A modern, responsive portfolio website built with Flask, featuring dark/light mode, animations, and interactive elements.",
        "tech_stack": ["Flask", "HTML5", "CSS3", "JavaScript", "Responsive Design"],
        "status": "completed",
        "github": "https://github.com/chinmay-476/portfolio",
        "demo": None,
        "image": "portfolio.jpg"
    },
    {
        "id": 2,
        "title": "📝 Smart To-Do App",
        "description": "A feature-rich task management app with categories, due dates, and progress tracking.",
        "tech_stack": ["Flask", "SQLite", "Bootstrap", "JavaScript", "CRUD"],
        "status": "in_progress",
        "github": "https://github.com/chinmay-476/todo-app",
        "demo": None,
        "image": "todo.jpg"
    },
    {
        "id": 3,
        "title": "🌦️ Weather Dashboard",
        "description": "Real-time weather app with location-based forecasts and beautiful data visualizations.",
        "tech_stack": ["Python", "OpenWeather API", "Chart.js", "Geolocation"],
        "status": "planned",
        "github": None,
        "demo": None,
        "image": "weather.jpg"
    },
    {
        "id": 4,
        "title": "🧠 Algorithm Visualizer",
        "description": "Interactive web app to visualize sorting algorithms and data structures in real-time.",
        "tech_stack": ["JavaScript", "HTML5 Canvas", "CSS3", "Algorithms"],
        "status": "planned",
        "github": None,
        "demo": None,
        "image": "algo.jpg"
    }
]

skills_data = {
    "languages": ["Python", "JavaScript", "C++", "HTML5", "CSS3", "SQL"],
    "frameworks": ["Flask", "Bootstrap", "jQuery"],
    "tools": ["Git", "GitHub", "VS Code", "SQLite"],
    "learning": ["React", "Node.js", "MongoDB", "Docker"]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', skills=skills_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/projects')
def api_projects():
    return jsonify(projects_data)

@app.route('/api/skills')
def api_skills():
    return jsonify(skills_data)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "Thanks for your message! I'll get back to you soon."
    })

if __name__ == '__main__':
    app.run(debug=True)