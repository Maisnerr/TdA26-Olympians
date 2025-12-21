from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

class CourseDB():
    def get():
        courses = Course.query.all()
        mezi = []
        for c in courses:
            mezi.append({
                'uuid': str(c.uuid),
                'title': c.title,
                'description': c.description,
                'created_at': c.created_at.isoformat(),
                'updated_at': c.updated_at.isoformat()
            })
        print("Fetched courses")
        return mezi
    
    def post(title, description):
        new_course = Course(title=title, description=description)
        db.session.add(new_course)
        db.session.commit()
        print("New course added:", new_course.title)
        return {
            'uuid': str(new_course.uuid),
            'title': new_course.title,
            'description': new_course.description,
            'created_at': new_course.created_at.isoformat(),
            'updated_at': new_course.updated_at.isoformat()
        }