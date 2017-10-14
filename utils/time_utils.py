from dateutil.tz import tz
from datetime import datetime, timedelta


# Converts the datetime given (UTC) into CST, then returns the time
def convert_datetime_string_to_time(date):
    utc_utz = tz.tzutc()
    central_tz = _get_central_tz()
    date = str(date)
    _datetime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    utc_datetime = _datetime.replace(tzinfo=utc_utz)
    central_datetime = utc_datetime.astimezone(central_tz)

    central_time = central_datetime.time()
    return central_time


# Returns the current datetime for central timezone
def get_current_central_datetime():
    central_tz = _get_central_tz()
    current_datetime_central = datetime.now(tz=central_tz)
    return current_datetime_central


# Returns tz for central time zone
def _get_central_tz():
    central_tz = tz.gettz('America/Chicago')
    return central_tz


# Returns true if current central time is more than 5 seconds greater than time1
def is_delta_5_seconds(time1):
    current_central_datetime = get_current_central_datetime()
    last_updated_time = get_current_central_datetime()
    last_updated_time = last_updated_time.replace(hour=time1.hour, minute=time1.minute, second=time1.second,
                                                  microsecond=time1.microsecond)

    print current_central_datetime
    print last_updated_time

    return current_central_datetime - last_updated_time > timedelta(seconds=5)


# Returns true if current datetime is weekday between 7AM-10PM
def are_cabs_running():
    MIN_HOUR = 7
    MAX_HOUR = 22
    central_datetime = get_current_central_datetime()
    matches_weekday = central_datetime.weekday() <= 4
    matches_hour = MIN_HOUR <= central_datetime.hour <= MAX_HOUR

    if matches_weekday and matches_hour:
        return True
    else:
        return False
