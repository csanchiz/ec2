#!/usr/bin/env python

# [boto3](https://github.com/boto/boto3)

import boto3

file = open('regions', 'r')
REGIONS=file.read().splitlines()

for region in REGIONS:

	ec2 = boto3.resource('ec2', region_name=region)

	response = ec2.volumes.all()

	Volumes = [v.volume_id for v in response]

	if len(Volumes) > 0:
		print "\t", len(Volumes), 'volumes in', region
		total = 0
		for vol in Volumes:
			volume = ec2.Volume(vol)
			print "\t",volume.volume_id, volume.volume_type, volume.size, "GB"
			total = volume.size + total
		print "Total Volume capacity in use in", region,"=>", total, "GB"
	else:
		print "No volumes in " + region