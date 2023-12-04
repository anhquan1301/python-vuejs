from http import HTTPStatus
import azure.functions as func
import datetime
import json
import logging
from controller.AuthController import AuthController
from common.Commons import Commons
from config.db import SessionLocal
from controller.CustomerController import CustomerController
from controller.ProductController import ProductController

app = func.FunctionApp()
db = SessionLocal()


def route_dispatcher(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        routes = {
            "product-list": ProductController(db=db).get_product_list,
            "customer-detail": CustomerController(db=db).get_customer_detail,
        }
    elif req.method == "POST":
        routes = {
            "login": AuthController(db=db).login,
            "register": AuthController(db=db).register,
            "create-product": ProductController(db=db).create_product,
            "create-product-capacity": ProductController(db=db).create_product_capacity,
            "create-customer":CustomerController(db=db).create_customer,
        }
    elif req.method == "PUT":
        routes = {"change-password": AuthController(db=db).change_password}
    elif req.method == "PATCH":
        routes = {}
    elif req.method == "DELETE":
        routes = {}
    else:
        error_message = Commons(db=db).get_message("Method not supported")
        return Commons(db=db).response_func_http(error_message, HTTPStatus.BAD_REQUEST)
    route = req.route_params.get("route")
    if route in routes:
        return routes[route](req)
    else:
        error_message = Commons(db=db).get_message("Route not found")
        return Commons(db=db).response_func_http(error_message, HTTPStatus.NOT_FOUND)


@app.route(route="{route}")
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info(req)
        return route_dispatcher(req)
    except Exception as e:
        logging.error(e)
        error_message = {"message": e.args[0]["message"]}
        return Commons(db=db).response_func_http(
            error_message, e.args[0]["http_status"]
        )
