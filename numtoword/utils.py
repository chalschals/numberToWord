from rest_framework.response import Response
from rest_framework import status
from num2words import num2words


def validation(number):
    if not number:
        return False, "Input Number Required"
    if not str(number).isdigit():
        return False, "Input Number Should Be Numeric"
    return True, ""


def requestHandler(reqData):
    isValidReq, errMsg = validation(reqData.get('number', None))
    if not isValidReq:
        return Response({
            "status": errMsg,
            "num_to_english": None,
        }, status=status.HTTP_400_BAD_REQUEST)
    return Response({
        "status": "Ok",
        "num_to_english": num2words(reqData.get('number'))
    }, status=status.HTTP_200_OK)
