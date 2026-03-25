from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

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
    "languages": ["Python", "JavaScript", "C++", "Java", "HTML5", "CSS3", "SQL"],
    "frameworks": ["Flask", "Spring Boot", "Bootstrap", "Jinja"],
    "tools": ["Git", "GitHub", "VS Code", "SQLite", "MongoDB", "MySQL"],
    "learning": ["React", "Node.js", "Docker", "Machine Learning", "AI Apps"],
}


@app.route("/")
def home():
    featured_projects = [project for project in projects_data if project.get("featured")][:4]
    return render_template("home.html", featured_projects=featured_projects)


@app.route("/about")
def about():
    return render_template("about.html", skills=skills_data)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_data)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/api/projects")
def api_projects():
    return jsonify(projects_data)


@app.route("/api/skills")
def api_skills():
    return jsonify(skills_data)


@app.route("/api/contact", methods=["POST"])
def api_contact():
    data = request.json
    return jsonify(
        {
            "status": "success",
            "message": "Thanks for your message! I'll get back to you soon.",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
