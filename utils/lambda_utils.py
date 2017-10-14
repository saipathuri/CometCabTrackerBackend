import json


# Creates a response that complies with API Gateway Lambda Proxy Integration
def make_response(body, status_code, headers={'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}):
    response = dict()
    response['headers'] = headers
    response['statusCode'] = status_code
    response['body'] = json.dumps(body)
    response['isBase64Encoded'] = False

    return response
