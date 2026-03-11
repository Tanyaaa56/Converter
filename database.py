from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('')
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
