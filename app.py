from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return """
    <h1>Welcome to CareerMate 🚀</h1>
    <p>Your AI-powered job application assistant</p>
    
    <h2>Upload Your Details</h2>
    <form method="POST" action="/submit">
        Name: <input type="text" name="name"><br><br>
        Email: <input type="email" name="email"><br><br>
        Skills: <input type="text" name="skills"><br><br>
        <input type="submit" value="Submit">
    </form>
    """

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    skills = request.form.get('skills')

    return f"""
    <h1>Thank you, {name}! 🎉</h1>
    <p>Email: {email}</p>
    <p>Skills: {skills}</p>
    <p>We will start applying to jobs for you soon 👀🔥</p>
    """

if __name__ == '__main__':
    app.run(debug=True)