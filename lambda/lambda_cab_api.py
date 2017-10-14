import boto3
from utils import DBHelper
from utils.lambda_utils import make_response
from utils.time_utils import is_delta_5_seconds
from utils.time_utils import are_cabs_running


# main function for lambda to invoke
def lambda_handler(event, context):
    body = dict()
    cabs = []
    cab_models = DBHelper.get_all_cabs()
    db_was_updated = determine_update(cab_models[0])
    if db_was_updated:
        cab_models = DBHelper.get_all_cabs()
    for cab in cab_models:
        cabs.append(serialize_cab(cab))
    body['cabs'] = cabs
    return make_response(body, 200)


# serialize the cab into a dictionary
# modify the time objects (moved, updated) into isoformat so that it can be serialized into json later
def serialize_cab(cab):
    cab_dict = cab.__dict__
    data = cab_dict['_data']
    data['moved'] = data['moved'].isoformat()
    data['updated'] = data['updated'].isoformat()
    return data


# invokes scraper lambda function
def invoke_scraper():
    client = boto3.client('lambda', region_name="us-east-2")
    client.invoke(FunctionName="cab_tracker_scraper")


# compares last update of cab with current UTC time to determine if we need to update the db before sending response
def determine_update(cab):
    time_updated = cab.updated
    should_update = is_delta_5_seconds(time_updated)
    if should_update and are_cabs_running():
        print 'Updating DB, time was > 5 seconds and cabs are running'
        invoke_scraper()
        return True
    else:
        return False
