from . import db

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.Date)
    gender = db.Column(db.String(10))
    
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    student_class = db.relationship('Class', back_populates='students')