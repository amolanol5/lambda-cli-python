import requests
import os
import json

# enviroment variables
URL = "http://" + os.environ['URL']


# function
def lambda_handler(event, context):
    response = requests.get(URL)
    print(response)
    return {
               'statusCode': 200,
               'body': json.dumps('Execution success!')
       }