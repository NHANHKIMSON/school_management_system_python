from flask import Flask,render_template, url_for, request,jsonify, redirect
import psycopg2
app = Flask(__name__)


DB_HOST = "ep-snowy-violet-ae183hoz.c-2.us-east-2.aws.neon.tech"
DB_NAME = "neondb"
DB_USER = "neondb_owner" 
DB_PASSWORD = "npg_6IUGwD0ArSPj"


# Connect to database

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
        )


#  index Home page
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    return render_template('index.html', users=users)
# End home page


# Create Users
@app.route("/create", methods=['GET', 'POST'])
def create():
    return render_template('create.html')
# End Create Users


# Submit Form Create Users
@app.route('/submit')
def submit():
    firstname = request.args.get('First-Name')
    lastname = request.args.get('Last-Name')
    email = request.args.get('Email')

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = f"""
                    INSERT INTO users(first_name, last_name, email)
                    VALUES('{firstname}', '{lastname}', '{email}')
                """
        cursor.execute(query=query)
        conn.commit()
        conn.close()
        cursor.close()

        return redirect('/listUser')
    
    return jsonify({
        "First name " : firstname,
        "Last name " : lastname,
        "Email " : email
    })
# End Submit Data Create Users


# List User or Output Data 
@app.route('/listUser', endpoint='listUser')
def list_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users ORDER BY id DESC""")
    users = cursor.fetchall()
    return render_template('list_users.html', users=users)
    # return users
# End List Users




# Update User
@app.route("/update/<id>")
def update(id):
    # return render_template('update.html')
    # return f"Upate id = {id}"
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {id}"
    cursor.execute(query=query)
    conn.commit()
    user = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('update.html', user = user)
# End Update data 


# Submit Data Update 
@app.route("/update-submit", methods=['GET', 'POST'])
def update_submit():
    id = request.form['id']
    first_name = request.form['First-Name']
    last_name = request.form['Last-Name']
    email = request.form['Email']
    query = f"UPDATE users SET first_name = '{first_name}', last_name = '{last_name}', email = '{email}' WHERE id = {id};"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query=query)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('listUser')
# End Submit data Update


# Delete Users
# @app.route("/delete/<id>", methods=['GET', 'POST'])
# def delete(id):
#     conn = get_db_connection()
#     query = f"DELETE FROM users WHERE id = {id};"
#     cursor = conn.cursor()
#     cursor.execute(query=query)
#     conn.commit()
#     cursor.close()
#     conn.close()

#     return redirect(url_for('listUser'))



# Remove user
@app.route('/remove-user', methods=['GET', 'POST'])
def remove_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    id = request.form['remove-id']
    query = f"DELETE FROM users WHERE id = '{id}'"
    cursor.execute(query=query)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/listUser')
    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)    