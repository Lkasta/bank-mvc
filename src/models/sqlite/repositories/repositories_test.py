import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .individual_repository import IndividualRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="db interaction")
def test_list_individuals():
  repo = IndividualRepository(db_connection_handler)
  response = repo.list_individuals()
  print(response)

@pytest.mark.skip(reason="db interaction")
def test_withdraw():
  repo = IndividualRepository(db_connection_handler)
  
  # Teste de saque válido
  response = repo.withdraw(individual_id=1, value=100.0)
  print(f"Saque de R$100 para ID 1: {response}")
  
  # Teste de saque com value maior que saldo
  response = repo.withdraw(individual_id=1, value=999999.0)
  print(f"Saque de R$999999 para ID 1: {response}")
  
  # Teste com ID inexistente
  response = repo.withdraw(individual_id=999, value=50.0)
  print(f"Saque de R$50 para ID 999 (inexistente): {response}")
