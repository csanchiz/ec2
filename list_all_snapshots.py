#!/usr/bin/env python

# [boto3](https://github.com/boto/boto3)

import boto3
accountId='YOUR_ACCOUNT_ID_HERE'

file = open('regions', 'r')
REGIONS=file.read().splitlines()

for region in REGIONS:

	ec2 = boto3.resource('ec2', region_name=region)

	response = ec2.snapshots.filter(
		Filters=[
	        {
	            'Name': 'owner-id',
	            'Values': [
	                accountId,
	            ]
	        },
	    ]
	  
	)
	Snapshots = [s.id for s in response]

	if len(Snapshots) > 0:
		print "\t", len(Snapshots), 'snapshots in', region
		total = 0
		for snap in Snapshots:
			snapshot = ec2.Snapshot(snap)
			print "\t",snapshot.snapshot_id, snapshot.start_time, snapshot.volume_size, "GB"
			total = snapshot.volume_size + total
		print "Total Snapshot capacity in use in", region,"=>", total, "GB"
	else:
		print "No snapshots in " + region