#!/usr/bin/env python

# [boto3](https://github.com/boto/boto3)

import boto3

REGIONS=["us-east-1", "us-west-1", "us-west-2", "eu-west-1", "eu-central-1", "ap-northeast-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "sa-east-1"]

for region in REGIONS:

	ec2 = boto3.resource('ec2', region_name=region)

	#client = boto3.client('ec2')

	response = ec2.instances.filter(
	    Filters=[
	        {
	            'Name': 'instance-state-name',
	            'Values': [
	                'running',
	            ]
	        },
	    ]
	  
	)

	Instances = [instance.id for instance in response]


	if len(Instances) > 0:
		print len(Instances), 'instances running in ', region
		print Instances

	else:
		print "No instances running in " + region