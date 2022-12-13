import json
import logging

import azure.functions as func


async def main(req: func.HttpRequest) -> func.HttpResponse:

    res = {
        "success": True,
        "app": {"app": "Simple Hello World Application", "version": "v0.0.1"},
        "status_code": 200,
    }
    logging.info(res)
    return func.HttpResponse(
        json.dumps(res), status_code=200, mimetype="application/json"
    )
