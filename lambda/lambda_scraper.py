import cab_scraper


def lambda_handler(event, context):
    try:
        cab_scraper.run()
    except:
        return 'error'
    return 'success'
