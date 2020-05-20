import json
import datetime


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """


    dt = datetime.datetime.today()
    if dt.day == 9 and dt.month == 2:
        birthday = True
    else:
        birthday = False

    if birthday:
        output_text = "Woot Woot! It's Daniel's Birthday!"
    else:
        output_text = "Sadface, today is not Daniel's bday. Check back another day! :)"

    data = {
        'output': output_text,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

