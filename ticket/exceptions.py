from rest_framework.exceptions import APIException


class DuplicateTicketError(APIException):
    status_code = 418
    default_detail = 'Вы уже покупали билеты на данный сеанс'
    default_code = 'service_unavailable'
