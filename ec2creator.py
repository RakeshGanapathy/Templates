import json
import boto3



def lambda_handler(event, context):
    #client
    ec2 = boto3.resource('ec2')
    # create an instance of ec2
    instance = ec2.create_instances(
        ImageId = 'ami-00bf4ae5a7909786c',
        InstanceType=  't2.micro',
        MinCount = 1,
        MaxCount = 1)
        
    print(instance)
    
    print("New instance created :",instance[0].id)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
