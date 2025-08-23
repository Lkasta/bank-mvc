from abc import ABC, abstractmethod

class IndividualWithdrawControllerInterface(ABC):
  @abstractmethod
  def withdraw(self, withdraw_info: dict) -> dict:
    pass
