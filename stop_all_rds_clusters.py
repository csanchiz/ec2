#!/usr/bin/env python

# [boto3](https://github.com/boto/boto3)

import boto3

file = open('regions', 'r')
REGIONS=file.read().splitlines()

for region in REGIONS:

	client = boto3.client('rds', region_name=region)
	response = client.describe_db_clusters()
	instances = response['DBClusters']

	if len(instances) > 0:

		for instance in instances:			
						
			#print counter, 'instances running in ', region
			db_clusters= "{0}".format(instance['DBClusterIdentifier'])
			print 'Stopping RDS cluster:' ,db_clusters, ' ', instance['Status'], ' ', instance['Engine']
			client.delete_db_cluster(DBClusterIdentifier=db_clusters,FinalDBSnapshotIdentifier=db_clusters+'-final')
	else:

		print "No clusters running in " + region
