from abc import ABC, abstractmethod
from src.models.sqlite.entities.individual import IndividualTable

class IndividalRepositoryInterface(ABC):
  @abstractmethod
  def list_individuals(self) -> list[IndividualTable]:
    pass

  @abstractmethod
  def withdraw(self, individual_id: int, value: float) -> bool:
    pass
