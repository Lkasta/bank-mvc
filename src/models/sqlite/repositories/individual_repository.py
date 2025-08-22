from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.individual import IndividualTable

class IndividualRepository:
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection

  def list_individuals(self) -> list[IndividualTable]:
    with self.__db_connection as database:
      try:
        individuals = database.session.query(IndividualTable).all()
        return individuals
      except NoResultFound:
        return []
