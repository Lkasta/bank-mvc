from src.models.sqlite.interfaces.individual_repository import IndividalRepositoryInterface

class IndividualWithdrawController:
  def __init__(self, individual_repository: IndividalRepositoryInterface) -> None:
    self.__individual_repository = individual_repository

  def withdraw(self, withdraw_info: dict) -> dict:
    individual_id = withdraw_info["individual_id"]
    value = withdraw_info["value"]

    self.__validate_value(value)
    self.__withdraw_value(individual_id, value)
    formated_response = self.__format_response(withdraw_info)
    return formated_response
    
  def __validate_value(self, value) -> None:
    if value < 0:
      raise Exception("The value cannot be less than 0!")
    
  def __withdraw_value(self, individual_id: int, value: float) -> None:
    self.__individual_repository.withdraw(individual_id=individual_id, value=value)

  def __format_response(self, individual_info) -> dict:
    return {
      "data": {
        "count": 1,
        "attributes": individual_info
      }
    }
