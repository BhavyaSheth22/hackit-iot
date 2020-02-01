import boto3
from datetime import datetime
#
class AwSClient():
    def __init__(self, database_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(database_name)
   
    def update(self, data):
        self.table.put_item(Item = {
            'timestamp' : str(datetime.now().timestamp()),
            'blob' : str(data)
        })

    def read(self, key):
        response = self.table.get_item(Key={
            'timestamp' : str(key)
        })

        return response['Item']

if __name__ == '__main__':
    db = AwSClient('fsociety_database')

    db.update("vedanta8a6asda")
    print(db.read(str(1580585038.451585)))

    