from flask import Flask, render_template, request, redirect

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Surender", "role": "Developer"},
    {"id": 2, "name": "Sridhar", "role": "Full Stack Developer"}
    {"id": 2, "name": "Vigneshwarar", "role": "Full Stack Developer"}
]

@app.route('/')
def index():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        new_id = len(employees) + 1
        employees.append({"id": new_id, "name": name, "role": role})
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    global employees
    employees = [emp for emp in employees if emp["id"] != id]
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
