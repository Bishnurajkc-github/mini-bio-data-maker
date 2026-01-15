# flask_biodata.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<body style="font-family: Arial; padding: 20px; max-width: 800px; margin: auto;">
    <h2>📄 Web Biodata Maker</h2>

    <form method="POST">
        <h3>👤 Personal Info</h3>
        <input name="name" placeholder="Full Name" required><br>
        <input name="email" placeholder="Email" type="email" required><br>
        <input name="phone" placeholder="Phone" required>

        <h3>🎓 Education</h3>
        <input name="degree" placeholder="Degree"><br>
        <input name="institute" placeholder="Institute">

        <h3>💼 Experience</h3>
        <input name="company" placeholder="Company"><br>
        <input name="position" placeholder="Position">

        <h3>🛠️ Skills</h3>
        <textarea name="skills" placeholder="Skills (comma separated)" rows="3" style="width: 100%;"></textarea>

        <br><br>
        <button type="submit">Generate Biodata</button>
    </form>

    {% if biodata %}
    <hr>
    <div style="border: 1px solid #ccc; padding: 20px; margin-top: 20px; background: #f9f9f9;">
        <h2 style="text-align: center;">BIODATA</h2>
        <p><strong>Name:</strong> {{ biodata.name }}</p>
        <p><strong>Email:</strong> {{ biodata.email }}</p>
        <p><strong>Phone:</strong> {{ biodata.phone }}</p>
        {% if biodata.degree %}<p><strong>Education:</strong> {{ biodata.degree }} ({{ biodata.institute }})</p>{% endif %}
        {% if biodata.company %}<p><strong>Experience:</strong> {{ biodata.position }} at {{ biodata.company }}</p>{% endif %}
        {% if biodata.skills %}<p><strong>Skills:</strong> {{ biodata.skills }}</p>{% endif %}
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def biodata_maker():
    biodata = None

    if request.method == 'POST':
        biodata = {
            'name': request.form.get('name', ''),
            'email': request.form.get('email', ''),
            'phone': request.form.get('phone', ''),
            'degree': request.form.get('degree', ''),
            'institute': request.form.get('institute', ''),
            'company': request.form.get('company', ''),
            'position': request.form.get('position', ''),
            'skills': request.form.get('skills', '')
        }

    return render_template_string(HTML, biodata=biodata)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)