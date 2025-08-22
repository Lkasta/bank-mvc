from sqlalchemy import Column, String, REAL, BIGINT
from src.models.sqlite.settings.base import Base

class IndividualTable(Base):
  __tablename__ = 'individual'

  id = Column(BIGINT, primary_key=True)
  monthly_income = Column(REAL, primary_key=False)
  age = Column(BIGINT, primary_key=False)
  full_name = Column(String, primary_key=False)
  phone = Column(String, primary_key=False)
  email = Column(String, primary_key=False)
  category = Column(String, primary_key=False)
  balance = Column(REAL, primary_key=False)

  def __repr__(self):
    return (
      f"Individual ["
      f"full_name={self.full_name}, "
      f"age={self.age}, "
      f"phone={self.phone}, "
      f"email={self.email}, "
      f"category={self.category}, "
      f"monthly_income={self.monthly_income}, "
      f"balance={self.balance}"
      f"]"
    )
