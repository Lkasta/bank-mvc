from sqlalchemy import Column, String, REAL, BIGINT
from src.models.sqlite.settings.base import Base

class IndividualTable(Base):
  __tablename__ = 'individual'

  id = Column(BIGINT, primary_key=True)
  revenue = Column(REAL, primary_key=False)
  age = Column(BIGINT, primary_key=False)
  trade_name = Column(String, primary_key=False)
  phone = Column(String, primary_key=False)
  corporate_email = Column(String, primary_key=False)
  category = Column(String, primary_key=False)
  balance = Column(REAL, primary_key=False)

  def __repr__(self):
    return (
      f"Indivisuals ["
      f"trade_name={self.trade_name}, "
      f"age={self.age}, "
      f"phone={self.phone}, "
      f"corporate_email={self.corporate_email}, "
      f"category={self.category}, "
      f"revenue={self.revenue}, "
      f"balance={self.balance}"
      f"]"
    )
