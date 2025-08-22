from .individual_withdraw_controller import IndividualWithdrawController

class MockIndividualRepository:
  def withdraw(self, individual_id: int, value: float):
    pass

def test_withdraw():
  individual_info = {
    "individual_id": 1,
    "value": 125.0
  }

  controller = IndividualWithdrawController(MockIndividualRepository())
  response = controller.withdraw(individual_info)

  print(response)
