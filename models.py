'''
Створити таблиці
Автор Ім'я опис
Стаття Заголовок Текст Опис
Тег Назва
Створити зв'язок
Один до багатьох стаття і автор (Автор має декілька статей) але стаття має всього одного автора
і багато до багатьох Стаття І тег
Стаття може мати декілька тегів і тег може мати декілька статей
'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

article_tag_table = db.Table("article_tag_table",
                             db.Column("article_id", db.ForeignKey("article.id")),
                             db.Column("tag_id", db.ForeignKey("tag.id"))
                             )

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    def __str__(self):
        return self.name


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text)
    description = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship('Author', back_populates="article")

    def __str__(self):
        return self.name


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.name
