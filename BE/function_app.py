import azure.functions as func
import datetime
import json
import logging
from controller.AuthController import AuthController

app = func.FunctionApp()


def route_dispatcher(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        routes = {}
    elif req.method == "POST":
        routes = {
            "login": AuthController(req=req).login,
            "register": AuthController(req=req).register,
        }
    elif req.method == "PUT":
        routes = {}
    elif req.method == "PATCH":
        routes = {}
    elif req.method == "DELETE":
        routes = {}
    else:
        return func.HttpResponse("Method not supported", status_code=400)

    route = req.route_params.get("route")
    if route in routes:
        return routes[route](req)
    else:
        return func.HttpResponse("Route not found", status_code=404)


@app.route(route="{route}")
def main(req: func.HttpRequest) -> func.HttpResponse:
    return route_dispatcher(req)
