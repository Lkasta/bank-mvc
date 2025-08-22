from src.models.sqlite.settings.connection import db_connection_handler
from .individual_repository import IndividualRepository

db_connection_handler.connect_to_db()

def test_list_individuals():
  repo = IndividualRepository(db_connection_handler)
  response = repo.list_individuals()
  print(response)
