#!/usr/bin/env python

# [boto3](https://github.com/boto/boto3)

import boto3

file = open('regions', 'r')
REGIONS=file.read().splitlines()

for region in REGIONS:

	client = boto3.client('rds', region_name=region)
	response = client.describe_db_instances()
	instances = response['DBInstances']

	if len(instances) > 0:

		for instance in instances:			
						
			#print counter, 'instances running in ', region
			db_instances = "{0}".format(instance['DBInstanceIdentifier'])
			print 'Stopping RDS instance:' ,db_instances, ' ', instance['DBInstanceStatus'], ' ', instance['Engine']
			client.delete_db_instance(DBInstanceIdentifier=db_instances)
	else:

		print "No instances running in " + region