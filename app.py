from datetime import datetime

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

profile_data = {
    "name": "Chinmay Sahoo",
    "headline": "Software developer focused on practical web apps, cleaner interfaces, and steady technical growth.",
    "summary": (
        "I build portfolio projects across Flask, Java, machine learning, and legal-tech workflows. "
        "My goal is to ship projects that are readable, useful, and clearly connected to real problem solving."
    ),
    "location": "Odisha, India",
    "email": "chinmaysahoo63715@gmail.com",
    "github": "https://github.com/chinmay-476",
    "linkedin": "https://www.linkedin.com/in/chinmay-sahoo-5ba863328",
}

projects_data = [
    {
        "id": 1,
        "title": "UrbanMove",
        "description": "A Flask-based rental analytics and decision-support system that helps renters compare listings, predict fair rent, review locality scores, and explore market trends through maps, charts, and machine-learning insights.",
        "tech_stack": ["Flask", "scikit-learn", "Chart.js", "Leaflet", "SQLite"],
        "status": "in_progress",
        "category": "Web App",
        "github": "https://github.com/chinmay-476/UrbanMove",
        "demo": None,
        "featured": True,
    },
    {
        "id": 2,
        "title": "Eligibuddy",
        "description": "A Spring Boot and MongoDB platform for managing scholarships, government jobs, schemes, and competitive exams, with secure authentication, documentation pages, and a local assistant integration.",
        "tech_stack": ["Java", "Spring Boot", "MongoDB", "Thymeleaf", "Spring Security", "Ollama"],
        "status": "in_progress",
        "category": "Platform",
        "github": "https://github.com/chinmay-476/eligibuddy",
        "demo": "https://chinmay-476.github.io/eligibuddy/",
        "featured": True,
    },
    {
        "id": 3,
        "title": "Justice4U Criminology",
        "description": "A Flask criminology management system for criminal case records, complaint tracking, role-based workflows, and section and punishment lookup, with real-time video signaling support.",
        "tech_stack": ["Flask", "SQLAlchemy", "MySQL", "Socket.IO", "WebRTC", "Node.js"],
        "status": "in_progress",
        "category": "Case Management",
        "github": "https://github.com/chinmay-476/Justice4U-criminology",
        "demo": None,
        "featured": False,
    },
    {
        "id": 4,
        "title": "Online Plant Nursery Management Store",
        "description": "A Flask plant store application with user authentication, wishlist support, and a server-authoritative checkout and payment flow backed by environment-based configuration.",
        "tech_stack": ["Flask", "Python", "SQLite", "MySQL", "HTML", "CSS"],
        "status": "completed",
        "category": "E-commerce",
        "github": "https://github.com/chinmay-476/online-plant-nursery-managment-store",
        "demo": None,
        "featured": False,
    },
    {
        "id": 5,
        "title": "AdvJava Ecommerce",
        "description": "An advanced Java e-commerce storefront with a refreshed UI, shared styling, database-backed DAO flows for cart, checkout, and orders, plus MySQL setup documentation.",
        "tech_stack": ["Java", "Servlets", "JSP", "MySQL", "HTML", "CSS"],
        "status": "completed",
        "category": "E-commerce",
        "github": "https://github.com/chinmay-476/AdvJava-Ecommerce",
        "demo": None,
        "featured": False,
    },
    {
        "id": 6,
        "title": "Adv Java",
        "description": "An advanced Java dynamic web app using Servlets and JSP to collect client data, validate required fields, and render submission feedback through a simple web workflow.",
        "tech_stack": ["Java", "Servlets", "JSP", "HTML"],
        "status": "completed",
        "category": "Web App",
        "github": "https://github.com/chinmay-476/Adv-java",
        "demo": None,
        "featured": False,
    },
    {
        "id": 7,
        "title": "Reducing Hospital Readmissions",
        "description": "A machine learning project focused on predicting hospital readmission risk for chronic-condition patients through preprocessing, exploratory analysis, risk modeling, and actionable recommendations.",
        "tech_stack": ["Python", "Machine Learning", "Data Analysis", "Pandas", "Scikit-learn"],
        "status": "completed",
        "category": "Machine Learning",
        "github": "https://github.com/chinmay-476/Reducing-Hospital-Readmissions",
        "demo": None,
        "featured": False,
    },
    {
        "id": 8,
        "title": "Justice4U Lawyer",
        "description": "A legal workflow platform that digitally assigns real cases to junior lawyers for supervised handling, with modular Flask routes for public pages, authentication, admin tools, and user portals.",
        "tech_stack": ["Flask", "Python", "HTML", "Role-Based Auth", "Testing"],
        "status": "in_progress",
        "category": "Legal Tech",
        "github": "https://github.com/chinmay-476/Justice4U-lawyer",
        "demo": None,
        "featured": True,
    },
    {
        "id": 9,
        "title": "Portfolio",
        "description": "My first Flask-backed portfolio site combining HTML, CSS, and JavaScript on the frontend to present my work, skills, and contact information.",
        "tech_stack": ["Flask", "HTML", "CSS", "JavaScript"],
        "status": "completed",
        "category": "Portfolio",
        "github": "https://github.com/chinmay-476/portfolio",
        "demo": "/",
        "featured": False,
    },
    {
        "id": 10,
        "title": "Todo List",
        "description": "A browser-based task manager built with HTML, Bootstrap, and JavaScript, featuring styled task entry and a clean productivity-focused interface.",
        "tech_stack": ["HTML", "Bootstrap", "JavaScript", "CSS"],
        "status": "completed",
        "category": "Frontend",
        "github": "https://github.com/chinmay-476/todo-list",
        "demo": None,
        "featured": False,
    },
    {
        "id": 11,
        "title": "Ollama Medical Chatbot",
        "description": "A local medical Q&A assistant built with Flask, FAISS, LangChain, and Ollama to answer questions from a medical PDF reference with retrieval and short-term session memory.",
        "tech_stack": ["Flask", "LangChain", "FAISS", "Ollama", "Python"],
        "status": "completed",
        "category": "AI",
        "github": "https://github.com/chinmay-476/ollamaMedicalChatbot",
        "demo": None,
        "featured": True,
    },
]

