import csv
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Float, Boolean, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref

app = Flask(__name__)
engine = create_engine("sqlite:///hw.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', backref=backref('books', cascade='all, delete-orphan', lazy='select'))
    students = relationship('ReceivingBook', back_populates='book')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(11))
    email = Column(String(50))
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, default=False)
    books = relationship('ReceivingBook', back_populates='student')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    date_of_issue = Column(DateTime, default=datetime.now)
    date_of_return = Column(DateTime)

    student = relationship('Student', back_populates='books')
    book = relationship('Book', back_populates='students')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(bind=engine)


@app.route('/books/author/<int:author_id>/', methods=['GET'])
def books_by_author(author_id):
    count = session.query(func.sum(Book.count)).join(ReceivingBook).filter(
        Book.author_id == author_id, ReceivingBook.date_of_return == None).scalar()
    return f'Количество оставшихся в библиотеке книг автора с id="{author_id}": {count or 0}'


@app.route('/books/not_read_by_student/<int:student_id>', methods=['GET'])
def recommend_books_by_student(student_id):
    books_id = session.query(ReceivingBook.book_id).filter(ReceivingBook.student_id == student_id).all()
    books_id = [item[0] for item in books_id]
    authors_id = session.query(Book.author_id).filter(ReceivingBook.student_id == student_id).all()
    authors_id = [item[0] for item in authors_id]
    books_by_authors = session.query(Book).filter(Book.author_id.in_(authors_id), ~Book.id.in_(books_id)).all()
    books_list = [book.name for book in books_by_authors]
    return jsonify({'books': books_list})


@app.route('/books/avg', methods=['GET'])
def book_of_the_month():
    current_month = datetime(datetime.now().year, datetime.now().month, 1)
    books_count = session.query(func.count(ReceivingBook.book_id)).filter(
        ReceivingBook.date_of_issue >= current_month).scalar()
    students_count = session.query(func.count(Student.id)).scalar()
    avg = round(books_count / students_count, 2) if students_count != 0 else 0
    return f'Среднее количество книг, которые студенты брали в этом месяце: {avg}'


@app.route('/books/most_popular', methods=['GET'])
def the_most_popular_book():
    book_id = session.query(func.count(ReceivingBook.book_id)). \
        join(Student).filter(Student.average_score >= 4.0).group_by(ReceivingBook.book_id). \
        order_by(func.count(ReceivingBook.book_id).desc()).limit(1).scalar()
    book = session.query(Book).filter(Book.id == book_id).one_or_none()
    result = book.name if book else 'No book found'
    return f'Cамая популярная книга среди студентов, у которых средний балл больше 4.0: {result}'


@app.route('/students/top_10_readers', methods=['GET'])
def get_top_10_readers():
    today = datetime.now()
    start_of_year = datetime(today.year, 1, 1)
    end_of_year = datetime(today.year + 1, 1, 1) - timedelta(days=1)
    top_10_students = session.query(Student.name). \
        join(ReceivingBook).filter(ReceivingBook.date_of_issue.between(start_of_year, end_of_year)). \
        group_by(Student.id). \
        order_by(func.count(ReceivingBook.book_id).desc()).limit(10).all()
    result = ', '.join(student[0] for student in top_10_students)
    return f'ТОП-10 самых читающих студентов в этом году: {result}'


@app.route('/students/upload', methods=['POST'])
def upload_students():
    students_file = request.files.get('students_file')
    if not students_file:
        return 'Файл "students_file" не найден', 400
    try:
        students_file.save('students.csv')
        students_list = []
        with open('students.csv', 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            for student in reader:
                student['scholarship'] = True if student['scholarship'].lower() == 'true' else False
                students_list.append(student)
        session.bulk_insert_mappings(Student, students_list)
    except Exception as e:
        print(e)
        return 'Ошибка при обработке файла "students_file"', 400
    session.commit()
    return 'Студенты из файла "students_file" были успешно добавлены', 200


if __name__ == "__main__":
    app.run()
