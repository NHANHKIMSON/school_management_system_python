from flask import Blueprint, render_template, request, redirect
from db.connect import get_db_connection

student_bp = Blueprint('students', __name__)

@student_bp.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)

@student_bp.route("/create", methods=['GET', 'POST'])
def create():
    return render_template('create.html')

@student_bp.route('/submit', methods=['POST'])
def submit():
    firstname = request.form.get('First-Name')
    lastname = request.form.get('Last-Name')
    email = request.form.get('Email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students(first_name, last_name, email)
        VALUES (%s, %s, %s)
    """, (firstname, lastname, email))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/listUser')

@student_bp.route('/listUser')
def list_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('list_students.html', students=students)

@student_bp.route("/update/<int:id>")
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    print("Student:",  student)
    return render_template('update.html', student=student)

@student_bp.route("/update-submit", methods=['POST'])
def update_submit():
    student_id = request.form['id']
    first_name = request.form['First-Name']
    last_name = request.form['Last-Name']
    email = request.form['Email']
    print("data: ", student_id)


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET first_name = %s, last_name = %s, email = %s
        WHERE id = %s
    """, (first_name, last_name, email, student_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/listUser')

@student_bp.route('/remove-user', methods=['POST'])
def remove_user():
    id = request.form['remove-id']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/listUser')
