from src.controllers.interfaces.individual_withdraw_controller import (
  IndividualWithdrawControllerInterface
)

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class IndividualWithdraw(ViewInterface):
  def __init__(self, controller: IndividualWithdrawControllerInterface):
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    person_info = http_request.body
    body_response = self.__controller.withdraw(person_info)

    return HttpResponse(status_code=200, body=body_response)