skills_data = {
    "Languages": ["Python", "JavaScript", "C++", "Java", "HTML5", "CSS3", "SQL"],
    "Frameworks": ["Flask", "Spring Boot", "Bootstrap", "Jinja"],
    "Tools": ["Git", "GitHub", "VS Code", "SQLite", "MongoDB", "MySQL"],
    "Currently Learning": ["React", "Node.js", "Docker", "Machine Learning", "AI Apps"],
}


@app.context_processor
def inject_globals():
    return {"current_year": datetime.now().year}


@app.route("/")
def home():
    featured_projects = [project for project in projects_data if project.get("featured")][:4]
    stats = {
        "projects": len(projects_data),
        "active": sum(project["status"] == "in_progress" for project in projects_data),
        "skills": sum(len(items) for items in skills_data.values()),
    }
    return render_template(
        "home.html",
        profile=profile_data,
        featured_projects=featured_projects,
        stats=stats,
    )


@app.route("/about")
def about():
    return render_template("about.html", profile=profile_data, skills=skills_data)


@app.route("/projects")
def projects():
    summary = {
        "total": len(projects_data),
        "featured": sum(project["featured"] for project in projects_data),
        "active": sum(project["status"] == "in_progress" for project in projects_data),
    }
    return render_template("projects.html", projects=projects_data, summary=summary)


@app.route("/contact")
def contact():
    return render_template("contact.html", profile=profile_data)


@app.route("/api/projects")
def api_projects():
    return jsonify(projects_data)


@app.route("/api/skills")
def api_skills():
    return jsonify(skills_data)


@app.route("/api/contact", methods=["POST"])
def api_contact():
    data = request.get_json(silent=True) or {}
    required_fields = ["name", "email", "message"]
    missing = [field for field in required_fields if not str(data.get(field, "")).strip()]

    if missing:
        return jsonify({"status": "error", "message": "Please fill in all required fields."}), 400

    return jsonify(
        {
            "status": "success",
            "message": "Thanks for your message. I will get back to you soon.",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
