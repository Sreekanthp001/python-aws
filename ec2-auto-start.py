# import boto3
# from botocore.exceptions import ClientError

# def start_instances_by_tag(tags, region):
#     ec2 = boto3.client('ec2', region_name=region)
#     #modify tag_filters to look for stopped instances
#     tag_filters = [{ 'Name': f'tag:{key}', 'Values': [value]} for key, value in tags.items()]
#     tag_filters.append({'Name': 'instance-state-name', 'Values': ['stopped']}) # include only stopped instances

#     try:
#         paginator = ec2.get_paginator('describe_instances')
#         page_iterator = paginator.paginate(Filters=tag_filters)

#         instances = []
#         for page in page_iterator:
#             for reservation in page['Reservations']:
#                 for instance in reservation['Instances']:
#                     instance.append(instance['InstanceId'])

        
#         if instances:
#             # use start_instances insted of stop_instances
#             start_response = ec2.start_instances(InstanceIds=instances)
#             print(f'Started instances: {instances}')
#             return start_response
#         else:
#             print('No stopped instances found with the specified tags.')
#     except ClientError as e:
#         print(f'An error occurred: {e}')

# def lambda_handler(event, context):
#     # specify the tag key, value, and region
#     tags = {
#         'AutoStartStop': 'True',
#         'Environment': 'Dev' #example additional tag
#     }
#     region = 'us-east-1'
#     start_instances_by_tag(tags, region)