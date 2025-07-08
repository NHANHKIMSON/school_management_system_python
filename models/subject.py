from . import db

class Subject(db.Model):
    __tablename__ = 'subjects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    teachers = db.relationship('Teacher', back_populates='subject')
    grades = db.relationship('Grade', back_populates='subject')