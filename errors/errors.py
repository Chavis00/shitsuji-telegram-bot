def unable_connect_api(instance):
    msg = {
        "error": "Unable to connect to" + instance.__class__.__name__ + " API"
    }
    return msg