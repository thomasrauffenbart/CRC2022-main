import json
import boto3

dynamodb = boto3.resource('dynamodb')
table =dynamodb.table('Dynamodb_crc_tom')

def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'ID:visits'
        }
    )

    visit_count = response['Item']['counter']
    visit_count = str(int(visit_count)+1)
      
    response = table.put_item(
        Item = {
            'ID':'visits',
            'counter': visit_count
        }
      )

    return{
      'statusCode':200,
      'headers': {
        'Access-Control-Allow-Headers' : '*',
        'Acccess-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods' : 'OPTIONS, POST, GET'
        },
        'body': visit_count
      }