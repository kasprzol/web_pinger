from http import HTTPStatus

import requests
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class Ping(APIView):
    def post(self, request: Request):
        # body: `{‘url’: ‘https://www.foobar.com‘}`
        body = request.data
        if "url" not in body:
            return Response(
                {"error": "Missing 'url' key in request"},
                status=HTTPStatus.BAD_REQUEST,
            )
        url = body["url"]

        try:
            web_response = requests.get(url, verify=False)
            web_response.raise_for_status()
        except Exception as e:
            return Response(
                {"error": f"the url caused an error: {type(e)}"},
                status=HTTPStatus.BAD_REQUEST,
            )
        return Response({"response": web_response.text})


class Info(APIView):
    def get(self, request: Request):
        return Response({"Receiver": "Cisco is the best!"})
