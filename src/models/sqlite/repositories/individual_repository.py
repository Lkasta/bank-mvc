from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.individual import IndividualTable
from src.models.sqlite.interfaces.individual_repository import IndividalRepositoryInterface

class IndividualRepository(IndividalRepositoryInterface):
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection

  def list_individuals(self) -> list[IndividualTable]:
    with self.__db_connection as database:
      try:
        individuals = database.session.query(IndividualTable).all()
        return individuals
      except NoResultFound:
        return []

  def withdraw(self, individual_id: int, value: float) -> bool:
    with self.__db_connection as database:
      try:
        individual = (
          database.session
          .query(IndividualTable)
          .filter(IndividualTable.id == individual_id)
          .first()
        )
        
        if not individual:
          return False
        
        if individual.balance < value:
          return False
        
        individual.balance -= value
        
        database.session.commit()
        return True
        
      except Exception as exception:
        database.session.rollback()
        raise exception
