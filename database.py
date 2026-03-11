from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://database_c0ib_user:3tHbS3cfXkw9oQlQuw5dLIZbVyks2y4n@dpg-d6ou8pkr85hc739b7h3g-a.oregon-postgres.render.com/database_c0ib')
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    def create_db(self):
        Base.metadata.create_all(engine)

    def drop_db(self):
        Base.metadata.drop_all(engine)

class Conversion(Base):
    __tablename__ = 'conversions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    from_currency: Mapped[str] = mapped_column(String(3))
    to_currency: Mapped[str] = mapped_column(String(3))

    # Сума, яку користувач хоче конвертувати
    amount: Mapped[float] = mapped_column(Float)

    result: Mapped[float] = mapped_column(Float)


base = Base()
base.create_db()


