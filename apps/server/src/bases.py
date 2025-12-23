from .db import *

class Course(db.Model):
    __tablename__ = 'courses'
    
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    quizzes = db.relationship('Quiz', cascade="all, delete-orphan")

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_course = db.Column(UUID(as_uuid=True), db.ForeignKey('courses.uuid'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    attempts = db.Column(db.Integer, default=0)

    questions = db.relationship('Question', cascade="all, delete-orphan")

class Question(db.Model):
    __tablename__ = 'questions'
    
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_quiz = db.Column(UUID(as_uuid=True), db.ForeignKey('quizzes.uuid'), nullable=False)
    type = db.Column(db.Text, nullable=False)
    options = db.Column(ARRAY(db.Text), nullable=False)
    correct = db.Column(ARRAY(db.Integer), nullable=False)
    question = db.Column(db.Text, nullable=False)

class Feed(db.Model):
    __tablename__ = "feed"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = db.Column(db.String(50))
    message = db.Column(db.Text, nullable=False)
    edited = db.Column(db.Boolean, nullable=False, default=False)
    createdAt = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.TIMESTAMP(timezone=True))
    
    uuid_course = db.Column(UUID(as_uuid=True), db.ForeignKey("courses.uuid", ondelete="CASCADE"), nullable=False)

class Material(db.Model):
    __tablename__ = "materials"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    # FILE
    fileUrl = db.Column(db.Text)
    mimeType = db.Column(db.String(100))
    sizeBytes = db.Column(db.Integer)

    # URL
    url = db.Column(db.Text)

    uuid_course = db.Column(UUID(as_uuid=True), db.ForeignKey("courses.uuid", ondelete="CASCADE"), nullable=False)
