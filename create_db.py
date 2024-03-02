import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Word


def create_db(engine):
    words = (
        ('Duck', 'Утка'),
        ('Rooster', 'Петух'),
        ('Cow', 'Корова'),
        ('Horse', 'Лошадь'),
        ('Goat', 'Коза'),
        ('Black', 'Черный'),
        ('Blue', 'Синий'),
        ('White', 'Белый'),
        ('Gray', 'Серый'),
        ('Yellow', 'Желтый')
    )
    create_tables(engine)

    for i in words:
        session.add(Word(word=i[0], translate=i[1]))
    session.commit()

engine = sqlalchemy.create_engine('postgresql://postgres:'password'@localhost:5432/tgbot')
Session = sessionmaker(bind=engine)
session = Session()

create_db(engine)

session.close()
